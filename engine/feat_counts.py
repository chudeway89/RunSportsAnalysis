from counts import *
from load import load
from anc import fit as afit, devig, L as LAM
import numpy as np, sys
stat=sys.argv[1]; kh,ka=('hc','ac') if stat=='corners' else ('hy','ay')
lines=[8.5,9.5,10.5] if stat=='corners' else [3.5,4.5]
odds={(r['lg'],r['date'],r['h'],r['a']):r for r in load()}
R=[r for r in load_counts() if r[kh] is not None and r[ka] is not None]
by=collections.defaultdict(list)
for r in R: by[r['lg']].append(r)
X=[];Y=[];D=[]
for lg,ms in by.items():
    ms.sort(key=lambda m:m['date']); t=dt.datetime(2025,3,1)
    while t<dt.datetime(2026,10,10):
        tr=[m for m in ms if t-dt.timedelta(days=500)<=m['date']<t]; te=[m for m in ms if t<=m['date']<t+dt.timedelta(days=28)]
        if len(tr)>150 and te:
            M=fit(tr,t,kh,ka,half=365,prior=30); base=sum(m[kh]+m[ka] for m in tr)/len(tr)
            for m in te:
                o=odds.get((m['lg'],m['date'],m['h'],m['a']))
                if not o or not o['oh'] or not o['o25'] or not o['u25']: continue
                pH,pD,pA=devig(o['oh'],o['od'],o['oa']); pO=devig(o['o25'],o['u25'])[0]
                i,j=afit(pH,pD,pA,pO); lh,la=LAM[i],LAM[j]
                h,a=mean(M,m['h'],m['a'])
                X.append([1,h+a,base,lh+la,abs(lh-la),(h+a)*0+ (stat=='cards' and 0 or 0)]); Y.append(m[kh]+m[ka]); D.append(m['date'])
        t+=dt.timedelta(days=28)
X=np.array(X,float)[:,:5]; Y=np.array(Y,float); D=np.array(D)
cut=dt.datetime(2026,1,1); tr=D<cut; te=~tr
beta=np.linalg.lstsq(X[tr],Y[tr],rcond=None)[0]
print('coef [const, teamMu, leagueAvg, mktGoals, |supremacy|]:',np.round(beta,3))
mu_reg=X[te]@beta; mu_team=0.5*X[te,1]+0.5*X[te,2]; mu_base=X[te,2]
res=Y[tr]-X[tr]@beta; var=res.var(); mbar=(X[tr]@beta).mean(); r=max(mbar**2/max(var-mbar,1e-6),1)
print('test n',te.sum(),'NB size',round(r,1))
clip=lambda q:min(max(q,1e-6),1-1e-6)
for name,mu in [('league avg',mu_base),('team blend',mu_team),('team+market regression',mu_reg)]:
    ll=0;n=0
    for m_,y in zip(mu,Y[te]):
        for Lx in lines:
            p=p_over(m_,r,Lx); ll+=-math.log(clip(p) if y>Lx else clip(1-p)); n+=1
    print(f'{name:<24} logloss {ll/n:.4f}')
# calibration of regression model
for Lx in lines:
    b=collections.defaultdict(lambda:[0,0])
    for m_,y in zip(mu_reg,Y[te]):
        p=p_over(m_,r,Lx); k=round(p*20)/20; b[k][0]+=1; b[k][1]+=y>Lx
    print(f'Over {Lx}:',' '.join(f'{k:.2f}->{v[1]/v[0]:.2f}(n{v[0]})' for k,v in sorted(b.items()) if v[0]>=80))
import json; json.dump(dict(beta=list(beta),r=r),open(f'coef_{stat}.json','w'))
