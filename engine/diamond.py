# Baseball engine: home/away runs ~ independent negative binomials anchored to the market (total line + moneyline).
# Extra innings: a 9-inning tie is resolved by a one-inning-at-a-time sim (both teams' per-inning scoring ~ mean/9, home bats last).
import numpy as np, math
from scipy.stats import nbinom
K=31
def pmf(mu,r): p=r/(r+mu); return nbinom.pmf(np.arange(K),r,p)
def extra(mh,ma,r):
    """distribution over (margin delta, total delta) from extra innings with Manfred runner (~+0.45 runs/half-inning)"""
    ih=pmf(mh/9+0.45,r/9*3); ia=pmf(ma/9+0.45,r/9*3)
    out={}; tie=1.0
    for inn in range(6):
        for a in range(8):
            for h in range(8):
                pr=tie*ia[a]*ih[h]
                if h>a: k=(1,a+min(h,a+1))      # walk-off: home stops at a+1... approximated by margin 1
                elif h<a: k=(h-a,a+h)
                else: continue
                out[k]=out.get(k,0)+pr
        tie*=sum(ia[x]*ih[x] for x in range(8))
    return out
def joint(mh,ma,r):
    """dict (home_runs, away_runs) -> prob, final (incl. extras)"""
    ph=pmf(mh,r); pa=pmf(ma,r); J=np.outer(ph,pa)
    E=extra(mh,ma,r); out={}
    for h in range(K):
        for a in range(K):
            if h!=a: out[(h,a)]=J[h,a]; continue
            for (dm,dt),p in E.items():
                hh=h+(dt+dm)//2; aa=a+(dt-dm)//2
                out[(hh,aa)]=out.get((hh,aa),0)+J[h,a]*p
    return out
def anchor(total_mean,p_home,r):
    """find (mh,ma) with mh+ma=total_mean and P(home win)=p_home"""
    lo,hi=0.05,0.95
    for _ in range(30):
        s=(lo+hi)/2; J=joint(total_mean*s,total_mean*(1-s),r)
        ph=sum(p for (h,a),p in J.items() if h>a)
        lo,hi=(s,hi) if ph<p_home else (lo,s)
    return total_mean*s,total_mean*(1-s)
