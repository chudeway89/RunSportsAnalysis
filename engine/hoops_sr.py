# Per-league basketball spread (SD of total & margin around a market-quality line) for all Sportradar leagues on file.
# sd_market ~= ratio * sd_teammodel, ratio measured on NBA/WNBA vs closing lines (coef_hoops_us.json).
import json,datetime as dt,numpy as np,collections
from hoops import walk
U=json.load(open('coef_hoops_us.json')); rT=np.mean([U[k]['rT'] for k in U]); rM=np.mean([U[k]['rM'] for k in U])
G=[json.loads(l) for l in open('data/sr_scores.jsonl')]
by=collections.defaultdict(list)
for g in G:
    if g['sport']!='basketball': continue
    g['date']=dt.datetime.fromisoformat(g['date']); by[(g['lg'],g['lgname'])].append(g)
out={}
for (lg,name),gs in by.items():
    if len(gs)<80: continue
    W=walk(gs,min_train=40)
    if len(W)<40: continue
    t=np.array([g['hs']+g['as_']-(eh+ea) for g,eh,ea in W]); m=np.array([g['hs']-g['as_']-(eh-ea) for g,eh,ea in W])
    out[lg]=dict(name=name,n=len(W),mean_total=float(np.mean([g['hs']+g['as_'] for g in gs])),sdT=float(t.std()*rT),sdM=float(m.std()*rM),biasT=float(t.mean()))
    print(f"{name:<40} n{len(W):4d} avg total {out[lg]['mean_total']:.1f}  SD total {out[lg]['sdT']:.1f}  SD margin {out[lg]['sdM']:.1f}")
json.dump(out,open('coef_hoops_sr.json','w'))
