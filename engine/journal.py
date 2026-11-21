# Deterministic daily "learning" entry, written by the scheduled workflow (no Claude session needed).
# Reads papertrade/graded.jsonl + status.json and appends one dated block to papertrade/JOURNAL.md with a
# per-market verdict against the paper-trade pass rule: n>=300, model log-loss < house, EV>=1.05 picks ROI>0.
import json,os,math,collections,datetime as dt
os.chdir(os.path.dirname(os.path.abspath(__file__)))
G,J,S='../papertrade/graded.jsonl','../papertrade/JOURNAL.md','../papertrade/status.json'
A=[json.loads(l) for l in open(G)] if os.path.exists(G) else []
st=json.load(open(S)) if os.path.exists(S) else {}
try: HL=json.load(open('../papertrade/health.json')).get('steps',{})
except Exception: HL={}
BAD=[f"{k} ({v.get('error','')[:80]})" for k,v in HL.items() if not v.get('ok')]
clip=lambda q:min(max(q,1e-6),1-1e-6)
ll=lambda v,k:sum(-math.log(clip(a[k]) if a['won'] else clip(1-a[k])) for a in v)/len(v)
by=collections.defaultdict(list)
for a in A: by[(a['sport'],a['mid'])].append(a)
rows=[]
for (sp,mid),v in sorted(by.items(),key=lambda t:-len(t[1])):
    m,h=ll(v,'mp'),ll(v,'hp'); pk=[a for a in v if a['ev']>=1.05 and 1.2<=a['odds']<=3.0]
    roi=(sum(a['odds'] for a in pk if a['won'])/len(pk)-1) if pk else 0.0
    if len(v)<300: verdict='collecting'
    elif m<h and pk and roi>0: verdict='**PASS**'
    elif m>=h: verdict='FAIL (house better)'
    else: verdict='FAIL (picks lose)'
    rows.append(f'| {sp} | {mid} | {len(v)} | {m:.4f} | {h:.4f} | {m-h:+.4f} | {len(pk)} | {roi:+.3f} | {verdict} |')
day=sum(1 for l in open(J) if l.startswith('## Day ')) + 1 if os.path.exists(J) else 1
now=dt.datetime.utcnow()
out=[f'## Day {day} — {now:%Y-%m-%d %H:%M} UTC',
     f"Run: {'OK' if st.get('ok') else 'FAILED'} | snapshot {st.get('snapshot_outcomes','?')} outcomes / {st.get('events','?')} events | failed steps: {st.get('failed_steps') or 'none'}",
     f"Pipeline steps: {', '.join(k+('' if v.get('ok') else ' FAILED') for k,v in HL.items()) or 'n/a'}"+(f" | **FAILED: {'; '.join(BAD)}**" if BAD else ''),
     f'Graded outcomes to date: {len(A)}', '',
     '| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |',
     '|---|---|---|---|---|---|---|---|---|', *rows, '']
if not os.path.exists(J):
    out=['# Paper-trade learning journal','','Written automatically by `.github/workflows/papertrade.yml` via `engine/journal.py`. '
         'A market is stakeable only once it shows **PASS** (n ≥ 300, model log-loss below the house, EV ≥ 1.05 picks with ROI > 0).','']+out
open(J,'a').write('\n'.join(out)+'\n'); print('\n'.join(out))
