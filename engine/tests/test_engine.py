# Unit tests for the parts where a silent error costs most: settlement rules, the leg gates, the step-health wrapper
# and the result parser that crashed for 16 days in November.  Run from engine/:  python3 -m unittest discover -s tests
import os,sys,json,unittest,tempfile,subprocess
HERE=os.path.dirname(os.path.abspath(__file__)); ENG=os.path.dirname(HERE)
sys.path.insert(0,ENG); os.chdir(ENG)
import tape_grade,tapelib,build_tickets,sr

def fb(fh,fa,h1=None):
    d=dict(fh=fh,fa=fa,rh=fh,ra=fa,winner=None,sid=1,soccer=True,per=[],stats=None)
    if h1: d.update(h1h=h1[0],h1a=h1[1])
    return d
def o(mid,desc,spec=None,odds=2.0,mdesc=''):
    return dict(eid='sr:match:1',sport='football',mid=mid,spec=spec,desc=desc,mdesc=mdesc,odds=odds,oid='1')

class Settlement(unittest.TestCase):
    def test_1x2(self):
        self.assertIs(tape_grade.settle(o('1','Home'),fb(2,1)),True)
        self.assertIs(tape_grade.settle(o('1','Draw'),fb(2,1)),False)
        self.assertIs(tape_grade.settle(o('1','Away'),fb(0,3)),True)
    def test_over_under_half_line(self):
        self.assertIs(tape_grade.settle(o('18','Over 2.5','total=2.5'),fb(2,1)),True)
        self.assertIs(tape_grade.settle(o('18','Under 2.5','total=2.5'),fb(2,1)),False)
    def test_integer_line_exact_is_void(self):          # L71/L80: Over 3 on exactly 3 goals is refunded
        self.assertEqual(tape_grade.settle(o('18','Over 3','total=3'),fb(2,1)),'V')
        self.assertIs(tape_grade.settle(o('18','Over 3','total=3'),fb(3,1)),True)
        self.assertIs(tape_grade.settle(o('18','Over 3','total=3'),fb(1,1)),False)
    def test_dnb_draw_is_void(self):
        self.assertEqual(tape_grade.settle(o('11','Home'),fb(1,1)),'V')
        self.assertIs(tape_grade.settle(o('11','Home'),fb(2,1)),True)
    def test_asian_handicap_whole_line(self):           # L24: exact margin on a whole-number line is refunded
        self.assertEqual(tape_grade.settle(o('16','Home (-1.0)','hcp=-1'),fb(2,1)),'V')
        self.assertIs(tape_grade.settle(o('16','Home (-1.0)','hcp=-1'),fb(3,1)),True)
        self.assertIs(tape_grade.settle(o('16','Away (+1.5)','hcp=-1.5'),fb(2,1)),True)

class ResultParser(unittest.TestCase):
    def test_period_keys_like_ft_do_not_crash(self):    # the Nov 4-20 crash: sorted() ran int('t') on the 'ft' key
        fake=dict(_id=1,_sid=4,status={'name':'Ended'},result={'home':3,'away':2,'winner':'home'},
                  periods={'ft':{'home':3,'away':2},'p1':{'home':1,'away':0},'p2':{'home':1,'away':1},'p3':{'home':1,'away':1},'ot':{'home':0,'away':0}})
        orig=sr.match_info; sr.match_info=lambda mid,maxage=None:fake
        try: r=tape_grade.result('sr:match:1',start=1)
        finally: sr.match_info=orig
        self.assertEqual(r['per'],[(1,0),(1,1),(1,1)]); self.assertEqual((r['fh'],r['fa']),(3,2))
    def test_unfinished_match_is_refetched_not_cached_forever(self):
        calls=[]
        def fake(mid,maxage=None):
            calls.append(maxage); return dict(_id=1,_sid=1,status={'name':'Not started'},result={})
        orig=sr.match_info; sr.match_info=fake
        try: r=tape_grade.result('sr:match:1',start=1)        # kick-off long ago
        finally: sr.match_info=orig
        self.assertIsNone(r); self.assertEqual(calls,[None,2*3600])

class Gates(unittest.TestCase):
    def leg(self,**k): return dict(dict(mid='18',spec='total=2.5',desc='Over 2.5',odds=1.4,p=0.7,sport='football'),**k)
    def test_ok(self): self.assertIsNone(build_tickets.gate(self.leg(),0.5,'England / Premier League'))
    def test_under_needs_082(self): self.assertIn('Under',build_tickets.gate(self.leg(desc='Under 3.5',spec='total=3.5',p=0.78,odds=1.25),0.5,'x'))
    def test_integer_over(self): self.assertIn('integer',build_tickets.gate(self.leg(desc='Over 3',spec='total=3'),0.5,'x'))
    def test_odds_band(self): self.assertIn('odds',build_tickets.gate(self.leg(odds=1.10),0.5,'x'))
    def test_catch_vs_strong_favourite(self):
        self.assertIn('+2.5',build_tickets.gate(self.leg(mid='16',spec='hcp=2.5',desc='Home (+2.5)',odds=1.3),0.65,'x'))
        self.assertIsNone(build_tickets.gate(self.leg(mid='16',spec='hcp=2',desc='Home (+2.0)',odds=1.3),0.65,'x'))
    def test_away_gate(self): self.assertIn('away',build_tickets.gate(self.leg(mid='1',spec='',desc='Away',odds=1.5,p=0.62),0.62,'x'))
    def test_basketball(self):
        self.assertIn('ML',build_tickets.gate(self.leg(mid='219',spec='',desc='Home',odds=1.3,p=0.72,sport='basketball'),0,'x'))
        self.assertIn('NCAA',build_tickets.gate(self.leg(mid='223',spec='hcp=5.5',desc='Home (+5.5)',odds=1.3,p=0.78,sport='basketball'),0,'USA / NCAA, Regular Season'))
    def test_build_respects_caps_and_target(self):
        c=[dict(eid=str(i),odds=1.3,p=0.76,cost=1.0+i/100,ctry='A' if i<8 else 'B',sport='football',kind='R') for i in range(16)]
        T=build_tickets.build(c,5,set(),ctry_cap=3)
        self.assertLessEqual(sum(l['ctry']=='A' for l in T),3); self.assertEqual(len({l['eid'] for l in T}),len(T))

class Health(unittest.TestCase):
    def test_failure_is_recorded_and_check_fails(self):
        import health
        with tempfile.TemporaryDirectory() as d:
            old=health.F; health.F=os.path.join(d,'health.json')
            try:
                health.main(['reset'])
                self.assertEqual(health.main(['run','good','--',sys.executable,'-c','pass']),0)
                self.assertEqual(health.main(['run','bad','--',sys.executable,'-c','raise SystemExit(3)']),0)   # pipeline goes on
                h=json.load(open(health.F)); self.assertTrue(h['steps']['good']['ok']); self.assertFalse(h['steps']['bad']['ok'])
                self.assertEqual(health.main(['check']),1)
            finally: health.F=old

class Tape(unittest.TestCase):
    def test_file_date_and_order(self):
        self.assertEqual(tapelib.file_date('x/2026-11-20_214234_session.csv.gz'),'2026-11-20')
        self.assertLess('2026-10-12.csv.gz','2026-10-12_000837_ci.csv.gz')
    def test_every_script_compiles(self):
        r=subprocess.run([sys.executable,'-m','compileall','-q','.'],capture_output=True,text=True,cwd=ENG)
        self.assertEqual(r.returncode,0,r.stdout[-400:])

class Learning(unittest.TestCase):
    def test_slice_keys(self):
        import learn_keys as k
        self.assertEqual(k.side(dict(desc='Over 2.5')),'Over'); self.assertEqual(k.side(dict(desc='Home (+1.5)')),'Home receiving')
        self.assertEqual(k.side(dict(desc='Away (-1.0)')),'Away giving'); self.assertEqual(k.band(1.25),'<1.30'); self.assertEqual(k.band(2.2),'2.20-3.99')
    def test_adjust_applies_learned_correction_and_clamps(self):
        l=dict(sport='football',mid='18',mdesc='Over/Under',odds=1.25,p=0.80)
        L={'calibration':{'football|18|Over/Under|Over|<1.30':0.02}}
        q,adj=build_tickets.adjust(l,L,'Over'); self.assertAlmostEqual(q,0.82); self.assertEqual(adj,0.02)
        q,adj=build_tickets.adjust(l,{},'Over'); self.assertEqual((q,adj),(0.80,0.0))

if __name__=='__main__': unittest.main()
