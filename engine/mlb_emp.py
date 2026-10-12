# Empirical MLB pricing anchored on closing lines: logistic models fitted on history.
#  totals:  P(total > ou+k)          = sigmoid(a_k + b_k*(ou-8.5))
#  margins: P(fav_margin + k > 0)    = sigmoid(a_k + b_k*logit(p_fav))   (k = handicap given to fav, e.g. -1.5, +1.5)
import json,math,numpy as np
from scipy.optimize import minimize
def ml2p(m): return 100/(m+100) if m>0 else -m/(-m+100)
lg=lambda p:math.log(p/(1-p)); sg=lambda z:1/(1+math.exp(-z))
def fitlog(x,y):
    x=np.array(x);y=np.array(y,float)
    f=lambda w:-np.sum(y*np.log(1/(1+np.exp(-(w[0]+w[1]*x)))+1e-12)+(1-y)*np.log(1-1/(1+np.exp(-(w[0]+w[1]*x)))+1e-12))
    return list(minimize(f,[0,1],method='Nelder-Mead').x)
KT=[-3.5,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3.5]; KM=[-4.5,-3.5,-2.5,-1.5,-0.5,0.5,1.5,2.5,3.5,4.5]
def rows(R):
    for r in R:
        ph=ml2p(r['hml']);pa=ml2p(r['aml']);ph=ph/(ph+pa); fav=1 if ph>=0.5 else -1
        yield r,ph,max(ph,1-ph),fav
def fit(R):
    C={'T':{},'M':{}}
    for k in KT:
        X=[];Y=[]
        for r,ph,pf,fav in rows(R):
            L=r['ou']+k; t=r['hs']+r['as_']
            if t==L: continue
            X.append(r['ou']-8.5); Y.append(t>L)
        C['T'][str(k)]=fitlog(X,Y)
    for k in KM:
        X=[];Y=[]
        for r,ph,pf,fav in rows(R): X.append(lg(pf)); Y.append(fav*(r['hs']-r['as_'])+k>0)
        C['M'][str(k)]=fitlog(X,Y)
    return C
def p_total_over(C,ou,line):
    k=line-ou; ks=sorted(float(x) for x in C['T'])
    if k<ks[0] or k>ks[-1]: return None
    # interpolate in logit space between nearest fitted offsets
    lo=max(x for x in ks if x<=k); hi=min(x for x in ks if x>=k)
    TT={float(x):w for x,w in C['T'].items()}
    z=lambda kk:TT[kk][0]+TT[kk][1]*(ou-8.5)
    zz=z(lo) if lo==hi else z(lo)+(z(hi)-z(lo))*(k-lo)/(hi-lo)
    return sg(zz)
def p_fav_cover(C,pfav,k):
    MM={float(x):w for x,w in C['M'].items()}
    if float(k) not in MM: return None
    a,b=MM[float(k)]; return sg(a+b*lg(pfav))
if __name__=='__main__':
    import collections
    R=sorted([json.loads(l) for l in open('data/espn_mlb.jsonl')],key=lambda r:r['date'])
    R=[r for r in R if r['ou'] and r['hml'] and r['aml']]
    tr=[r for r in R if r['date']<'2026-01-01']; te=[r for r in R if r['date']>='2026-01-01']
    C=fit(tr); B=collections.defaultdict(lambda:[0,0,0.0])
    for r,ph,pf,fav in rows(te):
        t=r['hs']+r['as_']
        for k in [-1.5,-0.5,0.5,1.5]:
            p=p_total_over(C,r['ou'],r['ou']+k); b=B[('T%+.1f'%k,round(p*20)/20)]; b[0]+=1; b[1]+=t>r['ou']+k; b[2]+=p
        for k in [-2.5,-1.5,1.5,2.5,3.5]:
            p=p_fav_cover(C,pf,k); b=B[('F%+.1f'%k,round(p*20)/20)]; b[0]+=1; b[1]+=fav*(r['hs']-r['as_'])+k>0; b[2]+=p
    for key in sorted(set(k for k,_ in B)):
        print(key,' '.join(f'{v[2]/v[0]:.2f}->{v[1]/v[0]:.2f}(n{v[0]})' for (kk,b),v in sorted(B.items()) if kk==key and v[0]>=60))
    json.dump(fit(R),open('coef_mlb_emp.json','w'))
