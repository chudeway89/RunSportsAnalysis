# List upcoming football events (no markets) for the next DAYS days -> cache/upcoming.json (feeds sr_football.py with ALL=1)
import json,time,sys
from post_lib import curl_get
D=float(sys.argv[1]) if len(sys.argv)>1 else 7
now=time.time()*1000; end=now+D*86400*1000; out=[]; seen=set()
JUNK=('srl','simulated','women','u19','u20','u21','u23','youth','reserve','esoccer','virtual','amateur')
for pg in range(1,200):
    d=curl_get(f'https://www.sportybet.com/api/ng/factsCenter/pcUpcomingEvents?sportId=sr:sport:1&marketId=1&pageSize=100&pageNum={pg}')
    ts=(d.get('data') or {}).get('tournaments') or []
    if not ts: break
    for t in ts:
        for e in t.get('events',[]):
            lg=e.get('sport',{}).get('category',{}).get('name','')+' / '+t.get('name','')
            if e['eventId'] in seen or e.get('estimateStartTime',0)>end or any(j in lg.lower() for j in JUNK): continue
            seen.add(e['eventId']); out.append({'sport':'football','eid':e['eventId'],'lg':lg,'mk':[]})
json.dump(out,open('cache/upcoming.json','w')); print(len(out))
