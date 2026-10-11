from load import load
from anc import *
import collections
R=[r for r in load() if r['oh'] and r['od'] and r['oa'] and r['o25'] and r['u25'] and r['date'].year>=2025]
cal={k:collections.defaultdict(lambda:[0,0]) for k in ['O15','U35','U45','TTH05','TTA05','AH+1.5dog']}
I=np.arange(K)[:,None]; Jx=np.arange(K)[None,:]
for r in R:
    pH,pD,pA=devig(r['oh'],r['od'],r['oa']); pO,_=devig(r['o25'],r['u25'])
    P=grid(*fit(pH,pD,pA,pO)); t=r['hg']+r['ag']
    dog='a' if pH>pA else 'h'
    pdog=(P*((Jx-I)>-2)).sum() if dog=='a' else (P*((I-Jx)>-2)).sum()
    ydog=(r['ag']-r['hg']>-2) if dog=='a' else (r['hg']-r['ag']>-2)
    for k,p,y in [('O15',(P*((I+Jx)>=2)).sum(),t>=2),('U35',(P*((I+Jx)<=3)).sum(),t<=3),('U45',(P*((I+Jx)<=4)).sum(),t<=4),
                  ('TTH05',(P*(I>=1)).sum(),r['hg']>=1),('TTA05',(P*(Jx>=1)).sum(),r['ag']>=1),('AH+1.5dog',pdog,ydog)]:
        b=cal[k][round(float(p)*20)/20]; b[0]+=1; b[1]+=y
print(len(R))
for k,v in cal.items(): print(k,' '.join(f'{a:.2f}:{c[1]/c[0]:.2f}(n{c[0]})' for a,c in sorted(v.items()) if c[0]>=80))
