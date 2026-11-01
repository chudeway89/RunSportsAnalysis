# Bias-free market tape: settle EVERY score-settleable outcome on EVERY fixture in the stored board harvests
# (cache/board_*.json = the full SportyBet board, not our picks), at the earliest pre-match price we saw.
# Output: ../papertrade/tape_graded.jsonl (one row per outcome) -> analyse with tape_report.py
# Settlement: football markets on the 90-minute score (+ 1st-half score from Sportradar periods.p1);
# integer O/U and AH lines push -> void (observed SportyBet behaviour, L71/L80). Markets that need the goal
# timeline (1UP/2UP, first goal, early goals, leads-by, goals in a row, player props) are skipped.
import json,glob,re,os,sys,concurrent.futures as cf
import sr
OUT='../papertrade/tape_graded.jsonl'

def load_tape():
    seen={}
    for f in sorted(glob.glob('cache/board_*.json'), key=os.path.getmtime):
        ev=json.load(open(f)); ev=ev if isinstance(ev,list) else ev.get('events',[])
        for e in ev:
            for o in e.get('mk',[]):
                k=(e['eid'],o['mid'],o.get('spec'),o['oid'])
                if k in seen: continue
                seen[k]=dict(eid=e['eid'],sport=e['sport'],lg=e.get('lg'),fx=e.get('fx'),ko=e.get('ko'),start=e.get('start'),
                             mid=o['mid'],mdesc=o.get('mdesc'),spec=o.get('spec'),desc=o['desc'],oid=o['oid'],
                             odds=o.get('odds'),hp=o.get('p'))
    import gzip,csv
    for f in sorted(glob.glob('../papertrade/tape/*.csv.gz')):   # committed tape (written daily by tape_store.py)
        with gzip.open(f,'rt') as g:
            for r in csv.reader(g):
                eid,sport,lg,fx,start,mid,mdesc,spec,desc,oid,odds,hp=r
                k=(eid,mid,spec or None,oid)
                if k in seen: continue
                seen[k]=dict(eid=eid,sport=sport,lg=lg,fx=fx,ko=None,start=int(start) if start and start!='None' else None,
                             mid=mid,mdesc=mdesc,spec=spec or None,desc=desc,oid=oid,odds=float(odds),hp=float(hp) if hp and hp!='None' else None)
    return list(seen.values())

def result(eid):
    mid=eid.split(':')[-1]
    m=sr.match_info(mid,maxage=None)
    fin=('Ended','AET','AP','Ended after extra time','Ended after penalties','After overtime','AOT','Ended after overtime')
    if not m or ((m.get('status') or {}).get('name','') not in fin and not m.get('canceled') and not m.get('postponed')):
        m=sr.match_info(mid,maxage=0)   # cached copy was pre-match: refetch
    if not m: return None
    if m.get('canceled') or m.get('postponed'): return 'void'
    st=(m.get('status') or {}).get('name','')
    if st not in ('Ended','AET','AP','Ended after extra time','Ended after penalties','After overtime','AOT','Ended after overtime'): return None
    r=m.get('result') or {}; p=m.get('periods') or {}
    if r.get('home') is None: return None
    ft=p.get('ft') or {}; h1=p.get('p1') or {}
    d=dict(fh=r['home'],fa=r['away'],soccer=(m.get('_sid')==1))
    if d['soccer']:
        if ft.get('home') is not None: d.update(fh=ft['home'],fa=ft['away'])  # 90 minutes
        if h1.get('home') is not None: d.update(h1h=h1['home'],h1a=h1['away'])
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
    if o['sport']!='football':
        if mid in ('219','251'): return res1x2(fh,fa,d) if d in ('Home','Away') else None
        if mid in ('225','258'): return ou(d,T,L)
        if mid=='227': return ou(d,fh,L)
        if mid=='228': return ou(d,fa,L)
        if mid in ('223','256'):
            if H is None: return None
            m=fh-fa+H if d.startswith('Home') else fa-fh-H
            return 'V' if m==0 else m>0
        return None
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

def main():
    tape=load_tape()
    sports={'football','basketball','baseball'}
    tape=[o for o in tape if o['sport'] in sports and o.get('odds') and o['odds']>1.0]
    evs=sorted({o['eid'] for o in tape})
    print('outcomes',len(tape),'events',len(evs),flush=True)
    R={}
    with cf.ThreadPoolExecutor(12) as ex:
        for i,(e,r) in enumerate(zip(evs,ex.map(result,evs))):
            R[e]=r
            if i%300==0: print('results',i,len(evs),flush=True)
    n=0; skipped=0
    with open(OUT,'w') as f:
        for o in tape:
            r=R.get(o['eid'])
            if r is None: continue
            if r=='void': y='V'
            else:
                try: y=settle(o,r)
                except Exception: y=None
            if y is None: skipped+=1; continue
            if isinstance(y,tuple):  # quarter line
                _,a,b=y; pay=0
                for z in (a,b): pay+= (o['odds'] if z is True else 1.0 if z=='V' else 0)/2
                ret=pay
            else: ret=o['odds'] if y is True else 1.0 if y=='V' else 0.0
            o2=dict(o); o2['ret']=round(ret,4); o2['res']=('V' if y=='V' else 'Q' if isinstance(y,tuple) else 'W' if y else 'L')
            if r!='void': o2.update(score=f"{r['fh']}:{r['fa']}", ht=(f"{r.get('h1h')}:{r.get('h1a')}" if r.get('h1h') is not None else None))
            f.write(json.dumps(o2)+'\n'); n+=1
    done=sum(1 for e in evs if isinstance(R.get(e),dict)); voids=sum(1 for e in evs if R.get(e)=='void')
    print(f'events with results {done} (+{voids} void) of {len(evs)}; graded outcomes {n}; unsettleable-by-score {skipped}')
if __name__=='__main__': main()
