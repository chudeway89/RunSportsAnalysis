# THE LEARNING LOOP (runs every night after tape_grade.py; no LLM needed).
# One streaming pass over the graded tape (every market on every fixture, cache/tape_graded/) answers three questions
# and writes what it learned where the ticket builder reads it:
#   1. CALIBRATION  where does SportyBet's own probability miss?  -> shrunken corrections per sport x market x side x odds band
#   2. FORM         did the automated data research (papertrade/form/: last-10 trend per market, stored BEFORE kick-off)
#                   know anything the price did not?               -> blend weight b in  p = house + b * (trend - house)
#   3. RESEARCH     how did our web research (papertrade/research/: picks, vetoes) do against results?
# Outputs: papertrade/learned.json (machine), papertrade/LEARNED.md (human), one line per run in papertrade/learning_log.jsonl
# Guards against fooling ourselves: SE clustered by fixture, a correction must hold in both halves of the period and
# clear |z| >= 3, and it is shrunk towards zero by sample size. Nothing is "learned" from noise.
import json,math,os,re,glob,gzip,csv,collections,datetime as dt
from tapelib import iter_graded,part_days,file_date,HERE
PT=os.path.join(HERE,'..','papertrade')
K_SHRINK=1500      # fixtures needed before a correction is trusted at half strength
from learn_keys import band,side
class Acc:
    """Residual (won - house p) and flat ROI for one slice, with fixture-clustered SE (rows arrive grouped by fixture)."""
    __slots__=('n','res','pnl','k','c2','_e','_s')
    def __init__(s): s.n=s.res=s.pnl=s.k=s.c2=0.0; s._e=None; s._s=0.0
    def add(s,eid,resid,pnl):
        if eid!=s._e:
            s.c2+=s._s*s._s; s._s=0.0; s._e=eid; s.k+=1
        s.n+=1; s.res+=resid; s.pnl+=pnl; s._s+=resid
    def out(s):
        if not s.n: return None
        c2=s.c2+s._s*s._s; mean=s.res/s.n
        se=math.sqrt(max(c2-s.k*(s.res/s.k)**2,0.0))/s.n if s.k>1 else 9.0     # cluster-robust SE of the mean residual
        return dict(n=int(s.n),fx=int(s.k),resid=mean,se=se or 9.0,z=mean/(se or 9.0),roi=s.pnl/s.n)
# ---- inputs that were fixed BEFORE kick-off
FORM_FILES=sorted(glob.glob(os.path.join(PT,'form','*.csv.gz')),key=os.path.basename)
def form_for(day,cache={}):
    """Predictions stored up to 3 days before this kick-off day (earliest prediction wins); older files are dropped."""
    lo=(dt.date.fromisoformat(day)-dt.timedelta(days=3)).isoformat()
    for f in [f for f in cache if not lo<=file_date(f)<=day]: del cache[f]
    for f in FORM_FILES:
        if lo<=file_date(f)<=day and f not in cache:
            d={}
            with gzip.open(f,'rt') as g:
                for r in csv.reader(g):
                    try: d[(r[0],r[1],r[2],r[3])]=float(r[6])
                    except Exception: pass
            cache[f]=d
    return [cache[f] for f in sorted(cache,key=os.path.basename)]
PICK={}; VETO=set(); SEEN=set()
for f in glob.glob(os.path.join(PT,'research','*.json')):
    try: J=json.load(open(f))
    except Exception: continue
    for x in (J if isinstance(J,list) else [J]):
        if not isinstance(x,dict) or not x.get('eid'): continue
        e=x['eid'] if str(x['eid']).startswith('sr:') else f"sr:match:{x['eid']}"; SEEN.add(e)
        if x.get('veto'): VETO.add(e)
        for p in x.get('picks') or []:
            if isinstance(p,dict): PICK[(e,str(p.get('mid')),p.get('spec') or '',p.get('desc'))]=True
# ---- one pass
days=part_days(); half=days[len(days)//2] if days else ''
CAL=collections.defaultdict(lambda:[Acc(),Acc(),Acc()])
FB=collections.defaultdict(lambda:dict(n=0,sxy=0.0,sxx=0.0,k=0,c2=0.0,_e=None,_s=0.0)); FBIN=collections.defaultdict(Acc)
RS=collections.defaultdict(Acc); tot=0
MAIN={'1','10','11','16','18','29','219','223','225'}
for d in days:
    forms=form_for(d) if FORM_FILES else []
    h=1 if d<half else 2
    for r in iter_graded([d]):
        hp=r.get('hp')
        if not hp or r['res'] not in ('W','L','Q'): continue
        y=1.0 if r['res']=='W' else 0.0 if r['res']=='L' else (1.0 if r['ret']>1 else 0.0 if r['ret']<1 else 0.5)
        resid=y-hp; pnl=r['ret']-1; eid=r['eid']; tot+=1
        t=CAL[(r['sport'],r['mid'],(r.get('mdesc') or '')[:40],side(r),band(r['odds']))]
        t[0].add(eid,resid,pnl); t[h].add(eid,resid,pnl)
        if forms and 1.15<=r['odds']<=4:
            key=(eid,r['mid'],r.get('spec') or '',str(r.get('oid')))
            for fd in forms:
                tr=fd.get(key)
                if tr is not None:
                    gap=tr-hp; s=FB[r['sport']]
                    if eid!=s['_e']: s['c2']+=s['_s']**2; s['_s']=0.0; s['_e']=eid; s['k']+=1
                    s['n']+=1; s['sxy']+=gap*resid; s['sxx']+=gap*gap; s['_s']+=gap*resid
                    b='form 15pp+ below price' if gap<-0.15 else 'form 5-15pp below' if gap<-0.05 else 'form within 5pp' if gap<=0.05 else 'form 5-15pp above' if gap<=0.15 else 'form 15pp+ above price'
                    FBIN[(r['sport'],b)].add(eid,resid,pnl); FBIN[('all sports',b)].add(eid,resid,pnl)
                    break
        if eid in SEEN:
            if (eid,r['mid'],r.get('spec') or '',r['desc']) in PICK: RS['research picks'].add(eid,resid,pnl)
            if r['mid'] in MAIN and 1.18<=r['odds']<2.2:
                RS['vetoed fixtures: short-priced main markets' if eid in VETO else 'researched, not vetoed: same markets'].add(eid,resid,pnl)
# ---- 1. calibration corrections
cal={}; table=[]; tested=0
for k,t in CAL.items():
    a=t[0].out()
    if not a or a['fx']<150: continue
    tested+=1
    e,l=t[1].out(),t[2].out()
    stable=bool(e and l and (e['resid']>0)==(l['resid']>0)==(a['resid']>0))
    if stable and abs(a['z'])>=3:
        adj=a['resid']*a['fx']/(a['fx']+K_SHRINK)
        cal['|'.join(k)]=round(adj,4); table.append((k,a,e,l,adj))
table.sort(key=lambda x:-abs(x[1]['z']))
# ---- 2. form blend weight per sport
form={}
for sp,s in FB.items():
    if s['sxx']<=0 or s['k']<50: continue
    c2=s['c2']+s['_s']**2; b=s['sxy']/s['sxx']; se=math.sqrt(max(c2,1e-12))/s['sxx']
    form[sp]=dict(b=round(b,4),se=round(se,4),z=round(b/se,2) if se else 0,n=s['n'],fixtures=s['k'],
                  use=round(max(0.0,min(b,1.0))*s['k']/(s['k']+K_SHRINK),4) if se and b/se>=3 else 0.0)
now=dt.datetime.now(dt.timezone.utc)
L=dict(as_of=f'{now:%Y-%m-%d %H:%M} UTC',outcomes=tot,first=days[0] if days else None,last=days[-1] if days else None,
       calibration=cal,slices_tested=tested,form=form,research={k:v.out() for k,v in RS.items()})
json.dump(L,open(os.path.join(PT,'learned.json'),'w'),indent=1)
pp=lambda x:f'{100*x:+.1f}pp'
md=[f'# What the engine has learned (auto, {L["as_of"]})','',
    f'Rebuilt every night by `engine/learn.py` from **{tot:,} settled outcomes** on every market of every fixture ({L["first"]} to {L["last"]}). '
    'Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.','',
    f'## 1. Where the house probability misses ({len(table)} of {tested} slices; chance alone would give about {tested*0.0027:.1f})','',
    '| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |','|---|---|---|---|---|---|---|---|---|---|']
md+=[f"| {k[0]} | {k[2] or k[1]} | {k[3]} | {k[4]} | {a['fx']:,} | {pp(a['resid'])} | {a['z']:+.1f} | {pp(e['resid'])} / {pp(l['resid'])} | {100*a['roi']:+.1f}% | {pp(adj)} |" for k,a,e,l,adj in table[:40]] or ['| none yet | | | | | | | | | |']
md+=['','## 2. Did the automated form research beat the price?','',
     'Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.','',
     '| Sport | Outcomes | Fixtures | b | SE | z | Weight used |','|---|---|---|---|---|---|---|']
md+=[f"| {sp} | {v['n']:,} | {v['fixtures']:,} | {v['b']:+.3f} | {v['se']:.3f} | {v['z']:+.1f} | {v['use']:.3f} |" for sp,v in sorted(form.items(),key=lambda kv:-kv[1]['n'])] or ['| collecting (first predictions stored 2026-11-20) | | | | | | |']
md+=['','| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |','|---|---|---|---|---|---|---|']
for (sp,b),acc in sorted(FBIN.items()):
    a=acc.out()
    if a and a['fx']>=30: md.append(f"| {sp} | {b} | {a['n']:,} | {a['fx']:,} | {pp(a['resid'])} | {a['z']:+.1f} | {100*a['roi']:+.1f}% |")
md+=['','## 3. Our web research against results','','| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |','|---|---|---|---|---|---|']
for k,acc in RS.items():
    a=acc.out()
    if a: md.append(f"| {k} | {a['n']:,} | {a['fx']:,} | {pp(a['resid'])} | {a['z']:+.1f} | {100*a['roi']:+.1f}% |")
open(os.path.join(PT,'LEARNED.md'),'w').write('\n'.join(md)+'\n')
with open(os.path.join(PT,'learning_log.jsonl'),'a') as f:
    f.write(json.dumps(dict(date=f'{now:%Y-%m-%d %H:%M}',outcomes=tot,corrections=len(cal),slices=tested,form={k:[v['b'],v['z'],v['fixtures']] for k,v in form.items()},
                            research={k:[round(v.out()['resid'],4),v.out()['fx']] for k,v in RS.items() if v.out()}))+'\n')
print('\n'.join(md[:60]))
