# Stage 2 of the factor study: effect sizes in plain units (quintiles), combined models out of sample,
# US sports (form vs closing lines), and FACTORS.md.  Run after factors.py (re-builds the features itself).
import json,math,collections,datetime as dt,numpy as np
import factors as F
R=F.load(); rows=F.build(R); CUT=F.CUT
for r in rows: r['y_gc']=r['y_ga']; r['y_cc']=r['y_ca']
lgm=collections.defaultdict(list)
for r in rows:
    if r['date']<CUT:
        for k in ('y_c','y_y'):
            if r[k] is not None: lgm[(r['lg'],k)].append(r[k])
lgm={k:sum(v)/len(v) for k,v in lgm.items()}
# opponent's last-5 conceded (the over-reaction test from the goals-conceded table, seen from the scoring side)
byid=collections.defaultdict(dict)
for i in range(0,len(rows),2):
    a,b=rows[i],rows[i+1]; a['o_ga5'],b['o_ga5']=b['ga5'],a['ga5']; a['o_fouls10'],b['o_fouls10']=b['fouls10'],a['fouls10']
    a['o_sotf10'],b['o_sotf10']=b['sotf10'],a['sotf10']; a['o_pts5'],b['o_pts5']=b['pts5'],a['pts5']
BASE={
 'y_g':  lambda r:(math.log(r['lam']),[]),
 'y_c':  lambda r:(math.log(lgm.get((r['lg'],'y_c'),5.0)),[math.log(r['lam']),math.log(r['lam_o']),r['home']]),
 'y_cc': lambda r:(math.log(lgm.get((r['lg'],'y_c'),5.0)),[math.log(r['lam_o']),math.log(r['lam']),1-r['home']]),
 'y_y':  lambda r:(math.log(lgm.get((r['lg'],'y_y'),2.0)),[abs(math.log(r['lam']/r['lam_o'])),math.log(r['lam']+r['lam_o']),r['home']]),
}
COMBO={
 'y_g':['sotf10','o_sota10','o_ga5','fin10','o_rank'],
 'y_c':['cf10','o_ca10','gf10','o_rank','rank'],
 'y_cc':['ca10','o_cf10','sa10','rank','ppg'],
 'y_y':['cards10','fouls10','o_fouls10','ref_y','rank','o_rank','pts5','o_pts5'],
}
LAB={'y_g':'Team goals scored','y_c':'Team corners won','y_cc':'Team corners conceded','y_y':'Team yellow cards'}
def design(D,feats,stats=None):
    if stats is None:
        stats={}
        for fe in feats:
            v=[r[fe] for r in D if r.get(fe) is not None and r['date']<CUT]; m=sum(v)/len(v); s=float(np.std(v)) or 1; stats[fe]=(m,s)
    Z=np.array([[((r[fe]-stats[fe][0])/stats[fe][1]) if r.get(fe) is not None else 0.0 for fe in feats] for r in D])
    M=np.array([[1.0 if r.get(fe) is None else 0.0 for fe in feats if fe=='ref_y'] for r in D]).reshape(len(D),-1)
    return np.c_[Z,M],stats
combo_out={}; coefs={}
for t,feats in COMBO.items():
    D=[r for r in rows if r.get(t) is not None]
    y=np.array([r[t] for r in D],float); B=[BASE[t](r) for r in D]; off=np.array([b[0] for b in B])
    C=np.array([b[1] for b in B],float).reshape(len(D),-1); X0=np.c_[np.ones(len(D)),C]
    Zf,stats=design(D,feats); X1=np.c_[X0,Zf]
    tr=np.array([r['date']<CUT for r in D]); te=~tr
    b0,_=F.pois(X0[tr],y[tr],off[tr]); b1,se1=F.pois(X1[tr],y[tr],off[tr])
    mu0=np.exp(off[te]+X0[te]@b0); mu1=np.exp(off[te]+X1[te]@b1)
    gain=F.ll(y[te],mu1)-F.ll(y[te],mu0)
    # in plain units: how far the factors move the expectation, and does the move come true in the test set?
    ratio=mu1/mu0; q=np.quantile(ratio,[0.2,0.4,0.6,0.8]); bins=np.digitize(ratio,q)
    qt=[(float(ratio[bins==k].mean()),float(y[te][bins==k].sum()/mu0[bins==k].sum()),int((bins==k).sum())) for k in range(5)]
    k0=X0.shape[1]
    combo_out[t]=dict(n_tr=int(tr.sum()),n_te=int(te.sum()),gain=gain,qt=qt,
        coef={fe:(math.exp(b1[k0+i]),b1[k0+i]/se1[k0+i]) for i,fe in enumerate(feats)},
        sd_move=float(np.std(np.log(ratio))))
    coefs[t]=dict(feats=feats,stats=stats,base_coef=list(map(float,b1[:k0])),beta=list(map(float,b1[k0:])))
# incremental fits: only the factors the LIVE pricers do not already use (they already use team corner/card history
# and the market goal expectation), so multiplying the live expectation by these does not double count.
INC={'y_g':(['sotf10','o_sota10','o_ga5','fin10'],[]),
     'y_c':(['gf10','rank','o_rank'],['cf10','o_ca10']),
     'y_y':(['rank','o_rank','pts5','o_pts5','fouls10','o_fouls10'],['cards10','o_cards10'])}
coefs['inc']={}
for t,(ex,ctrl) in INC.items():
    D=[r for r in rows if r.get(t) is not None]
    y=np.array([r[t] for r in D],float); B=[BASE[t](r) for r in D]; off=np.array([b[0] for b in B])
    C=np.array([b[1] for b in B],float).reshape(len(D),-1)
    Zc,_=design(D,ctrl) if ctrl else (np.zeros((len(D),0)),{})
    Ze,st=design(D,ex); X0=np.c_[np.ones(len(D)),C,Zc]; X1=np.c_[X0,Ze]
    tr=np.array([r['date']<CUT for r in D]); te=~tr
    b0,_=F.pois(X0[tr],y[tr],off[tr]); b1,se1=F.pois(X1[tr],y[tr],off[tr])
    gain=F.ll(y[te],np.exp(off[te]+X1[te]@b1))-F.ll(y[te],np.exp(off[te]+X0[te]@b0))
    bF,seF=F.pois(X1,y,off)        # final coefficients on all data
    k0=X0.shape[1]
    coefs['inc'][t]=dict(feats=ex,stats={k:st[k] for k in ex},beta=[float(v) for v in bF[k0:k0+len(ex)]],
        t=[float(bF[k0+i]/seF[k0+i]) for i in range(len(ex))],oos_gain=gain)
    print('INC',t,round(gain*1e4,2),dict(zip(ex,[round(math.exp(v),3) for v in bF[k0:k0+len(ex)]])))
json.dump(coefs,open('factor_coefs.json','w'),indent=1)
# ---------- quintile tables for headline factors: actual / expected under the baseline ----------
def qtab(t,fe):
    D=[r for r in rows if r.get(t) is not None and r.get(fe) is not None]
    y=np.array([r[t] for r in D],float); B=[BASE[t](r) for r in D]; off=np.array([b[0] for b in B])
    C=np.array([b[1] for b in B],float).reshape(len(D),-1); X0=np.c_[np.ones(len(D)),C]
    b0,_=F.pois(X0,y,off); mu=np.exp(off+X0@b0)
    v=np.array([r[fe] for r in D]); q=np.quantile(v,[0.2,0.4,0.6,0.8]); bins=np.digitize(v,q)
    return [(float(v[bins==k].mean()),float(y[bins==k].mean()),float(y[bins==k].sum()/mu[bins==k].sum()),int((bins==k).sum())) for k in range(5)]
Q={}
for t,fe in [('y_g','gf10'),('y_g','sotf10'),('y_g','rank'),('y_g','pts5'),('y_g','o_ga5'),('y_g','fin10'),('y_gc','ga10'),
             ('y_c','cf10'),('y_c','o_rank'),('y_cc','rank'),('y_cc','ca10'),('y_y','ref_y'),('y_y','cards10'),('y_y','o_rank')]:
    if t=='y_gc': BASE['y_gc']=lambda r:(math.log(r['lam_o']),[])
    Q[(t,fe)]=qtab(t,fe)
# ---------- US sports: does recent form beat the closing line? ----------
def us(sport):
    G=[json.loads(l) for l in open(f'data/espn_{sport}.jsonl')]
    G=[g for g in G if g.get('ou') and g.get('spread') is not None and g.get('season_type')!='preseason' and g.get('hs') is not None]
    G.sort(key=lambda g:g['date']); H=collections.defaultdict(list); out=[]
    for g in G:
        d=dt.date.fromisoformat(g['date']); x=dict(date=g['date'])
        for s,t,o in (('h',g['h'],g['a']),('a',g['a'],g['h'])):
            L=H[t][-10:]
            x[s+'_mar']=sum(e['mar'] for e in L)/len(L) if len(L)>=5 else None
            x[s+'_ats']=sum(e['ats'] for e in L)/len(L) if len(L)>=5 else None   # avg margin vs closing spread
            x[s+'_ovr']=sum(e['ovr'] for e in L)/len(L) if len(L)>=5 else None   # avg total vs closing total
            x[s+'_rest']=(d-H[t][-1]['d']).days if H[t] else None
        x['res_T']=g['hs']+g['as_']-g['ou']; x['res_M']=(g['hs']-g['as_'])+g['spread']
        out.append(x)
        for s,t in (('h',g['h']),('a',g['a'])):
            sg=1 if s=='h' else -1; mar=sg*(g['hs']-g['as_'])
            H[t].append(dict(d=d,mar=mar,ats=mar+sg*g['spread'],ovr=g['hs']+g['as_']-g['ou']))
    res={}
    for tgt,feats in (('res_T',[('ovr_sum',lambda x:x['h_ovr']+x['a_ovr'] if x['h_ovr'] is not None and x['a_ovr'] is not None else None),
                                 ('b2b_any',lambda x:int((x['h_rest']==1) or (x['a_rest']==1)) if x['h_rest'] and x['a_rest'] else None)]),
                      ('res_M',[('ats_diff',lambda x:x['h_ats']-x['a_ats'] if x['h_ats'] is not None and x['a_ats'] is not None else None),
                                ('mar_diff',lambda x:x['h_mar']-x['a_mar'] if x['h_mar'] is not None and x['a_mar'] is not None else None),
                                ('rest_diff',lambda x:min(x['h_rest'],4)-min(x['a_rest'],4) if x['h_rest'] and x['a_rest'] else None)])):
        for name,fn in feats:
            D=[(fn(x),x[tgt],x['date']) for x in out]; D=[d for d in D if d[0] is not None]
            if len(D)<200: continue
            v=np.array([d[0] for d in D],float); y=np.array([d[1] for d in D],float)
            z=(v-v.mean())/(v.std() or 1); b=float(np.dot(z,y)/np.dot(z,z)); e=y-b*z
            se=float(np.sqrt(np.sum(e**2)/(len(y)-1)/np.dot(z,z)))
            half=len(D)//2; b1=float(np.dot(z[:half],y[:half])/np.dot(z[:half],z[:half])); b2=float(np.dot(z[half:],y[half:])/np.dot(z[half:],z[half:]))
            res[(tgt,name)]=dict(n=len(D),slope=b,t=b/se,early=b1,late=b2,bias=float(y.mean()))
    return res
US={s:us(s) for s in ('nba','wnba','mlb')}
# ---------- write FACTORS.md ----------
res=json.load(open('cache/factor_results.json')); xg=json.load(open('cache/factor_xg.json'))
N=F.NAMES; N.update({'o_ga5':'opponent goals conceded, last 5','o_fouls10':'opponent fouls, last 10','o_pts5':'opponent points per game, last 5'})
def oo(x): return '' if x['oos'] is None else f"{x['oos']*1e4:+.2f}"
def pct(m): return f"{(m-1)*100:+.1f}%"
def verdict(x):
    if x['oos'] is None: return 'too few matches to test out of sample'
    if abs(x['mkt_t'])<2 or x['oos']<=0.5e-4: return '**already in the price** (no extra information)'
    return '**adds information beyond the price**'
o=['# What actually affects what — factor study','',
 f'Data: {len(R):,} matches (19 European leagues, 2022-23 to 2026-27; closing odds, shots, corners, cards, fouls; xG for 2026-27 only), plus NBA/WNBA/MLB closing lines. Every factor is measured from matches played **before** kick-off. Train = before July 2025, test = July 2025 onward.','',
 '## How to read this','',
 '- **Raw effect** = how much the outcome moves per 1 standard deviation of the factor, ignoring the odds. This is the question "does attacking form affect goals?".',
 '- **Beyond the price** = the same, after accounting for what the betting market already expects. This is the question that matters for betting: if the market already knows it, the factor gives no edge.',
 '- **Out-of-sample gain** = how much the factor improves predictions on games the model never saw (×10⁻⁴ nats per match). Anything ≤0.5 is noise.',
 '- For corners and cards there is no market price in this data, so "beyond the price" means beyond a baseline built from the goals market (expected goals for both sides, home/away, league average). SportyBet\'s own corner/card lines may already contain some of these factors.','']
o+=['## Headline answers','']
g=lambda t,f_:next((x for x in res if x['target']==t and x['feat']==f_),None)
def line(t,f_,q):
    x=g(t,f_); return f"- {q} Raw: {pct(x['raw'])} per SD (t={x['raw_t']:+.0f}). Beyond the price: {pct(x['mkt'])} (t={x['mkt_t']:+.1f}), out-of-sample {x['oos']*1e4:+.2f} → {verdict(x)}."
o+=[line('Team goals scored','gf10','**Does attacking form (goals scored, last 10) affect a team\'s goals?** Yes, strongly — but the market already prices it.'),
    line('Team goals scored','sotf10','**Shots on target form** is a better predictor than goals form, and a little of it is *not* fully priced.'),
    f"- **Does expected goals (xG) affect goals scored?** Within the same match, xG and goals correlate {xg.get('same_match_corr',0):.2f} (n={xg.get('same_match_n',0):,}) — xG explains a lot of what happened, but goals are noisy. As a *predictor*, a team's last-5 xG correlates {xg.get('xgf5',0):.2f} with its next-match goals vs {xg.get('gf5',0):.2f} for last-5 goals and {xg.get('sotf10',0):.2f} for last-10 shots on target; the market price alone correlates {xg.get('lam',0):.2f}. Beyond the price, xG adds {pct(xg['xg_beyond_mkt'][0])} per SD (t={xg['xg_beyond_mkt'][1]:+.1f}, n={xg['xg_beyond_mkt'][2]:,}, one season only) → not significant yet.",
    line('Team goals scored','rank','**Does table position affect goals scored?** Yes raw (top sides score more), but it is fully in the price.'),
    line('Team goals conceded','ga5','**Recent goals conceded:** the market slightly *over-reacts* — a side that has just leaked goals concedes a bit less than priced next time.'),
    line('Team goals scored','fin10','**Finishing luck** (goals above what shots on target would predict): there is a faint hint that the market over-rates hot finishers (mean reversion), but on its own it does not survive the out-of-sample test.'),
    line('Team goals scored','pts5','**Points form (last 5)** has no information beyond the price.'),
    line('Team goals scored','h2h','**Head-to-head goals** has no information beyond the price.'),
    line('Team goals scored','rest','**Rest days** don\'t matter for goals in this data.'),
    line('Team corners conceded','rank','**Does table position affect corners conceded?** Yes: lower-placed sides concede more corners, and some of it survives the baseline.'),
    line('Team corners conceded','ca10','**Corners-conceded form** carries the most signal for corners conceded.'),
    line('Team corners won','cf10','**Corners-won form** predicts corners won.'),
    line('Team corners won','gf10','**Goals form and corners:** once expected goals are known, sides that have been *scoring* more win *fewer* corners — leading teams sit back.'),
    line('Team yellow cards','ref_y','**The referee** is the biggest single card factor.'),
    line('Team yellow cards','cards10','**A team\'s own card history** predicts its cards.'),
    line('Team yellow cards','o_rank','**Table position and cards:** lower-placed sides, and sides facing a stronger opponent, collect more cards.'),'']
o+=['## Combined models (all factors together), out of sample','','| Outcome | Factors | Train / test matches | OOS gain ×10⁻⁴ | Typical move | Does the move come true? (test set: model multiplier → actual/baseline, by quintile) |','|---|---|---|---|---|---|']
for t,c in combo_out.items():
    qs=' · '.join(f"{a:.2f}→{b:.2f}" for a,b,_ in c['qt'])
    o.append(f"| {LAB[t]} | {', '.join(COMBO[t])} | {c['n_tr']:,} / {c['n_te']:,} | {c['gain']*1e4:+.2f} | ±{c['sd_move']*100:.1f}% | {qs} |")
o+=['','Coefficients (rate multiplier per 1 SD, t-stat, fitted on the training period):','']
for t,c in combo_out.items():
    o.append(f"- **{LAB[t]}**: "+'; '.join(f"{N.get(k,k)} {pct(m)} (t={tt:+.1f})" for k,(m,tt) in c['coef'].items()))
o+=['','## Quintile tables (all seasons): factor level → average outcome → actual vs baseline expectation','',
    'Actual/expected = 1.00 means the price/baseline already accounts for that factor level.','']
for (t,fe),qt in Q.items():
    nm={'y_g':'team goals scored','y_gc':'team goals conceded','y_c':'team corners won','y_cc':'team corners conceded','y_y':'team yellow cards'}[t]
    o.append(f"**{N.get(fe,fe)} → {nm}**: "+' | '.join(f"Q{i+1}: {a:.2f} → {m:.2f} ({rr:.3f})" for i,(a,m,rr,n) in enumerate(qt)))
    o.append('')
o+=['## Full table (each factor on its own)','','| Outcome | Factor | n | Corr | Raw / SD | t | Beyond price / SD | t | OOS ×10⁻⁴ | Verdict |','|---|---|---|---|---|---|---|---|---|---|']
for x in res:
    o.append(f"| {x['target']} | {N.get(x['feat'],x['feat'])} | {x['n']:,} | {x['corr']:+.3f} | {pct(x['raw'])} | {x['raw_t']:+.1f} | {pct(x['mkt'])} | {x['mkt_t']:+.1f} | {oo(x)} | {verdict(x)} |")
o+=['','## US sports: does recent form beat the closing line?','','Residual = actual − closing line (total points/runs, or home margin + spread). Slope = points/runs per 1 SD of the factor. A real edge needs |t|>2 **and** the same sign in both halves. MLB "margin" rows use the ±1.5 run line, which is not a margin forecast, so treat them as uninformative. Average residuals ignore the over/under juice, which ESPN does not store.','',
    '| Sport | Target | Factor | n | Slope | t | Early half | Late half | Avg residual |','|---|---|---|---|---|---|---|---|---|']
NM={'ovr_sum':'both teams\' recent totals vs line','b2b_any':'either team on a back-to-back','ats_diff':'recent results vs spread (home − away)','mar_diff':'recent margin (home − away)','rest_diff':'rest days (home − away)'}
for s,dd in US.items():
    for (tg,nm),v in dd.items():
        o.append(f"| {s.upper()} | {'total' if tg=='res_T' else 'margin'} | {NM[nm]} | {v['n']:,} | {v['slope']:+.2f} | {v['t']:+.1f} | {v['early']:+.2f} | {v['late']:+.2f} | {v['bias']:+.2f} |")
open('../papertrade/FACTORS.md','w').write('\n'.join(o)+'\n')
print('\n'.join(o[:60]))
for t,c in combo_out.items(): print(t,c['gain']*1e4,c['qt'])
for s,dd in US.items():
    for k,v in dd.items(): print(s,k,{a:round(b,3) for a,b in v.items()})
