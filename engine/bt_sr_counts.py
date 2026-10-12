# Walk-forward backtest of corners/cards count models on Sportradar history (all board leagues incl. S.America/Asia).
# No historical odds there, so the model is team strengths + league mean (+ team goal strengths as a goals proxy).
# Usage: python3 bt_sr_counts.py corners|cards  -> prints log-loss vs league-average baseline + calibration; saves coef_sr_<stat>.json
import json,sys,math,collections,datetime as dt
import numpy as np
from counts import fit,mean,p_over
stat=sys.argv[1]; kh,ka=('hc','ac') if stat=='corners' else ('hy','ay')
lines=[7.5,8.5,9.5,10.5,11.5] if stat=='corners' else [2.5,3.5,4.5,5.5]
R=[json.loads(l) for l in open('data/sr_fb_counts.jsonl')]
for r in R: r['date']=dt.datetime.fromisoformat(r['date'])
R=[r for r in R if r[kh] is not None and r[ka] is not None]
by=collections.defaultdict(list)
for r in R: by[r['lg']].append(r)
X=[];Y=[];D=[];LG=[]
for lg,ms in by.items():
    ms.sort(key=lambda m:m['date'])
    if len(ms)<120: continue
    t=ms[80]['date']
    while t<=ms[-1]['date']:
        tr=[m for m in ms if t-dt.timedelta(days=450)<=m['date']<t]; te=[m for m in ms if t<=m['date']<t+dt.timedelta(days=14)]
        if len(tr)>=80 and te:
            M=fit(tr,t,kh,ka,half=365,prior=30); G=fit(tr,t,'hg','ag',half=365,prior=15)
            base=sum(m[kh]+m[ka] for m in tr)/len(tr); gb=sum(m['hg']+m['ag'] for m in tr)/len(tr)
            for m in te:
                h,a=mean(M,m['h'],m['a']); gh,ga=mean(G,m['h'],m['a'])
                X.append([1,h+a,base,gh+ga-gb,abs(gh-ga)]); Y.append(m[kh]+m[ka]); D.append(m['date']); LG.append(lg)
        t+=dt.timedelta(days=14)
X=np.array(X,float);Y=np.array(Y,float);D=np.array(D)
order=np.argsort(D); half=D[order[len(D)//2]]; tr=D<half; te=~tr
beta=np.linalg.lstsq(X[tr],Y[tr],rcond=None)[0]
res=Y[tr]-X[tr]@beta; var=res.var(); mb=(X[tr]@beta).mean(); r=max(mb**2/max(var-mb,1e-6),1)
print(stat,'leagues',len(set(LG)),'predictions',len(Y),'train/test',tr.sum(),te.sum())
print('coef [const, teamMu, leagueAvg, goalsAboveAvg, |goalSup|]:',np.round(beta,3),' NB size',round(r,1))
clip=lambda q:min(max(q,1e-6),1-1e-6)
mu_reg=X[te]@beta
for name,mu in [('league avg',X[te,2]),('team blend',0.5*X[te,1]+0.5*X[te,2]),('regression',mu_reg)]:
    ll=n=0
    for m_,y in zip(mu,Y[te]):
        for L in lines: p=p_over(m_,r,L); ll+=-math.log(clip(p) if y>L else clip(1-p)); n+=1
    print(f'  {name:<12} logloss {ll/n:.4f}')
for L in lines:
    b=collections.defaultdict(lambda:[0,0])
    for m_,y in zip(mu_reg,Y[te]): p=p_over(m_,r,L); k=round(p*10)/10; b[k][0]+=1; b[k][1]+=y>L
    print(f'  Over {L}:',' '.join(f'{k:.1f}->{v[1]/v[0]:.2f}(n{v[0]})' for k,v in sorted(b.items()) if v[0]>=40))
reg=collections.defaultdict(list)
for lg,m_,y in zip(np.array(LG)[te],mu_reg,Y[te]): reg[lg].append(y-m_)
print('  per-league mean residual (actual-model):',{k:round(float(np.mean(v)),2) for k,v in reg.items() if len(v)>=30})
json.dump(dict(beta=list(beta),r=r),open(f'coef_sr_{stat}.json','w'))
