# Live pricing of SportyBet basketball & baseball markets.
# Basketball: normal around the house's own main line (centre), with OUR spread: NBA/WNBA measured vs closing lines,
#   other leagues = team-model SD x market/model ratio (hoops_sr.py). Markets: 219 winner, 223 handicap, 225 total, 227/228 team totals.
# Baseball: empirical MLB logistic tables (mlb_emp.py) anchored on main total line + devigged moneyline. Markets: 251, 256, 258.
# Usage: python3 live_sports.py cache/board_<date>.json  -> cache/priced_sports.json  (+ house-implied SD vs ours)
import json,sys,math,statistics
from scipy.stats import norm
from mlb_emp import p_total_over,p_fav_cover
U=json.load(open('coef_hoops_us.json')); S=json.load(open('coef_hoops_sr.json')); C=json.load(open('coef_mlb_emp.json'))
BYNAME={v['name']:v for v in S.values()}
def spec_val(s):
    try: return float(s.split('=')[1])
    except Exception: return None
def ladder(e,mid,a,b):
    """list of (line, pA_devig, oddsA, oddsB) for a 2-way ladder"""
    L={}
    for o in e['mk']:
        if o['mid']!=mid: continue
        v=spec_val(o['spec'] or '')
        if v is None: continue
        L.setdefault(v,{})[o['desc'].split(' ')[0]]=o
    out=[]
    for v,d in sorted(L.items()):
        if a in d and b in d:
            qa,qb=1/d[a]['odds'],1/d[b]['odds']; out.append((v,qa/(qa+qb),d[a],d[b]))
    return out
def centre(lad,sd,sign=1):
    if not lad: return None
    v,p,_,_=min(lad,key=lambda x:abs(x[1]-0.5))
    return v+sign*sd*norm.ppf(min(max(p,1e-3),1-1e-3))
def house_sd(lad,mu):
    xs=[(v-mu)/norm.ppf(1-p) for v,p,_,_ in lad if 0.08<p<0.92 and abs(v-mu)>3]
    return statistics.median(xs) if xs else None
def two_way(e,mid):
    q={o['desc']:1/o['odds'] for o in e['mk'] if o['mid']==mid}
    if 'Home' in q and 'Away' in q: return q['Home']/(q['Home']+q['Away'])
if __name__=='__main__':
    B=json.load(open(sys.argv[1])); out=[]; sdcmp=[]
    for e in B:
        if e['sport']=='basketball':
            lgn=e['lg']
            if 'NBA' in lgn and 'USA' in lgn: sdT,sdM,src=U['nba']['sdT'],U['nba']['sdM'],'nba-closing'
            elif 'WNBA' in lgn: sdT,sdM,src=U['wnba']['sdT'],U['wnba']['sdM'],'wnba-closing'
            elif lgn in BYNAME: sdT,sdM,src=BYNAME[lgn]['sdT'],BYNAME[lgn]['sdM'],'sr-teammodel'
            else: sdT,sdM,src=16.5,13.0,'default'
            T=ladder(e,'225','Over','Under'); H=ladder(e,'223','Home','Away')
            muT=centre(T,sdT)
            # home margin: P(margin + h > 0)=Phi((mu+h)/sd) -> mu = sd*Phi^-1(p) - h
            muM=None
            if H:
                v,p,_,_=min(H,key=lambda x:abs(x[1]-0.5)); muM=sdM*norm.ppf(min(max(p,1e-3),1-1e-3))-v
            elif two_way(e,'219'): muM=sdM*norm.ppf(two_way(e,'219'))
            if muT is None or muM is None: continue
            hsT=house_sd(T,muT)
            if hsT: sdcmp.append((lgn,src,round(sdT,1),round(hsT,1)))
            for v,p,oa,ob in T:
                po=1-norm.cdf((v-muT)/sdT)
                for o,pm in ((oa,po),(ob,1-po)): out.append(dict(e=e,o=o,mp=pm,src=src,line=v))
            for v,p,oa,ob in H:
                ph=norm.cdf((muM+v)/sdM)
                for o,pm in ((oa,ph),(ob,1-ph)): out.append(dict(e=e,o=o,mp=pm,src=src,line=v))
            for o in e['mk']:
                if o['mid']=='219': pm=norm.cdf(muM/sdM); out.append(dict(e=e,o=o,mp=pm if o['desc']=='Home' else 1-pm,src=src,line=None))
            sdTeam=math.sqrt(sdT**2+sdM**2)/2
            for mid in ('227','228'):
                L=ladder(e,mid,'Over','Under'); mu=centre(L,sdTeam)
                for v,p,oa,ob in L:
                    po=1-norm.cdf((v-mu)/sdTeam)
                    for o,pm in ((oa,po),(ob,1-po)): out.append(dict(e=e,o=o,mp=pm,src=src,line=v))
        elif e['sport']=='baseball':
            src='mlb-closing' if 'MLB' in e['lg'] else 'mlb-tables-transfer'
            T=ladder(e,'258','Over','Under'); ph=two_way(e,'251')
            if not T or ph is None: continue
            ou=min(T,key=lambda x:abs(x[1]-0.5))[0]; pf=max(ph,1-ph); fav_home=ph>=0.5
            for v,p,oa,ob in T:
                po=p_total_over(C,ou,v)
                if po is None: continue
                for o,pm in ((oa,po),(ob,1-po)): out.append(dict(e=e,o=o,mp=pm,src=src,line=v))
            for v,p,oa,ob in ladder(e,'256','Home','Away'):
                if v==int(v): continue
                k=v if fav_home else -v           # handicap expressed for the favourite
                pc=p_fav_cover(C,pf,k)
                if pc is None: continue
                p_home=pc if fav_home else 1-pc
                for o,pm in ((oa,p_home),(ob,1-p_home)): out.append(dict(e=e,o=o,mp=pm,src=src,line=v))
            for o in e['mk']:
                if o['mid']=='251': out.append(dict(e=e,o=o,mp=ph if o['desc']=='Home' else 1-ph,src=src,line=None))
    R=[dict(eid=x['e']['eid'],sid=x['e']['sid'],sport=x['e']['sport'],lg=x['e']['lg'],fx=x['e']['fx'],ko=x['e']['ko'],mid=x['o']['mid'],spec=x['o']['spec'],
            desc=x['o']['desc'],oid=x['o']['oid'],odds=x['o']['odds'],hp=x['o']['p'],mp=x['mp'],ev=x['mp']*x['o']['odds'],src=x['src'],line=x['line']) for x in out]
    json.dump(R,open('cache/priced_sports.json','w'))
    print('priced',len(R),'outcomes on',len(set(r['eid'] for r in R)),'events')
    print('basketball SD (ours vs house-implied):'); [print('  ',*x) for x in sdcmp]
    for sp in ('basketball','baseball'):
        for mid in sorted(set(r['mid'] for r in R if r['sport']==sp)):
            v=[r['ev'] for r in R if r['sport']==sp and r['mid']==mid and 1.2<=r['odds']<=3]
            if v: print(sp,mid,'n',len(v),'mean EV %.3f'%statistics.mean(v),'EV>=1.03 share %.2f'%(sum(x>=1.03 for x in v)/len(v)))
