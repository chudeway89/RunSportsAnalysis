import json,math,os,sys
sys.path.insert(0,'.')
from post_lib import curl_post,curl_get
L=json.load(open('cache/winmodel_legs.json')); T=json.load(open('cache/tickets.json'))
def find(fx,mid,spec,desc):
    c=[l for l in L if fx in l['fx'] and l['mid']==mid and (l.get('spec') or '')==spec and l['desc'].startswith(desc)]
    assert len(c)==1,(fx,mid,spec,desc,len(c)); return c[0]
MAIN=[find('PSG v Barcelona','16','hcp=-1.5','Away'),find('Napoli v Bodoe','16','hcp=-2.5','Away'),
      find('Fenerbahce Istanbul v Slavia','16','hcp=-2.5','Away'),find('Wolves v Portsmouth','18','total=1.5','Over'),
      find('Stuttgart v Atletico','16','hcp=1.5','Home')]
tickets={'MAIN':MAIN,'T500':T['500']['legs'],'T5000':T['5000']['legs'],'T50000':T['50000']['legs']}
def sel(l):
    s={'eventId':l['eid'],'marketId':l['mid'],'outcomeId':l['oid'],'productId':3,'sportId':l['sid']}
    if l.get('spec'): s['specifier']=l['spec']
    return s
K=lambda s:(s['eventId'],str(s['marketId']),s.get('specifier') or '',str(s['outcomeId']))
res={}
for name,LL in tickets.items():
    assert len({l['eid'] for l in LL})==len(LL)
    d=curl_post({'selections':[sel(l) for l in LL],'stake':100,'orderType':1}); code=(d.get('data') or {}).get('shareCode')
    v=curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}')['data'] if code else {}
    vs=v.get('ticket',{}).get('selections',[]) if v else []
    ok={K(sel(l)) for l in LL}=={K(s) for s in vs}
    O=math.prod(l['odds'] for l in LL); P=math.prod(l['p']+l.get('pp',0) for l in LL); Pw=math.prod(l['p'] for l in LL)
    res[name]=dict(code=code,legs=len(LL),odds=O,p=P,pw=Pw,identity=ok,L=[{k:l.get(k) for k in('fx','lg','ko','mdesc','spec','desc','odds','p','pp','sport','conf','flags')} for l in LL])
    print(f"{name}: {code} legs {len(LL)} (booked {len(vs)}) odds {O:,.1f} survive 1 in {1/P:,.1f} allwin 1 in {1/Pw:,.1f} identity {ok}")
json.dump(res,open('cache/codes_1020.json','w'),indent=1)
