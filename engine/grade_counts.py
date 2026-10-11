# Grade a counts paper-trade snapshot against football-data results (HC/AC/HY/AY).
# Usage: python3 grade_counts.py ../papertrade/<snapshot>.json   (run from engine/ after refreshing fd CSVs)
import json,sys,math,collections,datetime as dt
from counts import load_counts
S=json.load(open(sys.argv[1]))
res={}
for r in load_counts(): res[(r['lg'],r['h'],r['a'])]=r
def won(x,r):
    m,s,d=x['mid'],x['spec'] or '',x['desc']
    tc=r['hc']+r['ac']; ty=(r['hy'] or 0)+(r['ay'] or 0)+(r['hr'] or 0)+(r['ar'] or 0)
    if m=='166': v=tc
    elif m=='900300': v=r['hc']
    elif m=='900301': v=r['ac']
    elif m=='139': v=ty
    elif m=='800063': return ty>=int(d[:-1])
    else: return None
    t=float(s[6:])
    if v==t: return None   # push
    return v>t if d.startswith('Over') else v<t
clip=lambda q:min(max(q,1e-6),1-1e-6)
by=collections.defaultdict(lambda:dict(n=0,llm=0,llh=0,bets=0,ret=0))
for x in S:
    r=res.get((x['lg'],x['fdh'],x['fda']))
    if not r: continue
    y=won(x,r)
    if y is None: continue
    b=by[x['mid']]; b['n']+=1
    b['llm']+=-math.log(clip(x['mp']) if y else clip(1-x['mp'])); b['llh']+=-math.log(clip(x['hp']) if y else clip(1-x['hp']))
    if x['ev']>=1.05 and 1.3<=x['odds']<=2.6: b['bets']+=1; b['ret']+=x['odds'] if y else 0
for m,b in by.items():
    print(f"mid {m}: graded {b['n']}  logloss model {b['llm']/b['n']:.4f} vs house {b['llh']/b['n']:.4f}  | EV>=1.05 picks {b['bets']} ROI {(b['ret']/b['bets']-1 if b['bets'] else 0):+.3f}")
