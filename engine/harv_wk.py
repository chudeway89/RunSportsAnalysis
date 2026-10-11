import json,time,datetime,sys
from post_lib import *
now=time.time()*1000
end=datetime.datetime(2026,10,19,23,59,tzinfo=datetime.timezone.utc).timestamp()*1000
CATS={'England','Scotland','Germany','Italy','Spain','France','Netherlands','Belgium','Portugal','Turkiye','Turkey','Greece'}
out=[];seen=set()
for mk in ['1','18']:
    for pg in range(1,60):
        d=curl_get(f'https://www.sportybet.com/api/ng/factsCenter/pcUpcomingEvents?sportId=sr:sport:1&marketId={mk}&pageSize=100&pageNum={pg}')
        ts=(d.get('data') or {}).get('tournaments') or []
        if not ts: break
        for t in ts:
            for e in t.get('events',[]):
                st=e.get('estimateStartTime',0); cat=e.get('sport',{}).get('category',{}).get('name','')
                if st>end or st<now+60*60*1000 or e['eventId'] in seen or cat not in CATS: continue
                seen.add(e['eventId'])
                out.append({'sport':'football','sid':'sr:sport:1','eid':e['eventId'],'home':e['homeTeamName'],'away':e['awayTeamName'],'tour':t.get('name',''),'cat':cat,'start':st})
json.dump(out,open('board_wk.json','w')); print(len(out))
import collections; print(collections.Counter((o['cat'],o['tour']) for o in out).most_common(40))
