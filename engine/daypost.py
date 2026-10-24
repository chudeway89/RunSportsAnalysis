# ONE-RUN DAY BUILD, step 2 of 2 (step 1 = daypack.sh). After the research agents have written cache/factors<D>_G*.json:
#   merge research over autoform -> re-price every leg (winmodel adj) -> MAIN core + nested ladder (pick.py) ->
#   post every ticket, verify leg identity, append codes to papertrade/tickets.txt, write papertrade/<date>_tickets.md
# Usage: [POST=1] [SCREEN='cache/r<tag>_G*.json'] KOMIN='MM-DD HH:MM' python3 daypost.py <YYYYMMDD-tag e.g. 24> <board.json> [targets...]   (default 500 5000 50000 max)
import json,glob,math,os,sys,subprocess,datetime as dt,collections
from post_lib import curl_post,curl_get
tag,bf=sys.argv[1],sys.argv[2]; targets=sys.argv[3:] or ['500','5000','50000','max']
auto={a['eid']:a for a in json.load(open(f'cache/auto{tag}.json'))}
SCR={x['eid'] for f in glob.glob(os.environ.get('SCREEN','__none__')) for x in json.load(open(f))}
res={}
for f in sorted(glob.glob(f'cache/factors{tag}_G*.json')):
    try:
        for r in json.load(open(f)): res[r['eid']]=r
    except Exception as ex: print('bad research file',f,ex)
out=[]
for eid,a in auto.items():
    r=res.get(eid)
    if r:
        m=dict(a,**{k:v for k,v in r.items() if v is not None}); m['flags']=sorted(set(r.get('flags') or [])|set(a.get('flags') or [])); m['researched']=True
    elif eid in SCR:   # screened: data-rich league, searched with no adverse news -> house price trusted (v5), conf 0.2
        m=dict(a); m['confidence']=max(a.get('confidence',0),0.2); m['flags']=sorted(set(a.get('flags') or [])|{'screened'}); m['researched']=False
    else: m=dict(a); m['researched']=False
    out.append(m)
json.dump(out,open(f'cache/factors_all_{tag}.json','w'))
print('merged',len(out),'researched',sum(o['researched'] for o in out))
subprocess.run(['python3','-W','ignore','winmodel.py','adj',bf,f'cache/factors_all_{tag}.json'],check=True)
# MAIN core: researched legs only (conf>=0.25), each wins OUTRIGHT at p>=0.72 (ledger winning shape) (refunds don't count), 1.25-1.85, one per fixture/country
L=json.load(open('cache/winmodel_legs.json'))
sys.argv=['pick.py','5']; KO=os.environ.get('KOMIN') or dt.datetime.utcnow().strftime('%m-%d %H:%M')
import importlib.util
spec=importlib.util.spec_from_file_location('pk','pick.py'); pk=importlib.util.module_from_spec(spec)
_stdout=sys.stdout; sys.stdout=open(os.devnull,'w'); spec.loader.exec_module(pk); sys.stdout=_stdout   # reuse every pick.py gate
cand=[x for x in pk.OK if x['conf']>=0.25 and x['p']>=0.72 and 1.25<=x['odds']<=1.85 and x['mid'] not in('450001','450002','450003')]
cand.sort(key=lambda x:-(x['p']*x['odds']))   # best value at a high strike rate
MAIN=[]; cc=collections.Counter(); und=0
for x in cand:
    if any(y['eid']==x['eid'] for y in MAIN) or cc[pk.country(x)]>=1: continue
    if pk.side(x)=='under':
        if und>=1: continue
        und+=1
    MAIN.append(x); cc[pk.country(x)]+=1
    if len(MAIN)==5: break
excl=f'cache/excl{tag}.json'; json.dump([x['eid'] for x in MAIN],open(excl,'w'))
tg=[t if t!='max' else '1e12' for t in targets]
subprocess.run(['python3','-W','ignore','pick.py',*tg],check=True,env=dict(os.environ,EXCLUDE=excl,KOMIN=KO),stdout=subprocess.DEVNULL)
T=json.load(open('cache/tickets.json'))
tickets={'MAIN':MAIN}
for t in targets: tickets[('T'+t) if t!='max' else 'MAX']=T[str(int(float(t if t!='max' else '1e12')))]['legs']
def sel(l):
    s={'eventId':l['eid'],'marketId':l['mid'],'outcomeId':l['oid'],'productId':3,'sportId':l['sid']}
    if l.get('spec'): s['specifier']=l['spec']
    return s
K=lambda s:(s['eventId'],str(s['marketId']),s.get('specifier') or '',str(s['outcomeId']))
day=dt.datetime.utcnow().strftime('%Y-%m-%d'); md=[f'# Tickets {day}','']; codes={}
POST=os.environ.get('POST')=='1'
for name,LL in tickets.items():
    if not LL: print(name,'EMPTY'); continue
    if not POST:
        O=math.prod(l['odds'] for l in LL); P=math.prod(l['p']+l.get('pp',0) for l in LL)
        print(f'DRY {name}: {len(LL)} legs {O:,.1f}x survive 1 in {1/P:,.0f}')
        for l in LL: print('   ',l['ko'],l['lg'][:24],'|',l['fx'][:38],'|',l.get('mdesc'),l.get('spec') or '',l['desc'],l['odds'],round(l['p'],2),'R' if l['conf']>=0.3 else 's' if l['conf']>=0.2 else 'a')
        continue
    d=curl_post({'selections':[sel(l) for l in LL],'stake':100,'orderType':1}); code=(d.get('data') or {}).get('shareCode')
    v=curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}').get('data') if code else {}
    vs=(v or {}).get('ticket',{}).get('selections',[])
    ok={K(sel(l)) for l in LL}=={K(s) for s in vs}
    O=math.prod(l['odds'] for l in LL); P=math.prod(l['p']+l.get('pp',0) for l in LL); Pw=math.prod(l['p'] for l in LL)
    codes[name]=dict(code=code,legs=len(LL),odds=O,p=P,pw=Pw,identity=ok)
    print(f"{name}: {code} legs {len(LL)} (booked {len(vs)}) odds {O:,.1f} survive 1 in {1/P:,.1f} all-win 1 in {1/Pw:,.1f} identity {ok}")
    md+=[f'## {name} — {code} · {len(LL)} legs · {O:,.1f}x · model win chance 1 in {1/P:,.0f} (all legs winning outright 1 in {1/Pw:,.0f}) · identity {"OK" if ok else "MISMATCH"}','',
         '| KO (UTC) | Fixture | League | Market | Pick | Odds | p | Research |','|---|---|---|---|---|---|---|---|']
    md+=[f"| {l['ko']} | {l['fx']} | {l['lg']} | {l.get('mdesc','')} {l.get('spec') or ''} | {l['desc']} | {l['odds']} | {l['p']:.2f} | {'yes' if l['conf']>=0.25 else 'screened' if l['conf']>=0.2 else 'auto'} |" for l in LL]+['']
    if code and ok:
        with open('../papertrade/tickets.txt','a') as f: f.write(f"{code}  {day}  {name} {len(LL)} legs {O:,.0f}x\n")
if POST:
  json.dump(codes,open(f'cache/codes{tag}.json','w'),indent=1)
  open(f'../papertrade/{day}_tickets.md','w').write('\n'.join(md)+'\n'); print('wrote',f'papertrade/{day}_tickets.md')
