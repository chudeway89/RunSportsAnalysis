# Final-score history for every basketball & baseball league on the board (Sportradar feed; Asia, S. America, Europe...).
# Usage: python3 sr_scores.py cache/board_<date>.json -> data/sr_scores.jsonl
import json,sys,os,datetime as dt
from concurrent.futures import ThreadPoolExecutor
import sr
OUT='data/sr_scores.jsonl'; have=set()
if os.path.exists(OUT): have={json.loads(l)['mid'] for l in open(OUT)}
B=[e for e in json.load(open(sys.argv[1])) if e['sport'] in ('basketball','baseball')]
with ThreadPoolExecutor(12) as ex: I=list(ex.map(lambda e:(e,sr.match_info(e['eid'].split(':')[-1])),B))
seasons={}; teams=set()
for e,m in I:
    if m:
        seasons[m['_seasonid']]=(e['sport'],m['_utid'],e['lg'])
        for s in ('home','away'): teams.add((m['teams'][s]['uid'],m['_utid'],e['sport'],e['lg']))
rows={}
def add(m,sp,utid,lgname):
    r=m.get('result') or {}
    if m['_id'] in have or r.get('home') is None or m.get('canceled') or m.get('postponed') or m['_utid']!=utid: return
    if m['time']['uts']>dt.datetime.utcnow().timestamp()-4*3600: return
    rows[m['_id']]=dict(mid=m['_id'],sport=sp,lg='sr%d'%utid,lgname=lgname,date=dt.datetime.utcfromtimestamp(m['time']['uts']).strftime('%Y-%m-%d'),
        h=str(m['teams']['home']['uid']),a=str(m['teams']['away']['uid']),hn=m['teams']['home']['name'],an=m['teams']['away']['name'],
        hs=r['home'],as_=r['away'],period=r.get('period'))
with ThreadPoolExecutor(12) as ex:
    for (sid,(sp,utid,lgn)),ms in zip(seasons.items(),ex.map(sr.season_matches,seasons)):
        for m in ms: add(m,sp,utid,lgn)
    for (uid,utid,sp,lgn),ms in zip(teams,ex.map(lambda t:sr.team_lastx(t[0],60),teams)):
        for m in ms: add(m,sp,utid,lgn)
with open(OUT,'a') as f:
    for r in rows.values(): f.write(json.dumps(r)+'\n')
print('seasons',len(seasons),'added',len(rows))
