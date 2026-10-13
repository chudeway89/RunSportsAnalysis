# WIN-PROBABILITY MODEL (v8, Oct 13). Selection is driven by P(this market in this fixture comes through), not by
# model-vs-house EV. Each fixture's probability starts from the calibrated market-anchored base and is then moved by
# researched fixture factors (form, home/away splits, H2H, team news, league averages, stage/motivation), through ONE
# blend weight that the paper-trade grader will refit over time.
#
#  football:   base lambdas (lh, la) from devigged 1X2 + O/U 2.5 (anc.fit). Research returns its own expected goals
#              (rh, ra) and a confidence c in [0,1]. Adjusted lambda = l * (r/l)^(W*c), ratio clamped to [0.80, 1.25].
#              Every market on the fixture is then re-priced from the adjusted score grid, so a factor that says
#              "home attack depleted" moves the 1X2, DNB, AH, totals, team totals and bounds consistently.
#  basketball: base total/margin from the house ladders, SD from the house's own ladder (the grader showed the house
#              SD beats ours). Adjusted mean = base + W*c*(research - base), clamped to +/-6 pts (total), +/-5 (margin).
#  W = 0.35. Why not 1.0: on 54k matches an independent stat model LOST to the closing price (System Review v5), and
#  research verdicts were only reliable at the extremes (L78). Why not 0: named, checkable facts (absences, rotation,
#  must-win/dead-rubber) do move outcomes and the market can be stale on them. 0.35 is the prior; grade.py refits it.
#
#  Usage: python3 winmodel.py base  <board.json> <fixture_list.json>   -> cache/baseline.json  (what research sees)
#         python3 winmodel.py price <board.json> <factors.json>        -> cache/winmodel_legs.json
import json,sys,math,statistics,numpy as np
from scipy.stats import norm
from anc import fit,grid,devig,L,J,K
import price as _p   # reuse the exact settlement logic (price.price) — price.py is import-safe below
W=0.35
I=np.arange(K)[:,None]; Jx=np.arange(K)[None,:]
def g(mk,mid,spec,desc): return [o['odds'] for o in mk if o['mid']==mid and (o['spec'] or None)==spec and o['desc']==desc]
def fb_base(e):
    mk=e['mk']; h,d,a=g(mk,'1',None,'Home'),g(mk,'1',None,'Draw'),g(mk,'1',None,'Away')
    ov,un=g(mk,'18','total=2.5','Over 2.5'),g(mk,'18','total=2.5','Under 2.5')
    if not(h and d and a): return None
    pH,pD,pA=devig(h[0],d[0],a[0]); pO=devig(ov[0],un[0])[0] if ov and un else None
    ia,ib=fit(pH,pD,pA,pO)
    return dict(lh=float(L[ia]),la=float(L[ib]),pH=pH,pD=pD,pA=pA,pO25=pO)
def nearest(x): return int(np.argmin(np.abs(L-x)))
def bk_base(e):
    from live_sports import ladder,centre,house_sd,two_way
    T=ladder(e,'225','Over','Under'); H=ladder(e,'223','Home','Away')
    if not T: return None
    muT=centre(T,17.5); sdT=house_sd(T,muT) or 17.5; muT=centre(T,sdT)
    sdM=sdT*0.78
    if H: v,p,_,_=min(H,key=lambda x:abs(x[1]-0.5)); muM=sdM*norm.ppf(min(max(p,1e-3),1-1e-3))-v
    elif two_way(e,'219'): muM=sdM*norm.ppf(two_way(e,'219'))
    else: return None
    return dict(muT=muT,sdT=sdT,muM=muM,sdM=sdM)
def price_fb(e,lh,la):
    P=J[nearest(lh),nearest(la)]; out=[]
    for o in e['mk']:
        r=_p.price(P,o)
        if r: out.append((o,r[0],r[1]))
    return out
def price_bk(e,b):
    from live_sports import ladder
    out=[]
    for v,p,oa,ob in ladder(e,'225','Over','Under'):
        po=1-norm.cdf((v-b['muT'])/b['sdT']); out+= [(oa,po,0.0),(ob,1-po,0.0)]
    for v,p,oa,ob in ladder(e,'223','Home','Away'):
        ph=norm.cdf((b['muM']+v)/b['sdM']); out+= [(oa,ph,0.0),(ob,1-ph,0.0)]
    for o in e['mk']:
        if o['mid']=='219': pm=norm.cdf(b['muM']/b['sdM']); out.append((o,pm if o['desc']=='Home' else 1-pm,0.0))
    return out
if __name__=='__main__':
    mode,bf,xf=sys.argv[1:4]; B={e['eid']:e for e in json.load(open(bf))}
    if mode=='base':
        res=[]
        for f in json.load(open(xf)):
            e=B.get(f['eid'])
            if not e: continue
            b=fb_base(e) if e['sport']=='football' else bk_base(e) if e['sport']=='basketball' else None
            if b: res.append(dict(f,**{k:(round(v,3) if isinstance(v,float) else v) for k,v in b.items()}))
        json.dump(res,open('cache/baseline.json','w'),indent=0); print('baselines',len(res))
    else:
        F={f['eid']:f for f in json.load(open(xf))}; out=[]
        for eid,f in F.items():
            e=B.get(eid)
            if not e: continue
            c=max(0.0,min(1.0,float(f.get('confidence',0) or 0)))
            if e['sport']=='football':
                b=fb_base(e)
                if not b: continue
                def adj(l,r):
                    if not r: return l
                    ratio=min(1.25,max(0.80,r/l)); return l*ratio**(W*c)
                lh,la=adj(b['lh'],f.get('xg_h')),adj(b['la'],f.get('xg_a'))
                base={id(o):(pw,pp) for o,pw,pp in price_fb(e,b['lh'],b['la'])}
                for o,pw,pp in price_fb(e,lh,la):
                    bw,bp=base.get(id(o),(pw,pp))
                    out.append(dict(eid=eid,sid=e['sid'],sport='football',lg=e['lg'],fx=e['fx'],ko=e['ko'],mid=o['mid'],spec=o['spec'],desc=o['desc'],
                        mdesc=o['mdesc'],oid=o['oid'],odds=o['odds'],p_base=round(bw,4),p=round(pw,4),pp=round(pp,4),flags=f.get('flags',[]),veto=bool(f.get('veto')),
                        lam=(round(lh,2),round(la,2)),lam0=(round(b['lh'],2),round(b['la'],2)),conf=c,fav_p=round(max(b['pH'],b['pA']),3)))
            elif e['sport']=='basketball':
                b=bk_base(e)
                if not b: continue
                b2=dict(b)
                if f.get('total'): b2['muT']=b['muT']+max(-6,min(6,W*c*(f['total']-b['muT'])))
                if f.get('margin') is not None: b2['muM']=b['muM']+max(-5,min(5,W*c*(f['margin']-b['muM'])))
                base={id(o):pw for o,pw,_ in price_bk(e,b)}
                for o,pw,pp in price_bk(e,b2):
                    out.append(dict(eid=eid,sid=e['sid'],sport='basketball',lg=e['lg'],fx=e['fx'],ko=e['ko'],mid=o['mid'],spec=o['spec'],desc=o['desc'],
                        mdesc=o.get('mdesc',''),oid=o['oid'],odds=o['odds'],p_base=round(base.get(id(o),pw),4),p=round(pw,4),pp=0.0,flags=f.get('flags',[]),
                        veto=bool(f.get('veto')),mu=(round(b2['muT'],1),round(b2['muM'],1)),mu0=(round(b['muT'],1),round(b['muM'],1)),conf=c))
        json.dump(out,open('cache/winmodel_legs.json','w')); print('legs',len(out),'fixtures',len(set(x['eid'] for x in out)))
