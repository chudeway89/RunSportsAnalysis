# Live pricing of SportyBet corners/cards markets with the calibrated count models (paper-trade engine)
import json,math,re,difflib,collections,datetime as dt,sys
from counts import load_counts,fit,mean
from anc import fit as afit,devig,L as LAM
from scipy.stats import nbinom
import factor_adjust as FA
def norm(s):
    s=s.lower(); s=re.sub(r'\b(fc|cf|sc|ac|afc|cd|ca|sv|fk|if|bk|club|de|the|cp|ud|sd|ssc|as|rc|vfl|vfb|tsg|1\.|sk|nk|calcio|sad|real)\b','',s)
    return re.sub(r'[^a-z]','',s)
CO=json.load(open('coef_corners.json')); CA=json.load(open('coef_cards.json'))
import os; _cwd=os.getcwd(); os.chdir('fdcsv'); R=load_counts(); os.chdir(_cwd); by=collections.defaultdict(list)
for r in R: by[r['lg']].append(r)
now=dt.datetime.utcnow()
MC={lg:fit(ms,now,'hc','ac',half=365,prior=30) for lg,ms in by.items() if len(ms)>200}
MY={lg:fit([m for m in ms if m['hy'] is not None],now,'hy','ay',half=365,prior=30) for lg,ms in by.items() if len(ms)>200}
BASE={lg:(sum(m['hc']+m['ac'] for m in ms[-400:])/len(ms[-400:]), sum((m['hy'] or 0)+(m['ay'] or 0) for m in ms[-400:])/len(ms[-400:])) for lg,ms in by.items()}
teams={lg:set(M['F']) for lg,M in MC.items()}
def match(lg,name):
    best=max(teams.get(lg,[]),key=lambda t:difflib.SequenceMatcher(None,norm(name),norm(t)).ratio(),default=None)
    return best if best and difflib.SequenceMatcher(None,norm(name),norm(best)).ratio()>=0.6 else None
def nb_gt(mu,r,line): p=r/(r+mu); return 1-nbinom.cdf(math.floor(line),r,p)
def nb_eq(mu,r,k): p=r/(r+mu); return nbinom.pmf(k,r,p)
out=[]
MAP={('England','Premier League'):'E0',('England','Championship'):'E1',('England','League One'):'E2',('England','League Two'):'E3',
 ('Scotland','Premiership'):'SC0',('Scotland','Championship'):'SC1',('Scotland','League 1'):'SC2',('Scotland','League 2'):'SC3',
 ('Germany','Bundesliga'):'D1',('Germany','2. Bundesliga'):'D2',('Italy','Serie A'):'I1',('Italy','Serie B'):'I2',
 ('Spain','LaLiga'):'SP1',('Spain','LaLiga 2'):'SP2',('France','Ligue 1'):'F1',('France','Ligue 2'):'F2',
 ('Netherlands','Eredivisie'):'N1',('Belgium','Pro League'):'B1',('Portugal','Liga Portugal'):'P1',('Turkiye','Super Lig'):'T1',('Greece','Super League'):'G1'}
for e in json.load(open(sys.argv[1])):
    if e['sport']!='football': continue
    lg=MAP.get(tuple((e['lg'].split(' / ')+[''])[:2]))
    if not lg: continue
    e['home'],e['away']=e['fx'].split(' v ',1)
    if lg not in MC: continue
    h=match(lg,e['home']); a=match(lg,e['away'])
    if not h or not a or h==a: continue
    g=lambda mid,spec,desc:[o['odds'] for o in e['mk'] if o['mid']==mid and (o['spec'] or None)==spec and o['desc']==desc]
    H,D,A=g('1',None,'Home'),g('1',None,'Draw'),g('1',None,'Away'); O,U=g('18','total=2.5','Over 2.5'),g('18','total=2.5','Under 2.5')
    if not(H and D and A and O and U): continue
    pH,pD,pA=devig(H[0],D[0],A[0]); pO=devig(O[0],U[0])[0]; i,j=afit(pH,pD,pA,pO); lh,la=LAM[i],LAM[j]
    ch,ca=mean(MC[lg],h,a); yh,ya=mean(MY[lg],h,a)
    b=CO['beta']; muC=b[0]+b[1]*(0.5*(ch+ca)+0.5*BASE[lg][0])+b[2]*BASE[lg][0]+b[3]*(lh+la)+b[4]*abs(lh-la)
    b=CA['beta']; muY=b[0]+b[1]*(yh+ya)+b[2]*BASE[lg][1]+b[3]*(lh+la)+b[4]*abs(lh-la)
    shC=ch/(ch+ca); rC=CO['r']; rY=CA['r']
    # factor study (FACTORS.md): table position / form / fouls for cards, goals-form & rank for corners
    fh,fa=FA.mult(lg,h,a,True),FA.mult(lg,a,h,False); shY=yh/(yh+ya) if yh+ya else 0.5
    muC0,muY0=muC,muY; muC=muC*(shC*fh['y_c']+(1-shC)*fa['y_c']); muY=muY*(shY*fh['y_y']+(1-shY)*fa['y_y'])
    shC=shC*fh['y_c']/(shC*fh['y_c']+(1-shC)*fa['y_c'])
    for o in e['mk']:
        m,s,d=o['mid'],o['spec'] or '',o['desc']; p=None
        try:
            if m=='166' and s.startswith('total='):
                t=float(s[6:]); pg=nb_gt(muC,rC,t); p=pg if d.startswith('Over') else 1-pg-(nb_eq(muC,rC,int(t)) if t==int(t) else 0)
            elif m in('900300','900301') and s.startswith('total='):
                mu=muC*(shC if m=='900300' else 1-shC); t=float(s[6:]); pg=nb_gt(mu,rC*(mu/muC),t)
                p=pg if d.startswith('Over') else 1-pg
            elif m=='139' and s.startswith('total='):
                t=float(s[6:]); pg=nb_gt(muY+0.15,rY,t); p=pg if d.startswith('Over') else 1-pg
            elif m=='800063' and d.endswith('+'):
                k=int(d[:-1]); p=nb_gt(muY+0.15,rY,k-0.5)
        except Exception: p=None
        if p is None: continue
        out.append(dict(sport='football',src='fd-regression',line=None,eid=e['eid'],sid=e['sid'],fx=e['home']+' v '+e['away'],fdh=h,fda=a,lg=lg,ko=e['ko'],mid=m,spec=o['spec'],desc=d,mdesc=o['mdesc'],oid=o['oid'],
           odds=o['odds'],hp=o['p'],mp=p,ev=p*o['odds'],muC=round(muC,2),muY=round(muY,2),muC0=round(muC0,2),muY0=round(muY0,2)))
json.dump(out,open('cache/priced_fd_counts.json','w'))
print('priced outcomes',len(out),'fixtures',len(set(x['eid'] for x in out)))
cand=[x for x in out if 1.30<=x['odds']<=2.6]
cand.sort(key=lambda x:-x['ev'])
for x in cand[:40]: print(f"EV {x['ev']:.3f} model {x['mp']:.2f} house {x['hp']:.2f} {x['ko']} {x['lg']:<4} {x['fx'][:38]:<38} {x['mdesc'][:24]:<24} {x['spec'] or '':<11} {x['desc']:<10} @{x['odds']}  muC {x['muC']} muY {x['muY']}")
import statistics
for mid in ['166','900300','900301','139','800063']:
    v=[x['ev'] for x in out if x['mid']==mid and 1.3<=x['odds']<=2.6]
    if v: print(mid,'n',len(v),'mean EV %.3f'%statistics.mean(v),'share EV>=1.05: %.2f'%(sum(e>=1.05 for e in v)/len(v)))
