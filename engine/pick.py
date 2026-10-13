# Ticket builder on the v8 win-probability model. Ranks every leg by the probability it comes through (research-adjusted,
# push/void branches counted as survival) per unit of odds it adds, then fills nested tickets to the targets.
# Usage: python3 pick.py 500 5000 50000  -> cache/tickets.json  (reads cache/winmodel_legs.json)
import json,sys,math,collections
legs=json.load(open('cache/winmodel_legs.json'))
TARGETS=[float(x) for x in sys.argv[1:]] or [500,5000,50000]
RESULT={'1','10','11','16','219','223'}
OK_FB={'1','10','11','16','18','19','20','450001','450002','450003'}
OK_BK={'219','223','225'}
def country(x):
    lg=x['lg'].split(' / ')
    return lg[1] if lg[0].startswith('International') else lg[0]
def side(x):
    d=x['desc']
    if x['mid'] in('18','19','20','225') and d.startswith('Under'): return 'under'
    if x['mid'] in('18','19','20','225') and d.startswith('Over'): return 'over'
    return 'other'
def allowed(x):
    f=set(x['flags']); m=x['mid']; p=x['p']; d=x['desc']
    if x['veto'] or 'data_conflict' in f: return False
    if not (1.15<=x['odds']<=2.2): return False
    if x['sport']=='football':
        if m not in OK_FB: return False
        if m=='10' and d=='Home or Away': return False                        # no-draw DC (L2/L54)
        if m=='1' and p<0.62: return False
        if m in('450001','450002','450003') and p<0.80: return False        # capped bounds burned in thin leagues (Oct 7)
        if m in RESULT and ({'derby','season_opener'}&f): return False      # L60/L65
        if 'knockout_90min' in f and m in('1','16','10'): return False      # L56: only DNB/totals on knockouts
        if 'rotation_risk' in f and p<0.78: return False                    # L66
        if x['conf']<0.2 and p<0.78: return False                           # unresearched -> only near-locks
    else:
        if m not in OK_BK: return False
        if m=='223':
            h=abs(float(x['spec'].split('=')[1]))
            if h<8.5 and p<0.80: return False                               # close spreads (L52)
        if m=='225' and x['p']<0.70: return False
        if 'season_opener' in f and m in RESULT: return False
        if x['conf']<0.2 and p<0.78: return False
    return True
def cost(x):
    pw,pp=x['p'],x.get('pp',0); s=pw+pp
    if s<=0.5 or pw<=0: return 9
    return -math.log(s)/((pw*math.log(x['odds']))/s)
FLOOR={500:1.25,5000:1.30,50000:1.38}
OK=[x for x in legs if allowed(x)]
for x in OK: x['cost']=cost(x)
def mkpool(floor):
    best={}
    for x in OK:
        if x['odds']<floor: continue
        if x['eid'] not in best or x['cost']<best[x['eid']]['cost']: best[x['eid']]=x
    return sorted(best.values(),key=lambda x:x['cost'])
pool=mkpool(1.15)
def build(target,base=None,maxlegs=50):
    pool=mkpool(FLOOR.get(int(target),1.3))
    T=list(base or []); used={x['eid'] for x in T}
    cc=collections.Counter(country(x) for x in T); sd=collections.Counter(side(x) for x in T)
    def odds(L): return math.prod(x['odds'] for x in L)
    for x in pool:
        if odds(T)>=target or len(T)>=maxlegs: break
        if x['eid'] in used or cc[country(x)]>=3: continue
        n=len(T)+1; s=side(x)
        if s in('under','over') and (sd[s]+1)/n>0.45 and n>4: continue
        T.append(x); used.add(x['eid']); cc[country(x)]+=1; sd[s]+=1
    return T
out={}; base=None
for t in TARGETS:
    T=build(t,base); base=T
    P=math.prod(x['p']+x.get('pp',0) for x in T); Pw=math.prod(x['p'] for x in T); O=math.prod(x['odds'] for x in T)
    out[str(int(t))]=dict(legs=T,odds=O,p_survive=P,p_allwin=Pw)
    print(f"T{int(t)}: {len(T)} legs  odds {O:,.0f}  P(win incl refunds) 1 in {1/P:,.0f}   all-legs-win 1 in {1/Pw:,.0f}")
json.dump(out,open('cache/tickets.json','w'))
print('pool size',len(pool))
for x in pool[:70]:
    print(f"{x['cost']:.3f} {x['ko']} {x['sport'][:4]} {x['lg'][:28]:28} | {x['fx'][:36]:36} | {x.get('mdesc','')[:18]:18} {x['spec'] or ''} {x['desc']} @{x['odds']} p{x['p']:.3f} (base {x['p_base']:.3f}) c{x['conf']} {','.join(x['flags'])}")
