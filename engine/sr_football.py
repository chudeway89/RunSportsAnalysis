# Build corners/cards/fouls match history for EVERY football league on the board (incl. South America & Asia)
# from the Sportradar feed. Usage: python3 sr_football.py cache/board_<date>.json
# -> data/sr_fb_counts.jsonl (one finished match per line, de-duplicated, append-only)
import json,sys,os,datetime as dt,collections
from concurrent.futures import ThreadPoolExecutor
import sr
OUT='data/sr_fb_counts.jsonl'
have={}
if os.path.exists(OUT):
    for l in open(OUT): r=json.loads(l); have[r['mid']]=r
B=[e for e in json.load(open(sys.argv[1])) if e['sport']=='football' and (os.environ.get('ALL') or any(o['mid'] in('166','139','900300','900301') for o in e['mk']))]
print('board football events with corners/cards markets:',len(B))
def info(e): return e,sr.match_info(e['eid'].split(':')[-1])
with ThreadPoolExecutor(12) as ex: I=list(ex.map(info,B))
seasons={};teams=set()
for e,m in I:
    if not m or '_seasonid' not in m or '_utid' not in m: continue
    seasons[m['_seasonid']]=m['_utid']
    for s in ('home','away'): teams.add((m['teams'][s]['uid'],m['_utid']))
print('seasons',len(seasons),'teams',len(teams))
cand={}
def add(m,utid):
    if m.get('canceled') or m.get('postponed') or m.get('walkover'): return
    r=m.get('result') or {}
    if r.get('home') is None or m['_utid']!=utid: return
    if m['time']['uts']>dt.datetime.utcnow().timestamp()-3*3600: return
    cand[m['_id']]=(m,utid)
with ThreadPoolExecutor(12) as ex:
    for (sid,utid),ms in zip(seasons.items(),ex.map(sr.season_matches,seasons)):
        for m in ms: add(m,utid)
    for (uid,utid),ms in zip(teams,ex.map(lambda t:sr.team_lastx(t[0],40),teams)):
        for m in ms: add(m,utid)
todo=[k for k in cand if k not in have]
print('league matches found',len(cand),'new to fetch',len(todo))
def det(k): return k,sr.match_stats(k)
n=0
with open(OUT,'a') as f, ThreadPoolExecutor(16) as ex:
    for k,s in ex.map(det,todo):
        if not s: continue
        m,utid=cand[k]
        r=dict(mid=k,lg='sr%d'%utid,date=dt.datetime.utcfromtimestamp(m['time']['uts']).strftime('%Y-%m-%d'),
               h=str(m['teams']['home']['uid']),a=str(m['teams']['away']['uid']),hn=m['teams']['home']['name'],an=m['teams']['away']['name'],
               hg=m['result']['home'],ag=m['result']['away'],**s)
        f.write(json.dumps(r)+'\n'); n+=1
print('added',n,'total',len(have)+n)
