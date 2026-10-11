# walk-forward: for each league, every 2 weeks refit on prior 400 days, predict next 14 days; compare to avg closing
from model import *
R=load(); by=collections.defaultdict(list)
for r in R: by[r['lg']].append(r)
recs=[]
start=dt.datetime(2025,1,1); end=dt.datetime(2026,10,10)
for lg,ms in by.items():
    ms.sort(key=lambda m:m['date']); t=start
    while t<end:
        train=[m for m in ms if t-dt.timedelta(days=400)<=m['date']<t]
        test=[m for m in ms if t<=m['date']<t+dt.timedelta(days=14)]
        if len(train)>150 and test:
            M=fit(train,t)
            for m in test:
                if m['h'] not in M['att'] or m['a'] not in M['att']: continue
                P,_,_=probs(M,m['h'],m['a']); recs.append((lg,m,mk(P)))
        t+=dt.timedelta(days=14)
print('predictions',len(recs))
import json
def ll(p,y): p=min(max(p,1e-6),1-1e-6); return -(math.log(p) if y else math.log(1-p))
# O2.5 vs market
for name,fn,odd,oddn in [('O2.5',lambda m:m['hg']+m['ag']>2,'o25','u25'),('HomeWin',lambda m:m['hg']>m['ag'],'oh',None)]:
    lm=lmk=lb=n=0
    for lg,m,p in recs:
        o=m[odd]
        if not o: continue
        if oddn and m[oddn]: q=(1/o)/((1/o)+(1/m[oddn]))
        elif odd=='oh' and m['od'] and m['oa']: q=(1/o)/(1/o+1/m['od']+1/m['oa'])
        else: continue
        y=fn(m); pm=p['O25'] if name=='O2.5' else p['H']
        lm+=ll(pm,y); lmk+=ll(q,y); lb+=ll(0.5*pm+0.5*q,y); n+=1
    print(f'{name}: n={n} logloss model {lm/n:.4f} market {lmk/n:.4f} blend {lb/n:.4f}')
# value-betting ROI at avg closing when model edge > thr
for thr in [0.0,0.03,0.06,0.10]:
  for name in ['O25','U25','H','A']:
    s=[]
    for lg,m,p in recs:
        if name in('O25','U25'):
            o=m['o25'] if name=='O25' else m['u25']
            if not o: continue
            pm=p['O25'] if name=='O25' else 1-p['O25']; y=(m['hg']+m['ag']>2)==(name=='O25')
        else:
            o=m['oh'] if name=='H' else m['oa']
            if not o: continue
            pm=p[name]; y=(m['hg']>m['ag']) if name=='H' else (m['ag']>m['hg'])
        if pm*o-1>thr: s.append(o if y else 0)
    if s: print(f'edge>{thr:.2f} {name}: bets {len(s)} ROI {sum(s)/len(s)-1:+.3f}')
# calibration of model for O1.5 / U3.5 / U4.5
for key,f in [('O15',lambda m:m['hg']+m['ag']>=2),('U35',lambda m:m['hg']+m['ag']<=3),('U45',lambda m:m['hg']+m['ag']<=4)]:
    b=collections.defaultdict(lambda:[0,0,0.0])
    for lg,m,p in recs:
        k=round(p[key]*20)/20; b[k][0]+=1; b[k][1]+=f(m); b[k][2]+=p[key]
    print(key,' '.join(f'{k:.2f}:{v[1]/v[0]:.2f}(n{v[0]})' for k,v in sorted(b.items()) if v[0]>80))
json.dump([(lg,str(m['date'].date()),m['h'],m['a'],m['hg'],m['ag'],p) for lg,m,p in recs],open('bt.json','w'))
