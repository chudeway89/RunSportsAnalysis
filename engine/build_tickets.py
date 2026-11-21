# ONE reusable ticket builder (replaces the dated one-off scripts build21*.py / build_bb.py / post17-20.py / merge*.py).
# research files -> binding gates (CLAUDE.md section 5) -> live re-price -> tickets -> optional POST with identity check
# and automatic logging to papertrade/tickets.txt.
#
#   python3 build_tickets.py --board cache/allboard_sat21.json --research '../papertrade/research/res21_*.json' \
#           --targets 50,500 --date 2026-11-21 --label 'Sat lottery' [--sport basketball] [--nest] [--post]
#
# --targets a,b[,c,d]  odds targets. Without --nest every ticket uses different fixtures. With --nest (4 targets):
#                      A and B are disjoint, C = A + new fixtures, D = B + new fixtures (each fixture on <= 2 slips).
# --exclude FILE       JSON list of event ids that are already on two of the day's slips (S3).
# Selection ranks legs by the HOUSE probability (cost = -ln p / ln odds): the whole-board study (INSIGHTS.md) showed
# research does not beat the price, so research acts as a filter (vetoes, named mechanism), not as a probability.
import json,math,glob,re,sys,os,time,argparse,collections,datetime as dt
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from post_lib import curl_get,curl_post

JUNK=re.compile(r'women|female|femenina|feminin|wnbl|\bu1\d\b|\bu2\d\b|youth|junior|academy|reserve|espoirs|primavera',re.I)

def gate(leg,fav_p,lg):
    """Return a reason string if the leg breaks a binding rule, else None. `leg`: mid, spec, desc, odds, p, sport."""
    mid,spec,desc,odds,hp,sport=leg['mid'],leg.get('spec') or '',leg['desc'],leg['odds'],leg['p'],leg['sport']
    un=desc.startswith('Under'); ov=desc.startswith('Over')
    if not (1.18<=odds<=2.2): return f'odds {odds} outside 1.18-2.2'
    if un and hp<0.82: return f'Under p {hp:.2f} < 0.82'
    if mid=='10' and 'Home or Away' in desc: return 'Home-or-Away double chance (excluded class)'
    if sport=='football':
        if ov and mid=='18' and re.search(r'total=\d+$',spec): return 'integer-line Over'
        if mid=='16' and 'hcp=' in spec:
            try: h=float(re.search(r'hcp=([-\d.]+)',spec)[1])
            except Exception: h=0.0
            catch=h if desc.startswith('Home') else -h
            if catch>=2.5 and fav_p>=0.60: return '+2.5 catch v favourite p >= 0.60'
            if 1.5<=catch<2.0 and fav_p>=0.55: return '+1.5 catch v favourite p >= 0.55'
        if mid=='1' and desc=='Away' and hp<0.75: return 'away 1X2 p < 0.75'
        if mid in ('166','900301','59'): return 'excluded market class'
    if sport=='basketball':
        if ov and hp<0.74: return f'basketball Over p {hp:.2f} < 0.74'
        if mid=='219' and hp<0.75: return f'basketball ML p {hp:.2f} < 0.75'
        if 'NCAA' in lg and re.search(r'\(\+',desc): return 'NCAA catch in November'
    return None

def learned():
    """Corrections written nightly by learn.py (empty until something clears its evidence bar)."""
    try: return json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','papertrade','learned.json')))
    except Exception: return {}
def band(o): return '<1.30' if o<1.3 else '1.30-1.59' if o<1.6 else '1.60-2.19' if o<2.2 else '2.20-3.99' if o<4 else '4.00+'
def adjust(l,L,side):
    """House p plus the learned calibration correction for this sport x market x side x odds band (if any)."""
    adj=(L.get('calibration') or {}).get('|'.join((l['sport'],l['mid'],(l.get('mdesc') or '')[:40],side,band(l['odds']))),0.0)
    return min(max(l['p']+adj,0.01),0.99),adj

def kind(leg):
    d=leg['desc']
    if d.startswith('Under'): return 'U'
    if d.startswith('Over') or (leg['mid']=='29' and d in ('Yes','GG')): return 'O'
    return 'R'

def build(cands,target,used,ctry_cap=4,max_unders=1,over_frac=0.4,sport_cap=None):
    """Greedy cheapest-cost fill to `target` odds with the concentration rules (S3)."""
    T=[];o=1.0;cc=collections.Counter();sc=collections.Counter();u=0
    for l in sorted((c for c in cands if c['eid'] not in used),key=lambda l:l['cost']):
        if o>=target: break
        if cc[l['ctry']]>=ctry_cap: continue
        if sport_cap and sc[l['sport']]>=sport_cap.get(l['sport'],99): continue
        if l['kind']=='U' and u>=max_unders: continue
        if l['kind']=='O' and len(T)>=5 and sum(x['kind']=='O' for x in T)+1>over_frac*(len(T)+1): continue
        T.append(l);o*=l['odds'];cc[l['ctry']]+=1;sc[l['sport']]+=1;u+=l['kind']=='U'
    return T

def sel(l):
    s={'eventId':l['eid'],'marketId':l['mid'],'outcomeId':l['oid'],'productId':3,'sportId':l['sid']}
    if l.get('spec'): s['specifier']=l['spec']
    return s
KEY=lambda s:(s['eventId'],str(s['marketId']),s.get('specifier') or '',str(s['outcomeId']))

def post(T):
    """Book a ticket and verify every leg's identity on the fetched code. Returns (code, ok, booked)."""
    d=curl_post({'selections':[sel(l) for l in T],'stake':100,'orderType':1}); code=(d.get('data') or {}).get('shareCode')
    v=(curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}').get('data') or {}) if code else {}
    vs=v.get('ticket',{}).get('selections',[])
    return code,({KEY(sel(l)) for l in T}=={KEY(s) for s in vs}),len(vs)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--board',required=True,action='append'); ap.add_argument('--research',required=True,action='append')
    ap.add_argument('--targets',default='50,500'); ap.add_argument('--sport'); ap.add_argument('--exclude')
    ap.add_argument('--nest',action='store_true'); ap.add_argument('--post',action='store_true')
    ap.add_argument('--date',default=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')); ap.add_argument('--label',default='ticket')
    ap.add_argument('--lead-min',type=float,default=45); ap.add_argument('--drift',type=float,default=0.06)
    a=ap.parse_args()
    BE={}
    for b in a.board:
        B=json.load(open(b)); B=B if isinstance(B,list) else B.get('events',[])
        for e in B: BE[e['eid']]=e
    RES=[]
    for pat in a.research:
        for f in sorted(glob.glob(pat)):
            try: RES+=json.load(open(f))
            except Exception as ex: print('unreadable research file',f,ex)
    excl=set(json.load(open(a.exclude))) if a.exclude else set()
    komin=time.time()*1000+a.lead_min*60e3
    LRN=learned(); from learn_keys import side as _side
    legs=[];drop=collections.Counter()
    for r in RES:
        e=BE.get(r.get('eid'))
        if not e or r.get('veto') or e['start']<komin or r['eid'] in excl: continue
        if a.sport and e['sport']!=a.sport: continue
        if JUNK.search(e['lg']) and not any(str(p.get('desc','')).startswith('Over') for p in r.get('picks') or []): continue
        fp=max([o['p'] for o in e['mk'] if o['mid']=='1' and o['desc'] in ('Home','Away')] or [0])
        d=curl_get(f"https://www.sportybet.com/api/ng/factsCenter/event?eventId={r['eid']}&productId=3").get('data') or {}
        for p in r.get('picks') or []:
            mid=str(p.get('mid')); spec=p.get('spec') or ''; desc=p.get('desc'); hit=None
            for m in d.get('markets',[]):
                if str(m['id'])==mid and (m.get('specifier') or '')==spec and m.get('status',0)==0:
                    for o in m['outcomes']:
                        if o['desc']==desc and o.get('isActive',1)==1: hit=(float(o['odds']),float(o.get('probability') or 0),o['id'],m.get('desc',''))
            if not hit: drop['not on the live board']+=1; continue
            odds,hp,oid,mdesc=hit
            if p.get('odds') and odds<float(p['odds'])/(1+a.drift): drop['price drifted against the pick']+=1; continue
            l=dict(eid=r['eid'],sid=e['sid'],sport=e['sport'],fx=e.get('fx') or r.get('fx'),lg=e['lg'],start=e['start'],mid=mid,spec=spec or None,desc=desc,
                   oid=oid,mdesc=mdesc,odds=odds,p=hp,ctry=e['lg'].split(' / ')[0],why=(p.get('why') or '')[:160])
            why=gate(l,fp,e['lg'])
            if why or hp<=0: drop[why or 'no house probability']+=1; continue
            l['kind']=kind(l); l['q'],l['adj']=adjust(l,LRN,_side(l)); l['cost']=-math.log(l['q'])/math.log(odds); legs.append(l)
    print(f"{len(legs)} legs pass the gates ({sum(1 for l in legs if l['adj'])} with a learned correction, learned as of {LRN.get('as_of','never')}); dropped: {dict(drop)}")
    best={}
    for l in sorted(legs,key=lambda l:l['cost']): best.setdefault(l['eid'],l)
    cands=list(best.values()); tg=[float(x) for x in a.targets.split(',')]
    cap={'basketball':4,'ice hockey':2,'volleyball':2,'handball':2} if not a.sport else None
    tickets=[]; used=set()
    if a.nest and len(tg)==4:
        A=build(cands,tg[0],used,3,sport_cap=cap); used|={l['eid'] for l in A}
        B=build(cands,tg[1],used,4,sport_cap=cap); used|={l['eid'] for l in B}
        oA=math.prod(l['odds'] for l in A) or 1; oB=math.prod(l['odds'] for l in B) or 1
        X=build(cands,tg[2]/oA,used,6,max_unders=0,over_frac=0.45,sport_cap=cap); used|={l['eid'] for l in X}
        Y=build(cands,tg[3]/oB,used,7,max_unders=0,over_frac=0.45,sport_cap=cap)
        tickets=[(tg[0],A),(tg[1],B),(tg[2],A+X),(tg[3],B+Y)]
    else:
        for t in tg:
            T=build(cands,t,used,4 if not a.sport else 6,sport_cap=cap); used|={l['eid'] for l in T}; tickets.append((t,T))
    out=[]
    for t,T in tickets:
        if not T: print(f'\ntarget {t:g}x: no legs available'); continue
        O=math.prod(l['odds'] for l in T); P=math.prod(l['p'] for l in T)
        print(f"\ntarget {t:g}x: {len(T)} legs, odds {O:,.1f}, house joint {100*P:.4f}% = 1 in {1/P:,.0f}"+('' if O>=t*0.8 else '  (SHORT of target: pool exhausted)'))
        for l in sorted(T,key=lambda l:l['start']):
            print(f"  {dt.datetime.fromtimestamp(l['start']/1000,dt.timezone.utc):%m-%d %H:%M} | {l['fx'][:40]:40} | {l['mdesc'][:22]:22} {(l['spec'] or ''):11} {l['desc'][:18]:18} | {l['odds']:.2f} | p{l['p']:.3f}")
        rec=dict(target=t,legs=T,odds=O,p=P)
        if a.post:
            code,ok,n=post(T); rec.update(code=code,identity=ok,booked=n)
            print(f"  POSTED {code}: booked {n} of {len(T)}, identity {'OK' if ok else 'MISMATCH - do not use'}")
            if code and ok:
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','papertrade','tickets.txt'),'a') as f:
                    f.write(f"{code}  {a.date}  {a.label} {t:g}x ({len(T)} legs, 1 in {1/P:,.0f})\n")
        out.append(rec)
    json.dump(out,open('cache/tickets_last.json','w'),indent=1)

if __name__=='__main__': main()
