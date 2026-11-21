# 100,000 independent simulations of EVERY fixture on the board; settles every priced leg of that fixture on the same draws.
# Usage: python3 fixsim.py <baseline.json> [out.json=cache/fixsim04.json] [legs.json=cache/winmodel_legs.json]
# The legs file must be the one `winmodel.py price` wrote for THIS board: the script refuses to run when it is older
# than the baseline (the Nov 14-15 runs silently re-simulated Nov 12 legs).
import json,sys,os,collections,numpy as np
BASEF=sys.argv[1]; OUTF=sys.argv[2] if len(sys.argv)>2 else 'cache/fixsim04.json'; LEGF=sys.argv[3] if len(sys.argv)>3 else 'cache/winmodel_legs.json'
if os.path.getmtime(LEGF)<os.path.getmtime(BASEF)-60 and not os.environ.get('ALLOW_STALE'):
    sys.exit(f'STALE INPUT: {LEGF} is older than {BASEF}. Run `python3 winmodel.py price <board> <auto.json>` first (or set ALLOW_STALE=1).')
L=json.load(open(LEGF)); BASE={b['eid']:b for b in json.load(open(BASEF))}
N=100000; rng=np.random.default_rng(4)
def settle(x,draw):
    m,sp,d=x['mid'],x['spec'] or '',x['desc']
    if x['sport']=='football':
        h,a=draw;t=h+a;mg=h-a
        if m=='1': return np.where({'Home':mg>0,'Draw':mg==0,'Away':mg<0}[d],1,-1)
        if m=='11': w=(mg>0) if d=='Home' else (mg<0); return np.where(mg==0,0,np.where(w,1,-1))
        if m=='10': return np.where({'Home or Draw':mg>=0,'Draw or Away':mg<=0,'Home or Away':mg!=0}[d],1,-1)
        if m=='16': hc=float(sp.split('=')[1]); return np.sign((mg+hc) if d.startswith('Home') else (-mg-hc))
        if m in('18','19','20'): ln=float(sp.split('=')[1]); v={'18':t,'19':h,'20':a}[m]; return np.sign((v-ln) if d.startswith('Over') else (ln-v))
        if m in('450001','450002','450003'):
            v={'450001':t,'450002':h,'450003':a}[m]; lo,hi=d.split('-'); lo=int(lo)
            return np.where((v>=lo) if hi.endswith('+') else ((v>=lo)&(v<=int(hi))),1,-1)
        if m in('29','50'): return np.where(((h>0)&(a>0))==(d=='Yes'),1,-1)
    else:
        T,M=draw
        if m=='225': ln=float(sp.split('=')[1]); return np.sign((T-ln) if d.startswith('Over') else (ln-T))
        if m=='223': hc=float(sp.split('=')[1]); return np.sign((M+hc) if d.startswith('Home') else (-M-hc))
        if m=='219': return np.where((M>0) if d=='Home' else (M<0),1,-1)
    return None
G=collections.defaultdict(list)
for x in L: G[x['eid']].append(x)
out=[]
for eid,xs in G.items():
    x0=xs[0]
    if x0['sport']=='football' and x0.get('lam'):
        lh,la=x0['lam']; draw=(rng.poisson(lh,N),rng.poisson(la,N))
    elif x0['sport']=='basketball' and eid in BASE and x0.get('mu'):
        b=BASE[eid]; draw=(rng.normal(x0['mu'][0],b['sdT'],N),rng.normal(x0['mu'][1],b['sdM'],N))
    else: continue
    for x in xs:
        try: r=settle(x,draw)
        except Exception: r=None
        if r is None: continue
        w=float((r==1).mean()); v=float((r==0).mean())
        out.append(dict(x,sim=w,simv=v,simev=w*x['odds']+v))
json.dump(out,open(OUTF,'w'))
fx={o['eid'] for o in out}
print(len(fx),'fixtures simulated x',N,'| legs settled',len(out),'->',OUTF)
d=np.array([o['sim']-o['p'] for o in out if o['simv']==0]); print('sim vs model p: mean abs diff %.4f, max %.4f'%(abs(d).mean(),abs(d).max()))
