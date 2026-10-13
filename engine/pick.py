# Ticket builder on the v8 win-probability model. Ranks every leg by the probability it comes through (research-adjusted,
# push/void branches counted as survival) per unit of odds it adds, then fills nested tickets to the targets.
# Usage: python3 pick.py 500 5000 50000  -> cache/tickets.json  (reads cache/winmodel_legs.json)
import json,sys,math,collections,os,re
legs=json.load(open('cache/winmodel_legs.json'))
# Oct 13 calibration: never let a model-vs-house disagreement make a leg look safer. For two-way non-integer lines,
# the selection probability is min(model p, house devigged p) — stops the picker favouring legs where the model is
# simply more optimistic than the book (winner's curse; the losing legs carried the larger optimistic gaps).
_G=collections.defaultdict(list)
for x in legs: _G[(x['eid'],x['mid'],x['spec'])].append(x)
for k,g in _G.items():
    if len(g)==2 and all(x.get('pp',0)==0 for x in g):
        s=sum(1/x['odds'] for x in g)
        for x in g: x['p_model']=x['p']; x['p']=min(x['p'],(1/x['odds'])/s)
TARGETS=[float(x) for x in sys.argv[1:]] or [500,5000,50000]
PMIN=0.65; KOMIN=os.environ.get('KOMIN','10-13 11:00')
JUNK=re.compile(r'women|\bw\b|u1[0-9]|u2[0-3]|youth|reserve|srl|friendl',re.I)
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
    if x['veto'] or 'data_conflict' in f or 'women_or_youth' in f or JUNK.search(x['lg']+' '+x['fx']): return False
    if not (1.18<=x['odds']<=2.2): return False
    if x['p']+x.get('pp',0)<PMIN or x['ko']<KOMIN: return False
    if x['sport']=='football':
        if m not in OK_FB: return False
        if m=='10' and d=='Home or Away': return False                        # no-draw DC (L2/L54)
        if m=='1' and p<0.62: return False
        if m in('450001','450002','450003') and p<0.80: return False        # capped bounds burned in thin leagues (Oct 7)
        amateur=any(k in x['lg'] for k in('Amateur','Reserve','Regional'))
        if amateur and (d.startswith('Under') or m in('450001','450002','450003')): return False   # amateur routs (Oct 13: 0/3)
        if m=='16' and '+' in d and float(d.split('+')[1].rstrip(')'))>=2.5 and x.get('fav_p',0)>=0.70: return False  # L70 rout class
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
FLOOR={500:1.20,600:1.20,5000:1.20,50000:1.22}
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
        if s in('under','over') and (sd[s]+1)/n>0.40 and n>4: continue
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
