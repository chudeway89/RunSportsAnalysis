# Weekend basketball ticket: researched picks (Sat res21_* + Sun resB*) -> basketball gates -> live re-price -> one ticket to TARGET.
import json,math,glob,re,sys,os,collections,time
sys.path.insert(0,'.')
from post_lib import curl_get,curl_post
SP='/tmp/claude-0/-home-user-gsley/b526d9c8-57a7-5192-8f65-9a58ec7e9e11/scratchpad'
TARGET=float(os.environ.get('TARGET','5000'))
BE={}
for f in ('cache/allboard_sat21.json','cache/bbsun22.json'):
    for e in json.load(open(f)):
        if e['sport']=='basketball': BE[e['eid']]=e
RES=[]
for f in glob.glob('../papertrade/research/res21_*.json')+glob.glob(f'{SP}/resB*.json'):
    try: RES+=json.load(open(f))
    except Exception as ex: print('BAD',f,ex)
KOMIN=time.time()*1000+45*60e3
EXCL=set(json.load(open('cache/excl_bb.json')))
junk=re.compile(r'women|female|femenina|feminin|wnbl|u1\d|u2\d|youth|junior|academy|reserve|\bii\b| 2$| b$|espoirs',re.I)
def reprice(eid,mid,spec,desc):
    d=curl_get(f'https://www.sportybet.com/api/ng/factsCenter/event?eventId={eid}&productId=3').get('data') or {}
    for m in d.get('markets',[]):
        if str(m['id'])==str(mid) and (m.get('specifier') or '')==(spec or '') and m.get('status',0)==0:
            for o in m['outcomes']:
                if o['desc']==desc and o.get('isActive',1)==1: return float(o['odds']),float(o.get('probability') or 0),o['id'],m.get('desc','')
    return None
legs=[];drop=[]
for r in RES:
    e=BE.get(r.get('eid'))
    if not e or r.get('veto') or e['start']<KOMIN or r.get('eid') in EXCL: continue
    if junk.search(e['lg']) or junk.search(e['home']) or junk.search(e['away']): continue
    for p in r.get('picks') or []:
        mid=str(p['mid']); spec=p.get('spec') or ''; desc=p['desc']; tag=f"{r['fx']} | {desc}"
        lp=reprice(r['eid'],mid,spec,desc)
        if not lp: drop.append((tag,'not live')); continue
        odds,hp,oid,mdesc=lp
        if odds<p['odds']/1.06: drop.append((tag,f'drift {p["odds"]}->{odds}')); continue
        if not (1.18<=odds<=2.2): drop.append((tag,f'odds {odds}')); continue
        tot=desc.startswith(('Over','Under'))
        if desc.startswith('Under') and hp<0.82: drop.append((tag,f'Under p {hp:.2f}')); continue
        if desc.startswith('Over') and hp<0.74: drop.append((tag,f'Over p {hp:.2f}<.74')); continue
        if mid=='219' and hp<0.75: drop.append((tag,f'ML p {hp:.2f}<.75')); continue
        if 'NCAA' in e['lg'] and re.search(r'\(\+',desc): drop.append((tag,'NCAA catch (Nov)')); continue
        legs.append(dict(eid=r['eid'],sid=e['sid'],fx=r['fx'],lg=e['lg'],ko=e['ko'],start=e['start'],mid=mid,spec=spec or None,desc=desc,oid=oid,mdesc=mdesc,
                         odds=odds,p=hp,kind='U' if desc.startswith('Under') else 'O' if desc.startswith('Over') else 'R',ctry=e['lg'].split(' / ')[0],
                         cost=-math.log(hp)/math.log(odds),why=(p.get('why') or '')[:140]))
print('legs passing',len(legs),'dropped',len(drop))
for d in drop: print('  DROP',d)
best={}
for l in sorted(legs,key=lambda l:l['cost']): best.setdefault(l['eid'],l)
T=[];o=1.0;cc=collections.Counter();lgc=collections.Counter();u=0
for l in sorted(best.values(),key=lambda l:l['cost']):
    if o>=TARGET: break
    if cc[l['ctry']]>=6 or lgc[l['lg']]>=4: continue
    if l['kind']=='U' and u>=2: continue
    nO=sum(x['kind']=='O' for x in T)
    if l['kind']=='O' and len(T)>=5 and nO+1>0.5*(len(T)+1): continue
    T.append(l);o*=l['odds'];cc[l['ctry']]+=1;lgc[l['lg']]+=1;u+=l['kind']=='U'
P=math.prod(l['p'] for l in T)
print(f"\nTICKET legs {len(T)} odds {o:,.1f} house-joint {100*P:.4f}% = 1 in {1/P:,.0f}; Overs {sum(l['kind']=='O' for l in T)} Unders {u}; leagues {dict(lgc.most_common(5))}")
for l in sorted(T,key=lambda l:l['start']): print(f"  {l['ko']} | {l['lg'][:26]:26} | {l['fx'][:40]:40} | {l['mdesc'][:22]:22} {(l['spec'] or ''):12} {l['desc'][:18]:18} | {l['odds']:.2f} | p{l['p']:.3f}")
json.dump(T,open('cache/ticket_bb.json','w'),indent=1)
if os.environ.get('POST')=='1':
    def sel(l):
        s={'eventId':l['eid'],'marketId':l['mid'],'outcomeId':l['oid'],'productId':3,'sportId':l['sid']}
        if l.get('spec'): s['specifier']=l['spec']
        return s
    K=lambda s:(s['eventId'],str(s['marketId']),s.get('specifier') or '',str(s['outcomeId']))
    d=curl_post({'selections':[sel(l) for l in T],'stake':100,'orderType':1}); code=(d.get('data') or {}).get('shareCode')
    v=(curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}').get('data') or {}) if code else {}
    vs=v.get('ticket',{}).get('selections',[])
    print('POSTED',code,'booked',len(vs),'of',len(T),'identity',{K(sel(l)) for l in T}=={K(s) for s in vs})
