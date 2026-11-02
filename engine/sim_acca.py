import json,math,re,sys,os,io,contextlib,importlib.util,collections
import numpy as np
os.environ.setdefault('KOMIN','11-02 22:30')
sys.argv=['pick.py','5']
spec=importlib.util.spec_from_file_location('pk','pick.py'); pk=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(pk)
BASE={b['eid']:b for b in json.load(open('cache/baseline03.json'))}
THIN=re.compile(r'Saudi Arabia / (Second|Division 1)|Guatemala|Uganda|Indonesia|Egypt / League Cup|Rwanda|India|Jamaica|Sergipano|Montenegro|Venezuela|Scotland / Challenge Cup|Isthmian|Northern Premier|Southern League|National League South|Gulf Club|AFC Champions League Two|Paraguay|Tunisia|Uruguay',re.I)
def ok(x):
    if x['odds']<1.15 or THIN.search(x['lg']): return False
    if x['eid']=='sr:match:66887146': return False          # Bragantino-Santos: Santos +1.5 rests on a gutted Santos XI
    if x['spec'] and re.search(r'\.(25|75)$',x['spec']): return False
    return x['sport'] in('football','basketball')
pool=[x for x in pk.OK if ok(x)]
def cost(x): return -math.log(x['p'])/math.log(x['odds'])
pool.sort(key=cost)
def country(x): return pk.country(x)
def side(x): return pk.side(x)
def build(target,cap=3,maxlegs=50):
    T=[];cc=collections.Counter();u=o=0;lo=0.0
    for x in pool:
        if lo>=math.log(target): break
        if any(y['eid']==x['eid'] for y in T) or cc[country(x)]>=cap: continue
        s=side(x)
        if s=='under' and (u+1)>0.4*max(len(T)+1,5): continue
        if s=='over' and (o+1)>0.4*max(len(T)+1,5): continue
        T.append(x);cc[country(x)]+=1;lo+=math.log(x['odds']);u+=s=='under';o+=s=='over'
    # trim: drop the costliest legs while the ticket still clears the target
    while True:
        od=math.prod(y['odds'] for y in T); c=[y for y in sorted(T,key=cost,reverse=True) if od/y['odds']>=target]
        if not c: break
        T.remove(c[0])
    return T
# ---------- Monte Carlo: N joint draws, every fixture simulated N times ----------
N=100000; rng=np.random.default_rng(20261103)
G_SD,C_SD,BK_SD=0.06,0.08,3.0   # shared goal-environment: day-wide and per-competition log-sd; basketball shared total shift (pts) per league-night
def settle(x,draw):
    m,sp,d=x['mid'],x['spec'],x['desc']
    if x['sport']=='football':
        h,a=draw; t=h+a; mg=h-a
        if m=='1': return np.where({'Home':mg>0,'Draw':mg==0,'Away':mg<0}[d],1,-1)
        if m=='11':
            w=(mg>0) if d=='Home' else (mg<0); return np.where(mg==0,0,np.where(w,1,-1))
        if m=='16':
            hc=float(sp.split('=')[1]); v=(mg+hc) if d.startswith('Home') else (-mg-hc); return np.sign(v)
        if m in('18','19','20'):
            ln=float(sp.split('=')[1]); val={'18':t,'19':h,'20':a}[m]
            v=(val-ln) if d.startswith('Over') else (ln-val); return np.sign(v)
        if m in('450001','450002','450003'):
            val={'450001':t,'450002':h,'450003':a}[m]; lo_,hi_=d.split('-'); lo_=int(lo_)
            if hi_.endswith('+'): w=val>=lo_
            else: w=(val>=lo_)&(val<=int(hi_))
            return np.where(w,1,-1)
    else:
        T,M=draw
        if m=='225':
            ln=float(sp.split('=')[1]); v=(T-ln) if d.startswith('Over') else (ln-T); return np.sign(v)
        if m=='223':
            hc=float(sp.split('=')[1]); v=(M+hc) if d.startswith('Home') else (-M-hc); return np.sign(v)
        if m=='219': return np.where((M>0) if d=='Home' else (M<0),1,-1)
    raise ValueError(x['mid'])
def simulate(T,corr=True):
    g=np.exp(rng.normal(0,G_SD,N)) if corr else np.ones(N)
    comp={};bkn={};res=[]
    for x in T:
        if x['sport']=='football':
            c=comp.setdefault(x['lg'],np.exp(rng.normal(0,C_SD,N)) if corr else np.ones(N))
            lh,la=x['lam']; h=rng.poisson(lh*g*c); a=rng.poisson(la*g*c); r=settle(x,(h,a))
        else:
            b=BASE[x['eid']]; muT,muM=x['mu']
            s=bkn.setdefault(x['lg'],rng.normal(0,BK_SD,N) if corr else np.zeros(N))
            Tt=rng.normal(muT,b['sdT'],N)+s; Mm=rng.normal(muM,b['sdM'],N); r=settle(x,(Tt,Mm))
        res.append(r)
    R=np.array(res)                        # legs x N : 1 win, 0 void, -1 loss
    alive=(R>=0).all(0); allwin=(R==1).all(0)
    odds=np.array([x['odds'] for x in T]); pay=np.where(R==1,odds[:,None],1.0).prod(0)
    return dict(per_leg=(R==1).mean(1),void=(R==0).mean(1),survive=alive.mean(),allwin=allwin.mean(),
                ev=(np.where(alive,pay,0)).mean(),med_pay=np.median(pay[alive]) if alive.any() else 0)
out={}
for tgt in (50,500):
    T=build(tgt,cap=3 if tgt<=50 else 5); od=math.prod(x['odds'] for x in T)
    s=simulate(T,True); si=simulate(T,False)
    out[tgt]=dict(legs=T,odds=od,sim=s,ind=si)
    print(f'\n=== T{tgt}: {len(T)} legs, {od:.1f}x | simulated (correlated) survive {s["survive"]:.5f} = 1 in {1/s["survive"]:.0f}; all-win {s["allwin"]:.5f}; independent-only survive {si["survive"]:.5f} (1 in {1/si["survive"]:.0f}); EV per unit {s["ev"]:.3f}')
    for x,pl,vd in zip(T,s['per_leg'],s['void']):
        print(f"  {x['ko']} {x['lg'][:30]:30} {x['fx'][:42]:42} {x['mdesc'][:24]:24} {x['desc'][:16]:16} @{x['odds']:.2f} model{x['p']:.3f} sim{pl:.3f} void{vd:.3f} house{0.95/x['odds']:.2f}")
json.dump({k:dict(legs=[{kk:x[kk] for kk in('eid','sid','fx','lg','ko','mid','spec','desc','oid','odds','p','mdesc')} for x in v['legs']],odds=v['odds'],surv=v['sim']['survive'],allwin=v['sim']['allwin'],ind=v['ind']['survive'],ev=v['sim']['ev'],per=list(map(float,v['sim']['per_leg'])),void=list(map(float,v['sim']['void']))) for k,v in out.items()},open('/tmp/claude-0/-home-user-gsley/b526d9c8-57a7-5192-8f65-9a58ec7e9e11/scratchpad/sim03_out.json','w'),indent=1)
