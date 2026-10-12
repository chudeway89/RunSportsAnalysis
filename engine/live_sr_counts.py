# Live corners/cards pricing for football leagues WITHOUT football-data coverage (South America, Asia, MLS, Scandinavia...)
# using Sportradar match history (sr_football.py) and the team-blend model validated in bt_sr_counts.py.
# Usage: python3 live_sr_counts.py cache/board_<date>.json -> cache/priced_sr_counts.json
import json,sys,math,collections,datetime as dt
from scipy.stats import nbinom
import sr
from counts import fit,mean
FD={('England','Premier League'),('England','Championship'),('England','League One'),('England','League Two'),('Scotland','Premiership'),('Scotland','Championship'),
 ('Scotland','League 1'),('Scotland','League 2'),('Germany','Bundesliga'),('Germany','2. Bundesliga'),('Italy','Serie A'),('Italy','Serie B'),('Spain','LaLiga'),('Spain','LaLiga 2'),
 ('France','Ligue 1'),('France','Ligue 2'),('Netherlands','Eredivisie'),('Belgium','Pro League'),('Portugal','Liga Portugal'),('Turkiye','Super Lig'),('Greece','Super League')}
CC=json.load(open('coef_sr_corners.json')); CY=json.load(open('coef_sr_cards.json')); RC=CC['r']
BIAS_C=0.3   # out-of-sample mean residual (bt_sr_counts.py, Oct 12: model under-predicts corners ~0.3)
H=[json.loads(l) for l in open('data/sr_fb_counts.jsonl')]
by=collections.defaultdict(list)
for r in H: r['date']=dt.datetime.fromisoformat(r['date']); by[r['lg']].append(r)
now=dt.datetime.utcnow(); MOD={}
def model(lg):
    if lg not in MOD:
        ms=[m for m in by.get(lg,[]) if (now-m['date']).days<450]
        if len(ms)<80: MOD[lg]=None
        else:
            C=fit(ms,now,'hc','ac',half=365,prior=30); Y=fit([m for m in ms if m['hy'] is not None],now,'hy','ay',half=365,prior=30)
            G=fit(ms,now,'hg','ag',half=365,prior=15)
            MOD[lg]=(C,Y,sum(m['hc']+m['ac'] for m in ms)/len(ms),sum((m['hy'] or 0)+(m['ay'] or 0) for m in ms)/len(ms),len(ms),G,sum(m['hg']+m['ag'] for m in ms)/len(ms))
    return MOD[lg]
def gt(mu,r,line): p=r/(r+mu); return 1-nbinom.cdf(math.floor(line),r,p)
out=[]
for e in json.load(open(sys.argv[1])):
    if e['sport']!='football' or not any(o['mid'] in ('166','139','900300','900301') for o in e['mk']): continue
    cat,tour=(e['lg'].split(' / ')+[''])[:2]
    if (cat,tour) in FD: continue
    m=sr.match_info(e['eid'].split(':')[-1])
    if not m: continue
    M=model('sr%d'%m['_utid'])
    if not M: continue
    C,Y,bc,by_,n,G,gb=M; h,a=str(m['teams']['home']['uid']),str(m['teams']['away']['uid'])
    if h not in C['F'] or a not in C['F']: continue
    ch,ca=mean(C,h,a); sh=ch/(ch+ca); gh,ga=mean(G,h,a); yh,ya=mean(Y,h,a)
    b=CC['beta']; muC=b[0]+b[1]*(ch+ca)+b[2]*bc+b[3]*(gh+ga-gb)+b[4]*abs(gh-ga)+BIAS_C
    b=CY['beta']; muY=b[0]+b[1]*(yh+ya)+b[2]*by_+b[3]*(gh+ga-gb)+b[4]*abs(gh-ga)
    for o in e['mk']:
        mid,s,d=o['mid'],o['spec'] or '',o['desc']; p=None
        try:
            t=float(s.split('=')[1]) if s.startswith('total=') else None
            if mid=='166' and t is not None:
                pg=gt(muC,RC,t); pe=nbinom.pmf(int(t),RC,RC/(RC+muC)) if t==int(t) else 0
                p=pg if d.startswith('Over') else 1-pg-pe
            elif mid in ('900300','900301') and t is not None:
                mu=muC*(sh if mid=='900300' else 1-sh); pg=gt(mu,RC*mu/muC,t); p=pg if d.startswith('Over') else 1-pg
            elif mid=='139' and t is not None:
                pg=1-__import__('scipy.stats',fromlist=['poisson']).poisson.cdf(math.floor(t),muY+0.15); p=pg if d.startswith('Over') else 1-pg
        except Exception: p=None
        if p is None: continue
        out.append(dict(eid=e['eid'],sid=e['sid'],sport='football',lg=e['lg'],fx=e['fx'],ko=e['ko'],mid=mid,spec=o['spec'],desc=d,oid=o['oid'],odds=o['odds'],
                        hp=o['p'],mp=p,ev=p*o['odds'],src='sr-regression n%d'%n,line=t,muC=round(muC,2),muY=round(muY,2)))
json.dump(out,open('cache/priced_sr_counts.json','w'))
print('priced',len(out),'outcomes on',len(set(x['eid'] for x in out)),'events; leagues',sorted(set(x['lg'] for x in out)))
for mid in ('166','900300','900301','139'):
    v=[x['ev'] for x in out if x['mid']==mid and 1.2<=x['odds']<=3]
    if v: print(mid,'n',len(v),'mean EV %.3f'%(sum(v)/len(v)))
