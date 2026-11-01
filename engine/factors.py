# FACTOR STUDY: what actually predicts goals / corners / cards, and does it add anything BEYOND the betting price?
# Data: football-data.co.uk CSVs in engine/fdcsv/ (run fd_fetch.sh; 19 leagues x 5 seasons, closing odds, shots,
# corners, cards, fouls; xG only in 2026-27).  Every feature is computed from matches played BEFORE kick-off.
# For each (target, factor) we report:
#   raw   = how much the target moves per 1 SD of the factor on its own (Poisson rate ratio), and its correlation
#   +mkt  = the same, but with the market-implied expectation as an offset: does the factor add information the price lacks?
#   OOS   = out-of-sample log-likelihood gain per match (train <2025-07, test >=2025-07) when the factor is added on top of
#           the baseline.  Positive = the factor genuinely improves prediction; ~0 = already priced; negative = noise.
# Output: ../papertrade/FACTORS.md  and  factor_coefs.json (fitted multipliers the pricers can use).
import csv,glob,math,json,collections,datetime as dt,numpy as np
import anc
def f(x):
    try: return float(x)
    except: return None
TOP={'E0','D1','I1','SP1','F1'}
def load():
    R=[]
    for fn in sorted(glob.glob('fdcsv/*.csv')):
        lg,season=fn.split('/')[-1][:-4].split('_')
        try: rd=list(csv.DictReader(open(fn,encoding='utf-8-sig',errors='ignore')))
        except Exception: continue
        for r in rd:
            try:
                d=dt.datetime.strptime(r['Date'],'%d/%m/%Y' if len(r['Date'])==10 else '%d/%m/%y')
                hg,ag=int(r['FTHG']),int(r['FTAG'])
            except Exception: continue
            g=lambda k:f(r.get(k))
            oh,od,oa=g('AvgCH') or g('AvgH'),g('AvgCD') or g('AvgD'),g('AvgCA') or g('AvgA')
            o25,u25=g('AvgC>2.5') or g('Avg>2.5'),g('AvgC<2.5') or g('Avg<2.5')
            if not (oh and od and oa and o25 and u25): continue
            R.append(dict(lg=lg,season=season,date=d,h=r['HomeTeam'],a=r['AwayTeam'],hg=hg,ag=ag,
                hs=g('HS'),as_=g('AS'),hst=g('HST'),ast=g('AST'),hc=g('HC'),ac=g('AC'),hy=g('HY'),ay=g('AY'),
                hf=g('HF'),af=g('AF'),hxg=g('HxG'),axg=g('AxG'),ref=r.get('Referee') or None,
                oh=oh,od=od,oa=oa,o25=o25,u25=u25))
    R.sort(key=lambda x:x['date']); return R
# ---------- market expectation (lambda_home, lambda_away) from devigged 1X2 + O/U 2.5 ----------
_cache={}
def mkt(r):
    pH,pD,pA=anc.devig(r['oh'],r['od'],r['oa']); pO,_=anc.devig(r['o25'],r['u25'])
    k=(round(pH,3),round(pD,3),round(pA,3),round(pO,3))
    if k not in _cache:
        a,b=anc.fit(pH,pD,pA,pO); _cache[k]=(anc.L[a],anc.L[b])
    return _cache[k]
# ---------- rolling pre-match features ----------
def mean(v): v=[x for x in v if x is not None]; return sum(v)/len(v) if v else None
def build(R):
    hist=collections.defaultdict(list)          # team -> list of past team-perspective dicts
    tab=collections.defaultdict(lambda:dict(p=0,gd=0,n=0,gf=0))   # (lg,season,team)
    h2h=collections.defaultdict(list)           # frozenset(teams) -> past total goals
    refc=collections.defaultdict(list)          # referee -> past total yellows
    rows=[]
    for r in R:
        lh,la=mkt(r); r['lh'],r['la']=lh,la
        # league table snapshot BEFORE this match
        teams=[k for k in tab if k[0]==r['lg'] and k[1]==r['season']]
        def rank(t):
            me=tab[(r['lg'],r['season'],t)]
            if me['n']<5: return None
            ppg=lambda k:(tab[k]['p']/tab[k]['n'],tab[k]['gd']/tab[k]['n']) if tab[k]['n'] else (0,0)
            others=sorted((ppg(k) for k in teams),reverse=True)
            return (others.index(ppg((r['lg'],r['season'],t)))/max(len(others)-1,1))   # 0 = top, 1 = bottom
        hk=frozenset((r['h'],r['a'])); pr=h2h[hk][-4:]
        rv=refc[r['ref']][-15:] if r['ref'] else []
        for side,t,o in (('h',r['h'],r['a']),('a',r['a'],r['h'])):
            H=hist[t]; O=hist[o]; P=lambda L,k,n:mean([x[k] for x in L[-n:]]) if len(L)>=min(n,5) else None
            me=tab[(r['lg'],r['season'],t)]; op=tab[(r['lg'],r['season'],o)]
            ven=[x for x in H if x['home']==(side=='h')]
            x=dict(lg=r['lg'],season=r['season'],date=r['date'],top=r['lg'] in TOP,home=side=='h',
                y_g=r['hg'] if side=='h' else r['ag'], y_ga=r['ag'] if side=='h' else r['hg'],
                y_c=r['hc'] if side=='h' else r['ac'], y_ca=r['ac'] if side=='h' else r['hc'],
                y_y=r['hy'] if side=='h' else r['ay'],
                lam=lh if side=='h' else la, lam_o=la if side=='h' else lh,
                # attacking form
                gf5=P(H,'gf',5),gf10=P(H,'gf',10),sf10=P(H,'sf',10),sotf10=P(H,'sotf',10),xgf5=P(H,'xgf',5),
                cf10=P(H,'cf',10),gfv5=P(ven,'gf',5),
                # defensive form
                ga5=P(H,'ga',5),ga10=P(H,'ga',10),sa10=P(H,'sa',10),sota10=P(H,'sota',10),xga5=P(H,'xga',5),
                ca10=P(H,'ca',10),
                # opponent defence / attack
                o_ga10=P(O,'ga',10),o_sota10=P(O,'sota',10),o_ca10=P(O,'ca',10),o_cf10=P(O,'cf',10),o_xga5=P(O,'xga',5),
                o_gf10=P(O,'gf',10),
                # luck: goals minus shots-on-target conversion baseline / minus xG
                fin10=(P(H,'gf',10)-0.30*P(H,'sotf',10)) if P(H,'gf',10) is not None and P(H,'sotf',10) is not None else None,
                xgluck5=(P(H,'gf',5)-P(H,'xgf',5)) if P(H,'xgf',5) is not None and P(H,'gf',5) is not None else None,
                cards10=P(H,'yf',10),o_cards10=P(O,'yf',10),fouls10=P(H,'ff',10),
                pts5=P(H,'pts',5),rank=rank(t),o_rank=rank(o),
                ppg=me['p']/me['n'] if me['n']>=5 else None,o_ppg=op['p']/op['n'] if op['n']>=5 else None,
                rest=(r['date']-H[-1]['date']).days if H else None,o_rest=(r['date']-O[-1]['date']).days if O else None,
                h2h=mean(pr) if len(pr)>=2 else None,
                ref_y=mean(rv) if len(rv)>=8 else None,
                rnd=me['n'])
            rows.append(x)
        # update histories AFTER recording features
        for side,t,o in (('h',r['h'],r['a']),('a',r['a'],r['h'])):
            H= side=='h'; gf,ga=(r['hg'],r['ag']) if H else (r['ag'],r['hg'])
            k=lambda a,b:(r[a] if H else r[b])
            hist[t].append(dict(date=r['date'],home=H,gf=gf,ga=ga,sf=k('hs','as_'),sa=k('as_','hs'),sotf=k('hst','ast'),
               sota=k('ast','hst'),cf=k('hc','ac'),ca=k('ac','hc'),yf=k('hy','ay'),ff=k('hf','af'),
               xgf=k('hxg','axg'),xga=k('axg','hxg'),pts=3 if gf>ga else 1 if gf==ga else 0))
            m=tab[(r['lg'],r['season'],t)]; m['n']+=1; m['p']+=3 if gf>ga else 1 if gf==ga else 0; m['gd']+=gf-ga
        h2h[hk].append(r['hg']+r['ag'])
        if r['ref'] and r['hy'] is not None: refc[r['ref']].append(r['hy']+r['ay'])
    global STATE; STATE=(hist,tab)
    return rows
# ---------- Poisson regression with offset (IRLS) ----------
def pois(X,y,off,it=30):
    b=np.zeros(X.shape[1])
    for _ in range(it):
        eta=np.clip(off+X@b,-10,10); mu=np.exp(eta)
        W=mu; z=(eta-off)+(y-mu)/mu
        A=X.T@(X*W[:,None])+1e-6*np.eye(X.shape[1]); b2=np.linalg.solve(A,X.T@(W*z))
        if np.max(abs(b2-b))<1e-8: b=b2; break
        b=b2
    mu=np.exp(off+X@b); cov=np.linalg.inv(X.T@(X*mu[:,None])+1e-6*np.eye(X.shape[1]))
    # overdispersion-robust SE (sandwich)
    U=X*(y-mu)[:,None]; S=cov@(U.T@U)@cov
    return b,np.sqrt(np.diag(S))
def ll(y,mu): from scipy.special import gammaln; return float(np.mean(y*np.log(mu)-mu-gammaln(y+1)))
CUT=dt.datetime(2025,7,1)
def study(rows,target,feats,base,label):
    """base(row)->(log offset, list of baseline covariates).  Returns per-feature raw / +mkt / OOS table."""
    out=[]
    for fe in feats:
        D=[r for r in rows if r.get(target) is not None and r.get(fe) is not None]
        if len(D)<800: continue
        v=np.array([r[fe] for r in D],float); mu_,sd=v.mean(),v.std() or 1; z=(v-mu_)/sd
        y=np.array([r[target] for r in D],float)
        # raw: log(y) ~ const + z
        X=np.c_[np.ones(len(D)),z]; b,se=pois(X,y,np.zeros(len(D)))
        corr=float(np.corrcoef(z,y)[0,1])
        # +mkt: offset = baseline
        off=np.array([base(r)[0] for r in D]); C=np.array([base(r)[1] for r in D],float).reshape(len(D),-1)
        X0=np.c_[np.ones(len(D)),C]; X1=np.c_[X0,z]
        b1,se1=pois(X1,y,off)
        tr=np.array([r['date']<CUT for r in D]); te=~tr
        if te.sum()<300 or tr.sum()<500: oos=None
        else:
            b0t,_=pois(X0[tr],y[tr],off[tr]); b1t,_=pois(X1[tr],y[tr],off[tr])
            oos=ll(y[te],np.exp(off[te]+X1[te]@b1t))-ll(y[te],np.exp(off[te]+X0[te]@b0t))
        out.append(dict(target=label,feat=fe,n=len(D),corr=corr,raw=math.exp(b[1]),raw_t=b[1]/se[1],
                        mkt=math.exp(b1[-1]),mkt_t=b1[-1]/se1[-1],oos=oos,sd=sd,mean=mu_))
    return out
NAMES={'gf5':'own goals scored, last 5','gf10':'own goals scored, last 10','sf10':'own shots, last 10','sotf10':'own shots on target, last 10',
 'xgf5':'own xG, last 5','cf10':'own corners won, last 10','gfv5':'own goals at this venue, last 5','ga5':'own goals conceded, last 5',
 'ga10':'own goals conceded, last 10','sa10':'shots conceded, last 10','sota10':'shots on target conceded, last 10','xga5':'xG conceded, last 5',
 'ca10':'corners conceded, last 10','o_ga10':'opponent goals conceded, last 10','o_sota10':'opponent SoT conceded, last 10',
 'o_ca10':'opponent corners conceded, last 10','o_cf10':'opponent corners won, last 10','o_xga5':'opponent xG conceded, last 5','o_gf10':'opponent goals scored, last 10',
 'fin10':'finishing luck (goals - 0.3xSoT), last 10','xgluck5':'goals minus xG, last 5','cards10':'own yellows, last 10','o_cards10':'opponent yellows, last 10',
 'fouls10':'own fouls, last 10','pts5':'form: points per game, last 5','rank':'own table position (0 top, 1 bottom)','o_rank':'opponent table position',
 'ppg':'own season points per game','o_ppg':'opponent season points per game','rest':'own rest days','o_rest':'opponent rest days',
 'h2h':'avg total goals, last 2-4 H2H','ref_y':'referee avg yellows, last 15 games','rnd':'matches played this season','lam':'market goal expectation'}
if __name__=='__main__':
    R=load(); print('matches',len(R)); rows=build(R); print('team-rows',len(rows))
    for r in rows:
        r['y_tot']=None
    # Baselines.  Goals: offset = log(market lambda for this team).  Corners/cards: no market price in the data, so the
    # baseline is the best price-derived model we have: log(league-season mean) + log(lambda) + log(lambda_opp) + home.
    lgm=collections.defaultdict(list)
    for r in rows:
        if r['date']<CUT:
            for k in ('y_c','y_y'):
                if r[k] is not None: lgm[(r['lg'],k)].append(r[k])
    lgm={k:sum(v)/len(v) for k,v in lgm.items()}
    bg=lambda r:(math.log(r['lam']),[])
    bc=lambda r:(math.log(lgm.get((r['lg'],'y_c'),5.0)),[math.log(r['lam']),math.log(r['lam_o']),r['home']])
    by=lambda r:(math.log(lgm.get((r['lg'],'y_y'),2.0)),[abs(math.log(r['lam']/r['lam_o'])),math.log(r['lam']+r['lam_o']),r['home']])
    G=['lam','gf5','gf10','gfv5','sf10','sotf10','xgf5','fin10','xgluck5','o_ga10','o_sota10','o_xga5','pts5','ppg','rank','o_rank','o_ppg','rest','o_rest','h2h','rnd']
    GA=['ga5','ga10','sa10','sota10','xga5','o_gf10','rank','o_rank','pts5','rest','h2h']
    CF=['lam','cf10','sf10','o_ca10','gf10','pts5','rank','o_rank','o_ppg','rest']
    CA=['ca10','sa10','o_cf10','ga10','rank','o_rank','pts5','ppg']
    YF=['cards10','o_cards10','fouls10','ref_y','rank','o_rank','pts5','h2h']
    res=[]
    res+=study(rows,'y_g',G,bg,'Team goals scored')
    # goals conceded = the opponent's goals; offset = market lambda of the opponent
    for r in rows: r['y_gc']=r['y_ga']
    res+=study(rows,'y_gc',GA,lambda r:(math.log(r['lam_o']),[]),'Team goals conceded')
    res+=study(rows,'y_c',CF,bc,'Team corners won')
    for r in rows: r['y_cc']=r['y_ca']
    res+=study(rows,'y_cc',CA,lambda r:(math.log(lgm.get((r['lg'],'y_c'),5.0)),[math.log(r['lam_o']),math.log(r['lam']),1-r['home']]),'Team corners conceded')
    res+=study(rows,'y_y',YF,by,'Team yellow cards')
    json.dump(res,open('cache/factor_results.json','w'),default=str)
    # ---------- xG vs goals (2026-27 only): which past measure best predicts next-match goals? ----------
    xs=[r for r in rows if r['season']=='2627' and r['xgf5'] is not None and r['gf5'] is not None and r['sotf10'] is not None]
    xgcmp={}
    if len(xs)>200:
        y=np.array([r['y_g'] for r in xs],float)
        for k in ('gf5','xgf5','sotf10','lam'):
            xgcmp[k]=float(np.corrcoef([r[k] for r in xs],y)[0,1])
        # does xG add beyond the price?
        z=np.array([r['xgf5'] for r in xs]); z=(z-z.mean())/z.std(); off=np.log([r['lam'] for r in xs])
        b,se=pois(np.c_[np.ones(len(xs)),z],y,off); xgcmp['xg_beyond_mkt']=(math.exp(b[1]),b[1]/se[1],len(xs))
    # same-match xG vs goals (descriptive): how tightly does a match's xG track its goals?
    sm=[(r['hxg'],r['hg']) for r in R if r['hxg'] is not None]+[(r['axg'],r['ag']) for r in R if r['axg'] is not None]
    if sm: xgcmp['same_match_corr']=float(np.corrcoef(*zip(*sm))[0,1]); xgcmp['same_match_n']=len(sm)
    json.dump(xgcmp,open('cache/factor_xg.json','w'))
    print(json.dumps(xgcmp,indent=1))
    for x in res: print(f"{x['target']:24s} {x['feat']:9s} n={x['n']:6d} corr={x['corr']:+.3f} raw={x['raw']:.3f}({x['raw_t']:+.1f}) +mkt={x['mkt']:.3f}({x['mkt_t']:+.1f}) oos={x['oos'] if x['oos'] is None else round(x['oos']*1e4,2)}")
