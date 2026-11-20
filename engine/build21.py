# Sat 21 Nov build: research picks -> gates -> live re-price -> 4 tickets with each fixture on <=2 slips.
# Structure: A (50x) and B (500x) disjoint; C (5000x) = A + X; D (50000x) = B + Y; X, Y new fixtures.
import json,math,glob,re,sys,os,collections
sys.path.insert(0,'.')
from post_lib import curl_get,curl_post
SP='/tmp/claude-0/-home-user-gsley/b526d9c8-57a7-5192-8f65-9a58ec7e9e11/scratchpad'
BOARD=json.load(open('cache/board_sat21.json')); BOARD=BOARD if isinstance(BOARD,list) else BOARD['events']
BE={e['eid']:e for e in BOARD}
RES=[x for f in sorted(glob.glob(f'{SP}/res21_G*.json')) for x in json.load(open(f))]
SID={'football':'sr:sport:1','basketball':'sr:sport:2'}
def fav_p(e):
    ps=[o['p'] for o in e['mk'] if o['mid']=='1' and o['desc'] in ('Home','Away')]; return max(ps) if ps else 0
live_cache={}
def live(eid):
    if eid not in live_cache: live_cache[eid]=(curl_get(f'https://www.sportybet.com/api/ng/factsCenter/event?eventId={eid}&productId=3').get('data') or {})
    return live_cache[eid]
def reprice(eid,mid,spec,desc):
    d=live(eid)
    for m in d.get('markets',[]):
        if str(m['id'])==str(mid) and (m.get('specifier') or '')==(spec or '') and m.get('status',0)==0:
            for o in m['outcomes']:
                if o['desc']==desc and o.get('isActive',1)==1: return float(o['odds']),float(o.get('probability') or 0),o['id']
    return None
legs=[];drop=[]
for r in RES:
    e=BE.get(r['eid'])
    if not e or r.get('veto'): continue
    fp=fav_p(e)
    for i,p in enumerate(r.get('picks') or []):
        mid=str(p['mid']); spec=p.get('spec') or ''; desc=p['desc']; why=p.get('why','')
        lp=reprice(r['eid'],mid,spec,desc)
        tag=f"{r['fx']} {mid} {spec} {desc}"
        if not lp: drop.append((tag,'not on live board')); continue
        odds,hp,oid=lp
        if odds<p['odds']/1.06: drop.append((tag,f'drift {p["odds"]}->{odds}')); continue
        if not (1.18<=odds<=2.2): drop.append((tag,f'odds {odds} out of band')); continue
        un=desc.startswith('Under'); ov=desc.startswith('Over')
        if un and hp<0.82: drop.append((tag,f'Under p {hp:.3f}<0.82')); continue
        if ov and mid=='18' and re.search(r'total=\d+$',spec): drop.append((tag,'integer Over')); continue
        if mid=='16':
            h=float(re.search(r'hcp=([-\d.]+)',spec)[1]) if 'hcp' in spec else 0
            catch=(h if desc.startswith('Home') else -h)
            if catch>=2.5 and fp>=0.60: drop.append((tag,'+2.5 v fav>=.60')); continue
            if 1.5<=catch<2.0 and fp>=0.55: drop.append((tag,'+1.5 v fav>=.55')); continue
        if mid=='1' and desc=='Away' and hp<0.75: drop.append((tag,'away 1X2 p<.75')); continue
        if mid=='10' and 'Home or Away' in desc: drop.append((tag,'12 DC')); continue
        m=re.search(r'(?:own est|p≈|p~|~|\()\s*(0\.\d+)',why); own=float(m[1]) if m else hp
        legs.append(dict(eid=r['eid'],sid=SID[e['sport']],fx=r['fx'],lg=e['lg'],ko=__import__('datetime').datetime.utcfromtimestamp(e['start']/1000).strftime('%m-%d %H:%M'),mid=mid,spec=spec or None,desc=desc,oid=oid,
                         odds=odds,p=hp,own=own,conf=r.get('confidence',0.2),tight='tight' in why.lower(),
                         kind='U' if un else 'O' if (ov or 'GG' in desc or (mid=='29' and desc=='Yes')) else 'R',
                         ctry=e['lg'].split(' / ')[0],why=why[:160],mdesc=next((o.get('mdesc') for o in e['mk'] if o['mid']==mid),'')))
print('legs passing gates',len(legs),'dropped',len(drop))
for d in drop: print('  DROP',d)
# one leg per fixture per ticket; best leg per fixture by a blended p (house 70%, research 30%, capped at house+0.06)
for l in legs: l['q']=min(l['p']+0.06,0.7*l['p']+0.3*l['own']); l['cost']=-math.log(l['q'])/math.log(l['odds'])
byfx=collections.defaultdict(list)
for l in legs: byfx[l['eid']].append(l)
for v in byfx.values(): v.sort(key=lambda l:(not l['tight'],l['cost']))
def build(pool_fx,target,used,ctry_cap,maxU=1,over_frac=0.4):
    T=[];o=1.0;cc=collections.Counter();u=0
    cands=[min(byfx[e],key=lambda l:l['cost']) for e in pool_fx if e not in used]
    cands.sort(key=lambda l:l['cost'])
    for l in cands:
        if o>=target: break
        if cc[l['ctry']]>=ctry_cap: continue
        if l['kind']=='U' and u>=maxU: continue
        nO=sum(1 for x in T if x['kind']=='O')+(l['kind']=='O')
        if len(T)>=5 and nO>over_frac*(len(T)+1): continue
        T.append(l);o*=l['odds'];cc[l['ctry']]+=1;u+=l['kind']=='U'
    return T,o
allfx=list(byfx)
A,oA=build(allfx,50,set(),3)
B,oB=build(allfx,500,{l['eid'] for l in A},4)
AB={l['eid'] for l in A+B}
X,oX=build(allfx,5000/oA,AB,6,maxU=0,over_frac=0.45)
Y,oY=build(allfx,50000/oB,AB|{l['eid'] for l in X},7,maxU=0,over_frac=0.45)
if oY<50000/oB*0.8:   # not enough fresh fixtures: top up from X fixtures (they then sit on C and D = 2 slips)
    Y2,oY=build([e for e in allfx if e in {l['eid'] for l in X}]+[l['eid'] for l in Y],50000/oB,AB,8,maxU=0,over_frac=0.45)
    Y=Y2
C=A+X; D=B+Y
def summ(n,T):
    O=math.prod(l['odds'] for l in T); P=math.prod(l['p'] for l in T); Q=math.prod(l['q'] for l in T)
    print(f"\n{n}: legs {len(T)} odds {O:,.1f} house-joint 1 in {1/P:,.0f} (research-adjusted 1 in {1/Q:,.0f}); Overs {sum(l['kind']=='O' for l in T)} Unders {sum(l['kind']=='U' for l in T)}; countries {dict(collections.Counter(l['ctry'] for l in T).most_common(4))}")
    for l in T: print(f"   {l['ko'][:11]:11} {l['fx'][:38]:38} {l['mdesc'][:18]:18} {(l['spec'] or ''):10} {l['desc'][:16]:16} {l['odds']:.2f} p{l['p']:.3f}")
for n,T in (('A 50x',A),('B 500x',B),('C 5000x',C),('D 50000x',D)): summ(n,T)
cnt=collections.Counter(l['eid'] for T in (A,B,C,D) for l in T); assert max(cnt.values())<=2
json.dump(dict(A=A,B=B,C=C,D=D),open('cache/tickets21.json','w'),indent=1)
if os.environ.get('POST')=='1':
    def sel(l):
        s={'eventId':l['eid'],'marketId':l['mid'],'outcomeId':l['oid'],'productId':3,'sportId':l['sid']}
        if l.get('spec'): s['specifier']=l['spec']
        return s
    K=lambda s:(s['eventId'],str(s['marketId']),s.get('specifier') or '',str(s['outcomeId']))
    out={}
    for n,T in (('A50',A),('B500',B),('C5000',C),('D50000',D)):
        d=curl_post({'selections':[sel(l) for l in T],'stake':100,'orderType':1}); code=(d.get('data') or {}).get('shareCode')
        v=(curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}').get('data') or {}) if code else {}
        vs=v.get('ticket',{}).get('selections',[])
        ok={K(sel(l)) for l in T}=={K(s) for s in vs}
        out[n]=dict(code=code,identity=ok,booked=len(vs),legs=len(T),odds=math.prod(l['odds'] for l in T),p=math.prod(l['p'] for l in T))
        print(n,code,'booked',len(vs),'of',len(T),'identity',ok)
    json.dump(out,open('cache/codes21.json','w'),indent=1)
