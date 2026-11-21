# Bias-free market tape: settle EVERY score-settleable outcome on EVERY fixture in the stored board harvests
# (cache/board_*.json = the full SportyBet board, not our picks), at the earliest pre-match price we saw.
# Output: cache/tape_graded/<kick-off date>.jsonl.gz (one row per outcome, grouped by fixture) -> tape_report.py
# Incremental: each run re-grades only the last 6 kick-off days; `python3 tape_grade.py all` rebuilds everything.
# Settlement: football markets on the 90-minute score (+ 1st-half score from Sportradar periods.p1);
# integer O/U and AH lines push -> void (observed SportyBet behaviour, L71/L80). Markets that need the goal
# timeline (1UP/2UP, first goal, early goals, leads-by, goals in a row, player props) are skipped.
# Nov 8: all sports (winner/totals/handicaps incl. OT, set points, hockey regulation) + football corners/bookings.
import json,re,os,sys,time,gzip,csv,datetime as dt,collections,concurrent.futures as cf
import sr
from tapelib import PART_DIR,tape_files,file_date,part_path

FIN=('Ended','AET','AP','Ended after extra time','Ended after penalties','After overtime','AOT','Ended after overtime','After penalties','Retired','Walkover')

def load_tape(d0,d1):
    """Outcomes from the committed tape files harvested between d0 and d1 (inclusive, YYYY-MM-DD), earliest price first."""
    seen={}
    for f in tape_files():
        if not (d0<=file_date(f)<=d1): continue
        with gzip.open(f,'rt') as g:
            for r in csv.reader(g):
                if len(r)!=12: continue
                eid,sport,lg,fx,start,mid,mdesc,spec,desc,oid,odds,hp=r
                k=(eid,mid,spec,oid)
                if k in seen: continue
                try: o=float(odds)
                except ValueError: continue
                if o<=1.0: continue
                seen[k]=dict(eid=eid,sport=sport,lg=lg,fx=fx,start=int(float(start)) if start and start!='None' else None,
                             mid=mid,mdesc=mdesc,spec=spec or None,desc=desc,oid=oid,odds=o,hp=float(hp) if hp and hp!='None' else None)
    return list(seen.values())

def _done(m):
    return bool(m) and (m.get('canceled') or m.get('postponed') or ((m.get('status') or {}).get('name','') in FIN and (m.get('result') or {}).get('home') is not None))

def result(eid,start=None):
    mid=eid.split(':')[-1]
    m=sr.match_info(mid,maxage=None)
    # A match looked up before it finished must not stay cached as "no result" for ever (bug found Nov 21):
    # once its kick-off is 2h+ in the past, re-fetch unless the cached copy is recent.
    if not _done(m) and start and start<time.time()*1000-2*3600e3: m=sr.match_info(mid,maxage=2*3600)
    fin=FIN
    if not m: return None
    if m.get('canceled') or m.get('postponed'): return 'void'
    st=(m.get('status') or {}).get('name','')
    if st not in fin: return None
    r=m.get('result') or {}; p=m.get('periods') or {}
    if r.get('home') is None: return None
    sid=m.get('_sid'); ft=p.get('ft') or {}; h1=p.get('p1') or {}
    # rh/ra = final result incl. OT (sets for tennis/volleyball/table tennis, frames for snooker)
    d=dict(fh=r['home'],fa=r['away'],rh=r['home'],ra=r['away'],winner=r.get('winner'),sid=sid,soccer=(sid==1),
           per=[(p[k]['home'],p[k]['away']) for k in sorted((k for k in p if k[:1]=='p' and k[1:].isdigit()),key=lambda x:int(x[1:])) if isinstance(p[k],dict) and p[k].get('home') is not None])
    if d['soccer']:
        if ft.get('home') is not None: d.update(fh=ft['home'],fa=ft['away'])  # 90 minutes
        if h1.get('home') is not None: d.update(h1h=h1['home'],h1a=h1['away'])
        try: d['stats']=sr.match_stats(m['_id'])
        except Exception: d['stats']=None
    elif sid==4 and len(d['per'])>=3:   # ice hockey: regulation = 3 periods
        d.update(fh=sum(x[0] for x in d['per'][:3]),fa=sum(x[1] for x in d['per'][:3]),h1h=d['per'][0][0],h1a=d['per'][0][1])
    elif sid in (12,137) and h1.get('home') is not None:   # rugby / eFootball: halves like football
        d.update(h1h=h1['home'],h1a=h1['away'])
    return d

def num(spec,key):
    if not spec: return None
    for part in spec.split('|'):
        if part.startswith(key+'='):
            try: return float(part.split('=')[1])
            except Exception: return part.split('=')[1]
    return None

def ou(desc,v,L):
    if L is None or v is None: return None
    if v==L: return 'V'
    if desc.startswith('Over'): return v>L
    if desc.startswith('Under'): return v<L
    return None

def rng(desc,v):
    """'1-3', '2-5+', '3+', '0', '7+', 'No goal' -> bool"""
    d=desc.strip()
    if d.lower() in ('no goal','none'): return v==0
    m=re.fullmatch(r'(\d+)\s*-\s*(\d+)(\+?)',d)
    if m:
        a,b,plus=int(m[1]),int(m[2]),m[3]
        return v>=a if plus else a<=v<=b
    m=re.fullmatch(r'(\d+)\+',d)
    if m: return v>=int(m[1])
    if d.isdigit(): return v==int(d)
    return None

def res1x2(h,a,desc):
    w='Home' if h>a else 'Away' if a>h else 'Draw'
    d=desc.split(' (')[0]
    if d in ('Home','Away','Draw'): return d==w
    if ' or ' in d: return w in d.split(' or ')
    return None

def ah(desc,h,a,L):
    """Asian handicap; L is the handicap applied to HOME (spec hcp=)."""
    if L is None: return None
    m=h-a+L if desc.startswith('Home') else a-h-L
    if abs(L*4-round(L*4))<1e-9 and abs((L*2)-round(L*2))>1e-9:   # quarter line: split stake
        lo,hi=L-0.25,L+0.25
        r1=ah(desc,h,a,lo); r2=ah(desc,h,a,hi)
        return ('Q',r1,r2)
    if abs(m)<1e-9: return 'V'
    return m>0

def eh(desc,h,a,spec):
    """European handicap 'hcp=x:y' 3-way"""
    s=num(spec,'hcp')
    if not isinstance(s,str) or ':' not in s: return None
    x,y=map(int,s.split(':')); return res1x2(h+x,a+y,desc)

def settle(o,r):
    mid,d,spec=o['mid'],o['desc'],o['spec']
    fh,fa=r['fh'],r['fa']; T=fh+fa
    h1h,h1a=r.get('h1h'),r.get('h1a')
    h2h=fh-h1h if h1h is not None else None; h2a=fa-h1a if h1a is not None else None
    L=num(spec,'total'); H=num(spec,'hcp')
    sid=r.get('sid'); rh,ra=r['rh'],r['ra']; per=r.get('per') or []
    if mid in ('186','406','219','251','340'):   # match winner incl. OT / sets / super over (any sport)
        if r.get('winner') in ('home','away'): w=r['winner']
        elif rh!=ra: w='home' if rh>ra else 'away'
        else: return None
        return (w=='home')==(d in ('Home','1')) if d in ('Home','Away','1','2') else None
    if mid in ('225','258','412'): return ou(d,rh+ra,L)            # totals incl. OT
    if mid=='227': return ou(d,rh,L)
    if mid=='228': return ou(d,ra,L)
    if mid in ('223','256','493','366'):                             # handicaps incl. OT / frames / legs
        if H is None: return None
        m=rh-ra+H if d.startswith('Home') else ra-rh-H
        return 'V' if m==0 else m>0
    if mid in ('494','367') and sid in (19,22): return ou(d,rh+ra,L) # snooker frames / darts legs
    if sid in (23,20,5,34) and per:                                  # set sports: points per set
        if mid=='238': return ou(d,sum(a+b for a,b in per),L)
        if mid in ('202','245'):
            k=num(spec,'setnr') or num(spec,'gamenr') or 1
            try: a,b=per[int(k)-1]
            except Exception: return None
            return (a>b)==(d=='Home') if d in ('Home','Away') else None
        if mid=='199' and ':' in d: x,y=d.split(':'); return (int(x),int(y))==(rh,ra)
        return None
    if o['sport']=='football' and mid in ('166','900300','900301','139'):   # corners / bookings from match stats
        S=r.get('stats')
        if not S or L is None: return None
        v={'166':S['hc']+S['ac'],'900300':S['hc'],'900301':S['ac'],'139':(S['hy'] or 0)+(S['ay'] or 0)+(S['hr'] or 0)+(S['ar'] or 0)}[mid]
        return ou(d,v,L)
    if o['sport'] not in ('football','ice hockey','rugby','efootball') and not (sid in (4,12,137,1)): return None
    half=None
    if mid in ('60','63','64','65','66','68','69','70','71','74','75','76','77','78','79','81','552','810001','810002','900036','900037','900031','900032'): half=(h1h,h1a)
    if mid in ('83','85','86','87','88','90','91','92','93','94','95','96','97','98','553','900038','900052','900029','900030'): half=(h2h,h2a)
    if half is not None:
        if half[0] is None: return None
        h,a=half
    else: h,a=fh,fa
    t=h+a
    if mid in ('1','60','83'): return res1x2(h,a,d)
    if mid in ('10','63','85'): return res1x2(h,a,d)
    if mid in ('11','64','86'):
        if h==a: return 'V'
        return (h>a) if d=='Home' else (a>h)
    if mid=='12':  # Home No Bet
        if h>a: return 'V'
        return (h==a) if d=='Draw' else (a>h)
    if mid=='13':
        if a>h: return 'V'
        return (h==a) if d=='Draw' else (h>a)
    if mid in ('14','65','87'): return eh(d,h,a,spec)
    if mid in ('16','66','88'): return ah(d,h,a,H)
    if mid in ('18','68','90'): return ou(d,t,L)
    if mid in ('19','69','91'): return ou(d,h,L)
    if mid in ('20','70','92'): return ou(d,a,L)
    if mid in ('29','75','95'): return (h>0 and a>0)==(d=='Yes')
    if mid in ('26','74','94'): return (t%2==0)==(d=='Even')
    if mid in ('27','900032','900029'): return (h%2==0)==(d=='Even')
    if mid in ('28','900031','900030'): return (a%2==0)==(d=='Even')
    if mid in ('31','76','96'): return (a==0)==(d=='Yes')
    if mid in ('32','77','97'): return (h==0)==(d=='Yes')
    if mid=='30':
        k={'Only Home':h>0 and a==0,'Only Away':a>0 and h==0,'Both teams':h>0 and a>0,'None':t==0}; return k.get(d)
    if mid in ('45','81','98'):
        if ':' not in d: return None
        x,y=d.split(':'); return (h,a)==(int(x),int(y)) if x.isdigit() and y.isdigit() else None
    if mid=='46':
        try: a1,a2=d.split(' '); x1,y1=map(int,a1.split(':')); x2,y2=map(int,a2.split(':'))
        except Exception: return None
        if h1h is None: return None
        return (h1h,h1a,fh,fa)==(x1,y1,x2,y2)
    if mid=='47':
        if h1h is None or '/' not in d: return None
        p,q=d.split('/'); return res1x2(h1h,h1a,p) and res1x2(fh,fa,q)
    if mid in ('21','71','93','25','548','552','553','450001','810001'): return rng(d,t)
    if mid in ('23','450002'): return rng(d,h)
    if mid in ('24','450003'): return rng(d,a)
    if mid in ('450004','810002'): x=rng(d,t); return None if x is None else not x
    if mid=='450005': x=rng(d,h); return None if x is None else not x
    if mid=='450006': x=rng(d,a); return None if x is None else not x
    if mid=='15':
        m=re.fullmatch(r'(Home|Away) by (\d+)(\+?)',d)
        if d=='Draw': return h==a
        if not m: return None
        diff=(h-a) if m[1]=='Home' else (a-h); n=int(m[2])
        return diff>=n if m[3] else diff==n
    if mid in ('56','57'):
        if h1h is None: return None
        s=(h1h>0 and h2h>0) if mid=='56' else (h1a>0 and h2a>0); return s==(d=='Yes')
    if mid=='58':
        if h1h is None: return None
        y=(h1h+h1a>L) and (h2h+h2a>L); return y==(d=='Yes')
    if mid=='59':
        if h1h is None: return None
        y=(h1h+h1a<L) and (h2h+h2a<L); return y==(d=='Yes')
    if mid=='55':
        if h1h is None or '/' not in d: return None
        p,q=d.split('/'); g1=h1h>0 and h1a>0; g2=h2h>0 and h2a>0
        return (g1==(p=='Yes')) and (g2==(q=='Yes'))
    if mid in ('900036','900037','900038','900052','33','34'):
        win_nil=(h>a and a==0) if mid in ('900036','900038','33') else (a>h and h==0)
        return win_nil==(d=='Yes')
    if mid in ('900383','900384'): return None   # needs timeline
    if mid in ('78',):
        if ' & ' not in d: return None
        p,q=d.split(' & '); return res1x2(h,a,p) and ((h>0 and a>0)==(q.lower()=='yes'))
    if mid in ('79','37','547','818','819'):
        if ' & ' not in d: return None
        p,q=d.split(' & ',1)
        if mid in ('818','819'):
            if h1h is None or '/' not in p: return None
            x,y=p.split('/'); r1=res1x2(h1h,h1a,x) and res1x2(fh,fa,y)
            qq=ou(q,(h1h+h1a) if mid=='819' else T,L); return None if qq in (None,'V') else (r1 and qq)
        r1=res1x2(h,a,p); qq=ou(q,t,L); return None if qq in (None,'V') or r1 is None else (r1 and qq)
    if mid in ('35','36'):  # 1X2 & GG
        if ' & ' not in d: return None
        p,q=d.split(' & '); return res1x2(h,a,p) and ((h>0 and a>0)==(q.lower()=='yes'))
    if mid in ('854','858'):  # Home/Away or Over X (OR)
        w=(h>a) if mid=='854' else (a>h); y=(w or t>L); return y==(d=='Yes')
    return None

def grade(tape):
    """Settle a list of tape outcomes -> rows (dicts) plus counters."""
    starts={}
    for o in tape: starts.setdefault(o['eid'],o.get('start'))
    evs=sorted(starts)
    R={}
    with cf.ThreadPoolExecutor(12) as ex:
        for e,r in zip(evs,ex.map(lambda e:_safe_result(e,starts[e]),evs)): R[e]=r
    rows=[]; skipped=0
    for o in tape:
        r=R.get(o['eid'])
        if r is None: continue
        if r=='void': y='V'
        else:
            try: y=settle(o,r)
            except Exception: y=None
        if y is None: skipped+=1; continue
        if isinstance(y,tuple):  # quarter line
            _,a,b=y; ret=sum((o['odds'] if z is True else 1.0 if z=='V' else 0)/2 for z in (a,b))
        else: ret=o['odds'] if y is True else 1.0 if y=='V' else 0.0
        o2=dict(o); o2['ret']=round(ret,4); o2['res']=('V' if y=='V' else 'Q' if isinstance(y,tuple) else 'W' if y else 'L')
        if r!='void': o2.update(score=f"{r['fh']}:{r['fa']}", ht=(f"{r.get('h1h')}:{r.get('h1a')}" if r.get('h1h') is not None else None))
        rows.append(o2)
    done=sum(1 for e in evs if isinstance(R.get(e),dict)); voids=sum(1 for e in evs if R.get(e)=='void')
    return rows,dict(events=len(evs),with_result=done,void=voids,graded=len(rows),unsettleable=skipped)

def _safe_result(eid,start):
    try: return result(eid,start)
    except Exception as ex:
        print('result error',eid,repr(ex)[:120],flush=True); return None

def kick_day(o): return dt.datetime.utcfromtimestamp(o['start']/1000).strftime('%Y-%m-%d') if o.get('start') else None

def run_window(days):
    """(Re)write the graded partition of every kick-off day in `days` (a sorted list of YYYY-MM-DD)."""
    d0=(dt.date.fromisoformat(days[0])-dt.timedelta(days=4)).isoformat(); d1=days[-1]
    tape=[o for o in load_tape(d0,d1) if kick_day(o) in set(days)]
    rows,st=grade(tape) if tape else ([],dict(events=0,with_result=0,void=0,graded=0,unsettleable=0))
    by={d:[] for d in days}        # an empty partition is still written: it marks the day as processed
    for r in rows: by[kick_day(r)].append(r)
    os.makedirs(PART_DIR,exist_ok=True)
    for d,v in by.items():
        v.sort(key=lambda r:(r['eid'],r['mid'],r.get('spec') or '',r['oid']))   # grouped by fixture: reports stream it
        tmp=part_path(d)+'.tmp'
        with gzip.open(tmp,'wt') as f:
            for r in v: f.write(json.dumps(r)+'\n')
        os.replace(tmp,part_path(d))
    print(f"kick-off {days[0]}..{days[-1]}: events {st['events']} with result {st['with_result']} (+{st['void']} void) graded {st['graded']} unsettleable {st['unsettleable']}",flush=True)
    return st

def main():
    """Default: re-grade only the last DAYS kick-off days (results settle within a few days). `all` = full backfill."""
    arg=sys.argv[1] if len(sys.argv)>1 else '6'
    today=dt.datetime.utcnow().date()
    fdays=sorted({file_date(f) for f in tape_files()})
    if not fdays: print('no tape files'); return
    every=[]; d=dt.date.fromisoformat(fdays[0])
    while d<=today: every.append(d.isoformat()); d+=dt.timedelta(days=1)
    if arg=='all': days=every
    else:   # the last N kick-off days, plus any older day that has no partition yet (fresh checkout / lost cache)
        recent=(today-dt.timedelta(days=int(arg))).isoformat()
        days=[x for x in every if x>=recent or not os.path.exists(part_path(x))]
    groups=[]                         # runs of consecutive days, at most 3 per window (bounded memory)
    for x in days:
        if groups and len(groups[-1])<3 and dt.date.fromisoformat(x)-dt.date.fromisoformat(groups[-1][-1])==dt.timedelta(days=1): groups[-1].append(x)
        else: groups.append([x])
    tot=collections.Counter()
    for g in groups: tot.update(run_window(g))
    print(f"TOTAL events {tot['events']} with result {tot['with_result']} (+{tot['void']} void); graded outcomes {tot['graded']}; unsettleable-by-score {tot['unsettleable']}")
if __name__=='__main__': main()
