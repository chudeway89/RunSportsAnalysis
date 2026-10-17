import json,math,os,sys,collections
sys.path.insert(0,'.')
from post_lib import curl_post,curl_get
os.environ.setdefault('KOMIN','10-17 17:00')
g={}; exec(open('pick.py').read().split("out={}; base=None")[0],g)   # gates, pool, cost
T=json.load(open('cache/tickets.json'))
ladder_eids={x['eid'] for x in T['500']['legs']}
OK=g['OK']
def best_per_fixture(L):
    b={}
    for x in L:
        if x['eid'] not in b or x['cost']<b[x['eid']]['cost']: b[x['eid']]=x
    return sorted(b.values(),key=lambda x:x['cost'])
# 80% ticket: every leg wins outright >=0.80, odds>=1.18, not on the 500x base, <=1 per country
c80=[x for x in best_per_fixture([x for x in OK if x['p']>=0.80 and x['odds']>=1.18]) if x['eid'] not in ladder_eids]
H=[];cc=collections.Counter()
for x in c80:
    if cc[g['country'](x)]>=1: continue
    H.append(x); cc[g['country'](x)]+=1
    if len(H)==6: break
# basketball-only ticket
bk=best_per_fixture([x for x in OK if x['sport']=='basketball' and x['odds']>=1.2])
BK=[];cc=collections.Counter()
for x in bk:
    if cc[x['lg']]>=2: continue
    BK.append(x); cc[x['lg']]+=1
    if len(BK)==6: break
tickets={'T500':T['500']['legs'],'T5000':T['5000']['legs'],'T50000':T['50000']['legs'],'MAX':T['1000000000000']['legs'],'P80':H,'BASKET':BK}
def sel(l):
    s={'eventId':l['eid'],'marketId':l['mid'],'outcomeId':l['oid'],'productId':3,'sportId':l['sid']}
    if l.get('spec'): s['specifier']=l['spec']
    return s
res={}
for name,L in tickets.items():
    d=curl_post({'selections':[sel(l) for l in L],'stake':100,'orderType':1}); code=(d.get('data') or {}).get('shareCode')
    v=curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}') if code else {}
    vs=(v.get('data') or {}).get('ticket',{}).get('selections',[]) if v else []
    K=lambda s:(s['eventId'],str(s['marketId']),s.get('specifier') or '',str(s['outcomeId']))
    ok={K(sel(l)) for l in L}=={K(s) for s in vs}
    O=math.prod(l['odds'] for l in L); P=math.prod(l['p']+l.get('pp',0) for l in L); Pw=math.prod(l['p'] for l in L)
    res[name]=dict(code=code,legs=len(L),odds=O,p=P,pw=Pw,identity=ok,L=[{k:l[k] for k in('fx','lg','ko','mdesc','spec','desc','odds','p','sport')} for l in L])
    print(f"{name}: {code} legs {len(L)} odds {O:,.1f} survive 1 in {1/P:,.0f} allwin 1 in {1/Pw:,.0f} identity {ok}")
json.dump(res,open('cache/codes_1017.json','w'),indent=1)
