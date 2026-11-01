# FACTOR STUDY part 2: other markets and other sports.  Same test as factors.py: for each factor, does it move the
# outcome beyond what the price already says, and does that hold out of sample (train < 2025-07-01, test after)?
#  A. Football (football-data, closing prices): total goals, 1st-half goals, BTTS, draw, home win, total corners, cards
#     with match-context factors: rest/congestion, promoted sides, season stage, referee goal/home-win record,
#     table gap, relegation/title clashes, midweek, month, H2H draw rate.
#  B. NBA / WNBA / MLB (ESPN closing lines): back-to-backs, rest, road trips, streaks, season stage, scoring form.
#  C. Basketball + baseball on SportyBet's OWN lines (our tape: Europe/Asia/LatAm leagues), results from Sportradar.
# Output: appended section in ../papertrade/FACTORS.md (between markers) + cache/factor2_results.json
import json,math,glob,gzip,csv,collections,datetime as dt,numpy as np
from scipy.stats import norm
from scipy.special import gammaln
import factors as F
CUT=dt.datetime(2025,7,1)
def fit(kind,X,y,off,it=40):
    b=np.zeros(X.shape[1])
    for _ in range(it):
        eta=np.clip(off+X@b,-15,15)
        if kind=='pois': mu=np.exp(eta); W=mu; g=y-mu
        elif kind=='logit': mu=1/(1+np.exp(-eta)); W=mu*(1-mu)+1e-9; g=y-mu
        else: mu=eta; W=np.ones_like(y); g=y-mu
        A=X.T@(X*W[:,None])+1e-6*np.eye(X.shape[1]); d=np.linalg.solve(A,X.T@g); b=b+d
        if np.max(abs(d))<1e-9: break
    eta=off+X@b
    mu=np.exp(eta) if kind=='pois' else 1/(1+np.exp(-eta)) if kind=='logit' else eta
    W=mu if kind=='pois' else mu*(1-mu) if kind=='logit' else np.ones_like(y)
    cov=np.linalg.inv(X.T@(X*W[:,None])+1e-6*np.eye(X.shape[1])); U=X*(y-mu)[:,None]; S=cov@(U.T@U)@cov
    return b,np.sqrt(np.diag(S))
def score(kind,X,y,off,b):
    eta=off+X@b
    if kind=='pois': mu=np.exp(eta); return float(np.mean(y*np.log(mu)-mu-gammaln(y+1)))
    if kind=='logit': p=np.clip(1/(1+np.exp(-eta)),1e-9,1-1e-9); return float(np.mean(y*np.log(p)+(1-y)*np.log(1-p)))
    return float(-np.mean((y-eta)**2))     # ols: negative MSE
def test(D,kind,target,base,feats,label):
    """D = list of dicts with 'date'. base(r)->(offset, [controls]). Each feature added alone on top of the base."""
    out=[]
    for fe,typ in feats:
        S=[r for r in D if r.get(fe) is not None and r.get(target) is not None]
        if len(S)<400: continue
        v=np.array([float(r[fe]) for r in S]); y=np.array([float(r[target]) for r in S])
        if typ=='z': z=(v-v.mean())/(v.std() or 1)
        else: z=v                                   # binary flag: effect of the flag being on
        if z.std()==0: continue
        B=[base(r) for r in S]; off=np.array([b[0] for b in B]); C=np.array([b[1] for b in B],float).reshape(len(S),-1)
        X0=np.c_[np.ones(len(S)),C]; X1=np.c_[X0,z]
        b1,se1=fit(kind,X1,y,off)
        tr=np.array([r['date']<CUT for r in S]); te=~tr; oos=None
        if tr.sum()>300 and te.sum()>150:
            b0t,_=fit(kind,X0[tr],y[tr],off[tr]); b1t,_=fit(kind,X1[tr],y[tr],off[tr])
            oos=score(kind,X1[te],y[te],off[te],b1t)-score(kind,X0[te],y[te],off[te],b0t)
            half=same=None
        # stability: sign in each half of the whole sample
        h=len(S)//2; idx=np.argsort([r['date'] for r in S]); e1,_=fit(kind,X1[idx[:h]],y[idx[:h]],off[idx[:h]]); e2,_=fit(kind,X1[idx[h:]],y[idx[h:]],off[idx[h:]])
        eff=(math.exp(b1[-1])-1)*100 if kind=='pois' else b1[-1] if kind=='ols' else b1[-1]
        out.append(dict(market=label,factor=fe,typ=typ,n=len(S),n_on=int((z>0).sum()) if typ=='b' else None,kind=kind,coef=float(b1[-1]),
                        t=float(b1[-1]/se1[-1]),early=float(e1[-1]),late=float(e2[-1]),oos=oos,eff=eff))
    return out
RES=[]
# ================= A. FOOTBALL =================
R=F.load(); rows=F.build(R)
teams=collections.defaultdict(set)
for r in R: teams[(r['lg'],r['season'])]|={r['h'],r['a']}
def prev(s): return f"{int(s[:2])-1:02d}{int(s[2:])-1:02d}"
refg=collections.defaultdict(list); refh=collections.defaultdict(list); h2hd=collections.defaultdict(list)
M=[]
for i,r in enumerate(R):
    H,A=rows[2*i],rows[2*i+1]
    nt=len(teams[(r['lg'],r['season'])]); g=2*(nt-1) if nt>2 else 38; frac=H['rnd']/g
    pv=teams.get((r['lg'],prev(r['season'])))
    pH,pD,pA=F.anc.devig(r['oh'],r['od'],r['oa']); lh,la=r['lh'],r['la']
    pbtts=(1-math.exp(-lh))*(1-math.exp(-la))
    rg=refg[r['ref']][-20:] if r['ref'] else []; rh=refh[r['ref']][-30:] if r['ref'] else []
    hk=frozenset((r['h'],r['a'])); hd=h2hd[hk][-6:]
    m=dict(date=r['date'],lg=r['lg'],lam=lh+la,lh=lh,la=la,pH=pH,pD=pD,pbtts=pbtts,
      y_tot=r['hg']+r['ag'],y_1h=(r['hthg']+r['htag']) if r['hthg'] is not None and r['htag'] is not None else None,
      y_btts=int(r['hg']>0 and r['ag']>0),y_draw=int(r['hg']==r['ag']),y_home=int(r['hg']>r['ag']),
      y_corn=(r['hc']+r['ac']) if r['hc'] is not None and r['ac'] is not None else None,
      y_card=(r['hy']+r['ay']) if r['hy'] is not None and r['ay'] is not None else None,
      rest_h=H['rest'],rest_a=A['rest'],
      cong_h=int(H['rest'] is not None and H['rest']<=3), cong_a=int(A['rest'] is not None and A['rest']<=3),
      rest_diff=(min(H['rest'],10)-min(A['rest'],10)) if H['rest'] and A['rest'] else None,
      early=int(H['rnd']<5), late=int(frac>=0.85), stage=frac,
      prom_h=int(pv is not None and r['h'] not in pv) if pv else None, prom_a=int(pv is not None and r['a'] not in pv) if pv else None,
      ref_g=sum(rg)/len(rg) if len(rg)>=10 else None, ref_hw=sum(rh)/len(rh) if len(rh)>=15 else None,
      gap=abs(H['rank']-A['rank']) if H['rank'] is not None and A['rank'] is not None else None,
      releg=int(H['rank'] is not None and A['rank'] is not None and H['rank']>=0.8 and A['rank']>=0.8 and frac>0.5),
      title=int(H['rank'] is not None and A['rank'] is not None and H['rank']<=0.15 and A['rank']<=0.15),
      late_bottom_h=int(H['rank'] is not None and H['rank']>=0.8 and frac>=0.75),
      mid=int(r['date'].weekday() in (1,2,3)), dec_jan=int(r['date'].month in (12,1)), aug_sep=int(r['date'].month in (8,9)),
      h2h_draw=sum(hd)/len(hd) if len(hd)>=3 else None,
      form_h=H['pts5'],form_a=A['pts5'],sot_sum=(H['sotf10']+A['sotf10']) if H['sotf10'] is not None and A['sotf10'] is not None else None)
    M.append(m)
    if r['ref']: refg[r['ref']].append(r['hg']+r['ag']); refh[r['ref']].append(int(r['hg']>r['ag']))
    h2hd[hk].append(int(r['hg']==r['ag']))
lgc=collections.defaultdict(list); lgy=collections.defaultdict(list)
for m in M:
    if m['date']<CUT:
        if m['y_corn'] is not None: lgc[m['lg']].append(m['y_corn'])
        if m['y_card'] is not None: lgy[m['lg']].append(m['y_card'])
lgc={k:sum(v)/len(v) for k,v in lgc.items()}; lgy={k:sum(v)/len(v) for k,v in lgy.items()}
lo=lambda p:math.log(min(max(p,1e-4),1-1e-4)/(1-min(max(p,1e-4),1-1e-4)))
FB=[('rest_diff','z'),('cong_h','b'),('cong_a','b'),('early','b'),('late','b'),('prom_h','b'),('prom_a','b'),('ref_g','z'),('ref_hw','z'),
    ('gap','z'),('releg','b'),('title','b'),('late_bottom_h','b'),('mid','b'),('dec_jan','b'),('aug_sep','b'),('h2h_draw','z'),('form_h','z'),('form_a','z'),('sot_sum','z')]
RES+=test(M,'pois','y_tot',lambda m:(math.log(m['lam']),[]),FB,'Total goals')
RES+=test(M,'pois','y_1h',lambda m:(math.log(m['lam']),[]),FB,'1st-half goals')
RES+=test(M,'logit','y_btts',lambda m:(lo(m['pbtts']),[]),FB,'BTTS (both teams score)')
RES+=test(M,'logit','y_draw',lambda m:(lo(m['pD']),[]),FB,'Draw')
RES+=test(M,'logit','y_home',lambda m:(lo(m['pH']),[]),FB,'Home win')
RES+=test(M,'pois','y_corn',lambda m:(math.log(lgc.get(m['lg'],10)),[math.log(m['lam']),abs(math.log(m['lh']/m['la']))]),FB,'Total corners')
RES+=test(M,'pois','y_card',lambda m:(math.log(lgy.get(m['lg'],4)),[math.log(m['lam']),abs(math.log(m['lh']/m['la']))]),FB,'Total yellow cards')
# ================= B. US SPORTS (ESPN closing lines) =================
def ml2p(h,a):
    f=lambda m:100/(m+100) if m>0 else -m/(-m+100)
    ph,pa=f(h),f(a); return ph/(ph+pa)
for sport in ('nba','wnba','mlb'):
    G=[json.loads(l) for l in open(f'data/espn_{sport}.jsonl')]
    G=[g for g in G if g.get('ou') and g.get('hs') is not None and g.get('season_type')!='preseason']
    G.sort(key=lambda g:g['date']); H=collections.defaultdict(list); D=[]
    gl=[]                                   # league running scoring for relative form
    for g in G:
        d=dt.date.fromisoformat(g['date']); x=dict(date=dt.datetime.combine(d,dt.time()))
        for s,t in (('h',g['h']),('a',g['a'])):
            L=H[t]; last=L[-1] if L else None
            x[s+'_rest']=(d-last['d']).days if last else None
            x[s+'_b2b']=int(last is not None and (d-last['d']).days==1)
            x[s+'_gp']=sum(1 for e in L if e['season']==g['date'][:4] or (d-e['d']).days<200)
            x[s+'_streak']=0
            for e in reversed(L):
                if x[s+'_streak']>=0 and e['won']: x[s+'_streak']+=1
                elif x[s+'_streak']<=0 and not e['won']: x[s+'_streak']-=1
                else: break
            ra=0
            for e in reversed(L):
                if not e['home']: ra+=1
                else: break
            x[s+'_roadtrip']=ra
            l10=L[-10:]
            x[s+'_pf']=sum(e['pf'] for e in l10)/len(l10) if len(l10)>=5 else None
            x[s+'_pa']=sum(e['pa'] for e in l10)/len(l10) if len(l10)>=5 else None
        lg_avg=sum(gl[-300:])/len(gl[-300:]) if len(gl)>=50 else None
        x['early']=int(min(x['h_gp'],x['a_gp'])<8)
        x['b2b_h']=x['h_b2b']; x['b2b_a']=x['a_b2b']; x['b2b_both']=int(x['h_b2b'] and x['a_b2b'])
        x['rest_diff']=(min(x['h_rest'],5)-min(x['a_rest'],5)) if x['h_rest'] and x['a_rest'] else None
        x['streak_diff']=x['h_streak']-x['a_streak']; x['away_roadtrip']=min(x['a_roadtrip'],6)
        x['pace']=(x['h_pf']+x['h_pa']+x['a_pf']+x['a_pa'])/2-lg_avg if x['h_pf'] is not None and x['a_pf'] is not None and lg_avg else None
        x['net_diff']=((x['h_pf']-x['h_pa'])-(x['a_pf']-x['a_pa'])) if x['h_pf'] is not None and x['a_pf'] is not None else None
        x['playoff']=int(g.get('season_type')=='post-season' or g.get('season_type')=='postseason')
        x['y_T']=g['hs']+g['as_']-g['ou']; x['y_hw']=int(g['hs']>g['as_'])
        x['ph']=ml2p(g['hml'],g['aml']) if g.get('hml') and g.get('aml') else None
        x['y_M']=(g['hs']-g['as_'])+g['spread'] if sport!='mlb' and g.get('spread') is not None else None
        D.append(x); gl.append(g['hs']+g['as_'])
        for s,t in (('h',g['h']),('a',g['a'])):
            pf,pa=(g['hs'],g['as_']) if s=='h' else (g['as_'],g['hs'])
            H[t].append(dict(d=d,home=s=='h',won=pf>pa,pf=pf,pa=pa,season=g['date'][:4]))
    US=[('b2b_h','b'),('b2b_a','b'),('b2b_both','b'),('rest_diff','z'),('early','b'),('streak_diff','z'),('away_roadtrip','z'),('pace','z'),('net_diff','z'),('playoff','b')]
    nm=sport.upper()
    RES+=test(D,'ols','y_T',lambda x:(0.0,[]),US,f'{nm} total vs closing line')
    if sport!='mlb': RES+=test(D,'ols','y_M',lambda x:(0.0,[]),US,f'{nm} home margin vs closing spread')
    RES+=test([x for x in D if x['ph']],'logit','y_hw',lambda x:(lo(x['ph']),[]),US,f'{nm} home win vs closing moneyline')
# ================= C. SPORTYBET'S OWN LINES (tape) — basketball & baseball, all leagues =================
score_={}
for l in open('data/sr_scores.jsonl'):
    s=json.loads(l); score_[str(s['mid'])]=s
lines=collections.defaultdict(dict)
for f in sorted(glob.glob('../papertrade/tape/*.csv.gz')):
    with gzip.open(f,'rt') as g:
        for row in csv.reader(g):
            eid,sport,lg,fx,start,mid,mdesc,spec,desc,oid,odds,hp=row[:12]
            if sport not in ('basketball','baseball') or mid not in ('225','258','223','219','251'): continue
            try: hp=float(hp)
            except: continue
            key=eid.split(':')[-1]; L=lines[key]; L.setdefault('lg',lg); L.setdefault('start',start)
            if mid in ('225','258') and desc.startswith('Over'):
                v=float(spec.split('=')[1])
                if abs(hp-0.5)<abs(L.get('tp',9)-0.5): L['tp']=hp; L['tl']=v; L['sp']=sport
            if mid=='223' and desc.startswith('Home'):
                v=float(spec.split('=')[1])
                if abs(hp-0.5)<abs(L.get('mp',9)-0.5): L['mp']=hp; L['ml']=v
            if mid in ('219','251') and desc=='Home': L['ph']=hp
# also the daily paper-trade snapshots (they carry the same SportyBet lines for every priced basketball/baseball game)
for f in sorted(glob.glob('../papertrade/*_snapshot.json')):
    for o_ in json.load(open(f)):
        if o_.get('sport') not in ('basketball','baseball') or o_['mid'] not in ('225','258','223','219','251'): continue
        key=o_['eid'].split(':')[-1]; L=lines[key]; hp=o_['hp'] or 0; d=o_['desc']; sp=o_.get('spec') or ''
        if o_['mid'] in ('225','258') and d.startswith('Over') and abs(hp-0.5)<abs(L.get('tp',9)-0.5): L['tp']=hp; L['tl']=float(sp.split('=')[1])
        if o_['mid']=='223' and d.startswith('Home') and abs(hp-0.5)<abs(L.get('mp',9)-0.5): L['mp']=hp; L['ml']=float(sp.split('=')[1])
        if o_['mid'] in ('219','251') and d=='Home': L['ph']=hp
SD={'basketball':17.5,'baseball':3.5}
SB=[]
for key,L in lines.items():
    s=score_.get(key)
    if not s or 'tl' not in L or s.get('hs') is None: continue
    x=dict(date=dt.datetime.fromisoformat(s['date']),sport=s['sport'],lg=s['lg'],h=s['h'],a=s['a'],hs=s['hs'],as_=s['as_'],
           muT=L['tl']+SD[s['sport']]*norm.ppf(min(max(L['tp'],0.02),0.98)),ph=L.get('ph'),
           muM=(-L['ml']+13*norm.ppf(min(max(L['mp'],0.02),0.98))) if 'ml' in L else None)
    SB.append(x)
# team history from the full Sportradar score file (all leagues, not just tape days)
hist=collections.defaultdict(list)
allg=sorted((json.loads(l) for l in open('data/sr_scores.jsonl')),key=lambda s:s['date'])
idx={}
for s in allg:
    d=dt.date.fromisoformat(s['date'])
    for t,pf,pa,hm in ((s['h'],s['hs'],s['as_'],1),(s['a'],s['as_'],s['hs'],0)):
        if pf is None: continue
        idx[(str(s['mid']),hm)]=list(hist[t])
        hist[t].append(dict(d=d,pf=pf,pa=pa,home=hm))
key_of={(x['h'],x['a'],x['date'].date().isoformat()):x for x in SB}
for s in allg:
    x=key_of.get((s['h'],s['a'],s['date']))
    if not x: continue
    d=dt.date.fromisoformat(s['date'])
    for side,hm in (('h',1),('a',0)):
        P=idx.get((str(s['mid']),hm),[])
        x[side+'_rest']=(d-P[-1]['d']).days if P else None
        l10=P[-10:]
        x[side+'_tot']=sum(e['pf']+e['pa'] for e in l10)/len(l10) if len(l10)>=4 else None
        x[side+'_net']=sum(e['pf']-e['pa'] for e in l10)/len(l10) if len(l10)>=4 else None
        x[side+'_n']=len(P)
for x in SB:
    x['y_T']=x['hs']+x['as_']-x['muT']; x['y_M']=(x['hs']-x['as_'])-x['muM'] if x['muM'] is not None else None
    x['y_hw']=int(x['hs']>x['as_'])
    x['form_tot']=((x['h_tot']+x['a_tot'])/2-x['muT']) if x.get('h_tot') is not None and x.get('a_tot') is not None else None
    x['form_net']=(x['h_net']-x['a_net']) if x.get('h_net') is not None and x.get('a_net') is not None else None
    x['rest_diff']=(min(x['h_rest'],7)-min(x['a_rest'],7)) if x.get('h_rest') and x.get('a_rest') else None
    x['b2b_any']=int((x.get('h_rest')==1) or (x.get('a_rest')==1)) if x.get('h_rest') and x.get('a_rest') else None
    x['early']=int(min(x.get('h_n',0),x.get('a_n',0))<5)
SBF=[('form_tot','z'),('form_net','z'),('rest_diff','z'),('b2b_any','b'),('early','b')]
for sp in ('basketball','baseball'):
    D=[x for x in SB if x['sport']==sp]
    CUTS=sorted(x['date'] for x in D)
    if len(D)<400: continue
    globals()['CUT']=CUTS[int(len(CUTS)*0.6)]          # tape spans weeks: train first 60%, test last 40%
    RES+=test(D,'ols','y_T',lambda x:(0.0,[]),SBF,f'{sp.title()} total vs SportyBet line (all leagues)')
    if sp=='basketball': RES+=test(D,'ols','y_M',lambda x:(0.0,[]),SBF,'Basketball margin vs SportyBet spread (all leagues)')
    RES+=test([x for x in D if x['ph']],'logit','y_hw',lambda x:(lo(x['ph']),[]),SBF,f'{sp.title()} home win vs SportyBet price (all leagues)')
    globals()['CUT']=dt.datetime(2025,7,1)
json.dump(RES,open('cache/factor2_results.json','w'),default=str)
# ================= report =================
NAME={'rest_diff':'rest days (home − away)','cong_h':'home side played ≤3 days ago','cong_a':'away side played ≤3 days ago','early':'first 4 rounds of season',
 'late':'last 15% of season','prom_h':'home side newly promoted','prom_a':'away side newly promoted','ref_g':'referee avg goals (last 20)','ref_hw':'referee home-win rate (last 30)',
 'gap':'table-position gap','releg':'two bottom-20% sides, 2nd half of season','title':'two top-15% sides','late_bottom_h':'home side bottom-20% in run-in',
 'mid':'midweek (Tue-Thu)','dec_jan':'December/January','aug_sep':'August/September','h2h_draw':'H2H draw rate (last 3-6)','form_h':'home points form (last 5)',
 'form_a':'away points form (last 5)','sot_sum':'both sides\' shots on target form','b2b_h':'home team on back-to-back','b2b_a':'away team on back-to-back',
 'b2b_both':'both on back-to-back','streak_diff':'win streak (home − away)','away_roadtrip':'away team\'s road-trip length','pace':'both teams\' recent scoring vs league',
 'net_diff':'recent net rating (home − away)','playoff':'playoffs','form_tot':'both teams\' recent totals vs line','form_net':'recent net margin (home − away)','b2b_any':'either team on a back-to-back'}
def oof(x): return '' if x['oos'] is None else (f"{x['oos']:+.2f} pts² MSE" if x['kind']=='ols' else f"{x['oos']*1e4:+.1f}")
def unit(x):
    if x['kind']=='pois': return f"{x['eff']:+.1f}%"
    if x['kind']=='logit': return f"{x['coef']:+.3f} log-odds"
    return f"{x['coef']:+.2f} pts/runs"
def verdict(x):
    if x['n_on'] is not None and min(x['n_on'],x['n']-x['n_on'])<100: return 'too few games with the flag to judge'
    stable=np.sign(x['early'])==np.sign(x['late'])
    if abs(x['t'])>=2 and stable and (x['oos'] is None or x['oos']>0): return '**real, beyond the price**'
    if abs(x['t'])>=2 and stable: return 'real in-sample, fails out of sample'
    return 'no effect beyond the price'
o=['<!-- PART2 -->','## Part 2 — other markets and other sports','',
   'Same test: each factor is added on top of the price (football: market expectation; US sports: closing line; tape: SportyBet\'s own line). "Effect" is per 1 SD for continuous factors, or the effect of the flag being on. A factor counts only if |t|≥2, the sign is the same in both halves of the data, and it improves out-of-sample prediction.','']
by=collections.defaultdict(list)
for x in RES: by[x['market']].append(x)
real=[x for x in RES if verdict(x).startswith('**real')]
nt=len(RES); o+=[f'**Multiple-testing warning:** {nt} factor×market tests were run. At |t|≥2, about {round(nt*0.046)} would pass by chance alone, and about half of those also keep their sign across both halves. So treat the |t| 2-3 rows as unconfirmed; only |t|≥3 rows are strong evidence.','','### What survives (all markets, all sports)','','| Market | Factor | n | Effect | t | Out-of-sample |','|---|---|---|---|---|---|']
o+=[f"| {x['market']} | {NAME.get(x['factor'],x['factor'])} | {x['n']:,} | {unit(x)} | {x['t']:+.1f} | {oof(x)} |" for x in sorted(real,key=lambda x:-abs(x['t']))] or ['| none | | | | | |']
for mk,L in by.items():
    o+=['',f'### {mk}','','| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |','|---|---|---|---|---|---|---|---|']
    for x in sorted(L,key=lambda x:-abs(x['t'])):
        oo=oof(x)
        o.append(f"| {NAME.get(x['factor'],x['factor'])}{' (n on='+str(x['n_on'])+')' if x['n_on'] is not None else ''} | {x['n']:,} | {unit(x)} | {x['t']:+.1f} | {x['early']:+.3f} | {x['late']:+.3f} | {oo} | {verdict(x)} |")
o.append('<!-- /PART2 -->')
P='../papertrade/FACTORS.md'; s=open(P).read()
s=s.split('<!-- PART2 -->')[0].rstrip()+'\n\n'+'\n'.join(o)+'\n'
open(P,'w').write(s)
for x in sorted(real,key=lambda x:-abs(x['t'])): print('REAL',x['market'],x['factor'],round(x['t'],1),unit(x),x['oos'])
print('tested',len(RES),'real',len(real)); print('tape SB n',collections.Counter(x['sport'] for x in SB))
