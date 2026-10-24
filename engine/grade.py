# Settle every paper-trade snapshot (papertrade/*_snapshot.json) against the Sportradar results feed and report
# per market: graded n, model vs house log-loss, hit-rate vs predicted, and ROI of model-EV>=1.05 picks (odds 1.2-3.0).
# Usage: python3 grade.py   -> appends papertrade/graded.jsonl, prints + writes papertrade/grade_report.txt
import json,glob,os,math,collections,datetime as dt
import sr
G='../papertrade/graded.jsonl'; done=set()
if os.path.exists(G): done={json.loads(l)['key'] for l in open(G)}
now=dt.datetime.utcnow()
def res(eid):
    m=sr.match_info(eid.split(':')[-1],maxage=3*3600)
    if not m or (m.get('result') or {}).get('home') is None: return None
    if m.get('canceled') or m.get('postponed'): return 'void'
    st=(m.get('status') or {}).get('name','')
    if st and st not in ('Ended','AET','AP','Ended after extra time','Ended after penalties','After overtime','AOT','Ended after overtime'): return None
    r=dict(hs=m['result']['home'],as_=m['result']['away'])
    if m.get('_doctype')=='soccer' or m.get('_sid')==1:
        p=(m.get('periods') or {}).get('ft') or {}
        if p.get('home') is not None: r.update(hs=p['home'],as_=p['away'])   # 90-minute score
        s=sr.match_stats(m['_id'])
        if not s: return None
        r.update(s)
    return r
def outcome(x,r):
    m,d,L=x['mid'],x['desc'],x.get('line')
    if L is None and x.get('spec') and '=' in x['spec']:
        try: L=float(x['spec'].split('=')[1])
        except Exception: pass
    hs,as_=r['hs'],r['as_']
    if m in ('166','900300','900301','139'):
        v={'166':r['hc']+r['ac'],'900300':r['hc'],'900301':r['ac'],'139':(r['hy'] or 0)+(r['ay'] or 0)+(r['hr'] or 0)+(r['ar'] or 0)}[m]
    elif m in ('225','258'): v=hs+as_
    elif m=='227': v=hs
    elif m=='228': v=as_
    elif m in ('219','251'): return (hs>as_) if d=='Home' else (as_>hs)
    elif m in ('223','256'):
        mg=hs-as_+L if d.startswith('Home') else as_-hs-L
        return None if mg==0 else mg>0
    else: return None
    if v==L: return None
    return v>L if d.startswith('Over') else v<L
new=[]; cache={}
for fn in sorted(glob.glob('../papertrade/*_snapshot.json')):
    for x in json.load(open(fn)):
        key=f"{x['eid']}|{x['oid']}|{x.get('spec')}"
        if key in done: continue
        try: ko=dt.datetime.strptime(fn.split('/')[-1][:4]+'-'+x['ko'],'%Y-%m-%d %H:%M')
        except Exception: continue
        if now-ko<dt.timedelta(hours=3): continue
        if x['eid'] not in cache: cache[x['eid']]=res(x['eid'])
        r=cache[x['eid']]
        if r is None: continue
        y=None if r=='void' else outcome(x,r)
        done.add(key)
        if y is None: continue
        new.append(dict(key=key,date=fn.split('/')[-1][:10],sport=x.get('sport','football'),lg=x['lg'],mid=x['mid'],src=x.get('src'),odds=x['odds'],hp=x['hp'],mp=x['mp'],ev=x['ev'],won=bool(y)))
with open(G,'a') as f:
    for n in new: f.write(json.dumps(n)+'\n')
A=[json.loads(l) for l in open(G)] if os.path.exists(G) else []
clip=lambda q:min(max(q,1e-6),1-1e-6)
lines=[f'graded total {len(A)} (+{len(new)} new)   [{now:%Y-%m-%d %H:%M} UTC]']
by=collections.defaultdict(list)
for a in A: by[(a['sport'],a['mid'])].append(a)
for (sp,mid),v in sorted(by.items()):
    llm=sum(-math.log(clip(a['mp']) if a['won'] else clip(1-a['mp'])) for a in v)/len(v)
    llh=sum(-math.log(clip(a['hp']) if a['won'] else clip(1-a['hp'])) for a in v)/len(v)
    pk=[a for a in v if a['ev']>=1.05 and 1.2<=a['odds']<=3.0]
    roi=(sum(a['odds'] for a in pk if a['won'])/len(pk)-1) if pk else 0
    fv=[a for a in v if a['mp']>=0.5] or v   # model-favoured side only (both sides of a line average to 0.500)
    lines.append(f"{sp:<10} mid {mid:<7} n {len(v):5d}  fav-side hit {sum(a['won'] for a in fv)/len(fv):.3f} vs model {sum(a['mp'] for a in fv)/len(fv):.3f}  "
                 f"logloss model {llm:.4f} house {llh:.4f}  | EV>=1.05 picks {len(pk)} ROI {roi:+.3f}  {'PASS' if len(v)>=300 and llm<llh and pk and roi>0 else ''}")
open('../papertrade/grade_report.txt','w').write('\n'.join(lines)+'\n'); print('\n'.join(lines))
