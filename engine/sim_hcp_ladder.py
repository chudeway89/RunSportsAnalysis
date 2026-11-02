import json,numpy as np,sys
from scipy.stats import norm
from scipy.optimize import minimize
S=sys.argv[1]
w=json.load(open(S+'/WZE16X.json')); mk=json.load(open(S+'/WZE_mk.json'))
sels=w['ticket']['selections']
rng=np.random.default_rng(7); N=100000
out=[]; fits={}
for s in sels:
    e=s['eventId']; m=mk[e]
    # devig 223 pairs: home desc vs away desc per spec
    pairs={}
    for x in m['mk']:
        if x['mid']=='223': pairs.setdefault(x['spec'],{})[x['oid']]=x
    pts=[]
    for sp,d in pairs.items():
        if len(d)<2: continue
        h=float(sp.split('=')[1]); ks=sorted(d)
        ph=1/d[ks[0]]['odds']; pa=1/d[ks[1]]['odds']; pa=pa/(ph+pa)
        pts.append((h,pa))  # P(away covers) = P(M + h < 0) -> M < -h
    tots={}
    for x in m['mk']:
        if x['mid']=='225': tots.setdefault(x['spec'],{})[x['oid']]=x
    def f(v):
        mu,sd=v; return sum((norm.cdf((-h-mu)/sd)-pa)**2 for h,pa in pts)
    r=minimize(f,[-25,12],method='Nelder-Mead'); mu,sd=r.x
    fits[e]=(mu,sd,len(pts))
    h=float(s['specifier'].split('=')[1]); odds=None
    for x in m['mk']:
        if x['mid']=='223' and x['spec']==s['specifier'] and x['oid']==s['outcomeId']: odds=x['odds']
    out.append(dict(eid=e,fx=m['fx'],ko=m['ko'],h=h,odds=odds,mu=mu,sd=sd,p=norm.cdf((-h-mu)/sd),
        alts=sorted([(float(x['spec'].split('=')[1]),x['odds'],x['oid']) for x in m['mk'] if x['mid']=='223' and x['oid']==s['outcomeId']])))
def sim(legs,shared=2.5):
    Z=rng.normal(0,shared,N) if shared else 0
    alive=np.ones(N,bool)
    for L in legs:
        M=rng.normal(L['mu'],L['sd'],N)+Z   # Z>0: home (favourite here) does better? mu negative means home fav? check sign
        alive&=(M< -L['h'])
    return alive.mean()
for L in sorted(out,key=lambda L:-L['p']):
    print(f"{L['fx'][:42]:42} h={L['h']:6} @{L['odds']} mu={L['mu']:6.1f} sd={L['sd']:4.1f} p={L['p']:.3f} EV={L['p']*L['odds']:.3f} alts={[(a,o) for a,o,_ in L['alts']]}")
tot=np.prod([L['odds'] for L in out])
pi=np.prod([L['p'] for L in out])
print('odds',round(tot),'indep 1 in',round(1/pi),'corr2.5 1 in',round(1/max(sim(out),1e-9)),'corr0',round(1/max(sim(out,0),1e-9)))
json.dump(out,open(S+'/wze_legs.json','w'))
