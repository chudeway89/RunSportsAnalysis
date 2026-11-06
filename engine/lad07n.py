import json,math,re,collections,numpy as np,datetime as dt
L=json.load(open('cache/fixsim07n.json'))
THIN=re.compile(r'Montenegro|Dominican|Israel / National|Regionalliga|Saudi Arabia / Second|Kenya|Mali|Algeria|Vietnam|Kuwait|Cymru|Wales|Northern Ireland|Austria / 2|Egypt|Nigeria|Ghana|Morocco|Tanzania|Ethiopia|Thailand|Indonesia|Malaysia|Myanmar|Cambodia|Tunisia|Libya|Sudan|Cameroon|Zimbabwe|Mozambique|Angola|South Africa|Belarus|Armenia|Georgia|Albania|Bosnia|North Macedonia|Moldova|Latvia|Lithuania|Iceland|Faroe|Malta|Gibraltar|San Marino|Andorra|Luxembourg|Liga Premier|Primera B|Primera C|Federal|Reserv|U19|U20|U21|U23|NCAA|WNBL|LIDOM|LVBP|Pacifico|Puerto Rico|Estonia|Finland|Juniori|Lebanon|Liga Argentina|Ligue 3|Liga 2|Liga Alef|Kosovo|Botswana|Senegal|Ivory|Zambia|Oman|Bahrain|Iraq|Jordan|Qatar|Azerbaijan|El Salvador|Honduras|SAFF|Bangalore|India|Iran|Uzbek|Copa|Cup|Australian Championship|Uganda|Rwanda|Hong Kong|Venezuela|NKL|AFC|Expansion|Paraguay|Women|Torneo DIMAYOR|Costa Rica|Panam|Guatemala|New Zealand|K3|Football League|J3|W League|WNBL|Dominican|Australian Championship',re.I)
now=dt.datetime.utcnow()
def kot(x): return dt.datetime.strptime('2026-'+x['ko'],'%Y-%m-%d %H:%M')
FRAG=set(); DF=['Sacramento Kings','Charlotte Hornets','CA Independiente Avellaneda','Union de Santa Fe','San Lorenzo de Almagro','Auckland FC','Fortaleza FC','Los Angeles Lakers','Boyaca']; EX=set(json.load(open('cache/excl07n.json')))  # fragile favourite: no result-side
def ok(x):
    if x['eid'] in EX or any(k in x['fx'] for k in DF) or THIN.search(x['lg']) or x.get('veto') or (kot(x)-now).total_seconds()<40*60: return False
    o,p=x['odds'],x['sim']; m,d,sp=x['mid'],x['desc'],x['spec'] or ''
    if not(1.18<=o<=2.4) or p<0.60 or p*o<0.93: return False
    fl=set(x.get('flags',[])); res=m in('1','11','16','219','223')
    if res and (fl&{'derby','rotation_risk'} or x['fx'] in FRAG or 'season_opener' in fl): return False
    if m in('10','29','50','450001','450002','450003') or 'Multi' in x.get('mdesc',''): return False
    if m in('18','19','20') and re.search(r'=\d+$',sp): return False      # integer O/U
    if re.search(r'\.(25|75)$',sp): return False
    if m=='20' and d.startswith('Over'): return False
    under='Under' in d
    if under and p<0.82: return False
    if fl&{'big_club','derby'} and m in('18','19','20','225') and p<0.82: return False
    if x['sport']=='football':
        if m=='16':
            hc=float(sp.split('=')[1]); mine=hc if d.startswith('Home') else -hc
            if mine>=2.5 and x.get('fav_p',0)>=0.60: return False
            if mine>=1.5 and x.get('fav_p',0)>=0.55 and p<0.80: return False
            if mine<0 and d.startswith('Away') and p<0.75: return False
        if m=='1' and d=='Away' and p<0.75: return False
    if x['sport']=='basketball':
        if m=='223' and abs(float(sp.split('=')[1]))<8.5: return False
        if m=='219' and p<0.75: return False
        if m=='225' and p<0.74: return False
    return True
P=[x for x in L if ok(x)]
cost=lambda x:-math.log(x['sim'])/math.log(x['odds'])
P.sort(key=cost)
def ctry(x): return x['lg'].split(' / ')[0] if 'International' not in x['lg'] else x['lg']
def side(x): return 'under' if 'Under' in x['desc'] else ('over' if 'Over' in x['desc'] else 'res')
def build(tgt,cap):
    T=[];cc=collections.Counter();n=collections.Counter();lo=0
    for x in P:
        if lo>=math.log(tgt): break
        if any(y['eid']==x['eid'] for y in T) or cc[ctry(x)]>=cap: continue
        s=side(x)
        if s!='res' and n[s]+1>0.4*max(len(T)+1,5): continue
        T.append(x);cc[ctry(x)]+=1;n[s]+=1;lo+=math.log(x['odds'])
    while True:
        od=math.prod(y['odds'] for y in T);c=[y for y in sorted(T,key=cost,reverse=True) if od/y['odds']>=tgt]
        if not c:break
        T.remove(c[0])
    return T
# joint sim with shared environment
N=100000;rng=np.random.default_rng(5)
B={b['eid']:b for b in json.load(open('cache/baseline.json'))}
import importlib.util,sys
spec=importlib.util.spec_from_file_location('fs','fixsim.py')
src=open('fixsim.py').read().split('G=collections.defaultdict')[0]
exec(src.replace("L=json.load(open('cache/winmodel_legs.json')); BASE={b['eid']:b for b in json.load(open(sys.argv[1]))}","BASE=B"))
def joint(T):
    surv=np.ones(N,bool);allw=np.ones(N,bool);g=rng.normal(0,0.06,N);comp={}
    for x in T:
        if x['sport']=='football':
            c=comp.setdefault(x['lg'],rng.normal(0,0.08,N));lh,la=x['lam'];k=np.exp(g+c)
            dr=(rng.poisson(lh*k),rng.poisson(la*k))
        else:
            c=comp.setdefault(x['lg'],rng.normal(0,3,N));b=B[x['eid']]
            dr=(rng.normal(x['mu'][0],b['sdT'],N)+c,rng.normal(x['mu'][1],b['sdM'],N))
        r=settle(x,dr);surv&=r>=0;allw&=r==1
    return surv.mean(),allw.mean()
out={}
for tgt,cap in((100,4),):
    T=build(tgt,cap);od=math.prod(x['odds'] for x in T);s,a=joint(T)
    print(f'\n=== T{tgt}: {len(T)} legs {od:,.0f}x | joint 100k survive 1 in {1/s:,.0f} (indep 1 in {1/math.prod(x["sim"] for x in T):,.0f})')
    for x in sorted(T,key=lambda x:x['ko']): print(f"  {x['ko']} {x['lg'][-22:]:22} {x['fx'][:40]:40} {x['mdesc'][:22]:22} {x['desc'][:16]:16} @{x['odds']:.2f} sim{x['sim']:.3f}")
    out[tgt]=T
json.dump(out,open('/tmp/claude-0/-home-user-gsley/b526d9c8-57a7-5192-8f65-9a58ec7e9e11/scratchpad/lad07n.json','w'))
print('pool',len(P))
