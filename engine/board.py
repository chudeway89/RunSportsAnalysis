# Harvest the SportyBet pre-match board (football/basketball/baseball) for the next HOURS hours + all markets.
# Usage: python3 board.py [HOURS=30]  -> cache/board_<UTCdate>.json
import json,time,datetime,sys,os
from concurrent.futures import ThreadPoolExecutor
from post_lib import curl_get,SID
H=float(sys.argv[1]) if len(sys.argv)>1 else 30
now=time.time()*1000; end=now+H*3600*1000
JUNK=('srl','simulated','women','u19','u20','u21','u23','youth','reserve','esoccer','ebasketball','virtual','2k')
ev=[];seen=set()
for sp,sid in SID.items():
    for mk in ['1','219','251','18']:
        for pg in range(1,60):
            d=curl_get(f'https://www.sportybet.com/api/ng/factsCenter/pcUpcomingEvents?sportId={sid}&marketId={mk}&pageSize=100&pageNum={pg}')
            ts=(d.get('data') or {}).get('tournaments') or []
            if not ts: break
            for t in ts:
                for e in t.get('events',[]):
                    st=e.get('estimateStartTime',0)
                    if st>end or st<now+30*60*1000 or e['eventId'] in seen: continue
                    seen.add(e['eventId'])
                    cat=e.get('sport',{}).get('category',{}).get('name','')
                    lg=cat+' / '+t.get('name','')
                    if any(j in (lg+' '+e['homeTeamName']+' '+e['awayTeamName']).lower() for j in JUNK): continue
                    ev.append({'sport':sp,'sid':sid,'eid':e['eventId'],'home':e['homeTeamName'],'away':e['awayTeamName'],'lg':lg,'start':st})
    print(sp,len(ev),file=sys.stderr)
def f(e):
    d=curl_get(f"https://www.sportybet.com/api/ng/factsCenter/event?eventId={e['eid']}&productId=3")
    mk=[]
    for m in (d.get('data') or {}).get('markets',[]) or []:
        if m.get('status',0)!=0: continue
        for o in m.get('outcomes',[]):
            if not o.get('isActive',1): continue
            try: mk.append({'mid':str(m['id']),'spec':m.get('specifier'),'mdesc':m.get('desc',''),'desc':o.get('desc'),'odds':float(o['odds']),'p':float(o.get('probability') or 0),'oid':o['id']})
            except Exception: pass
    return dict(e,ko=datetime.datetime.utcfromtimestamp(e['start']/1000).strftime('%m-%d %H:%M'),fx=e['home']+' v '+e['away'],mk=mk)
with ThreadPoolExecutor(12) as ex: R=list(ex.map(f,ev))
fn=os.path.join('cache','board_%s.json'%datetime.datetime.utcnow().strftime('%Y-%m-%d'))
json.dump(R,open(fn,'w')); print(fn,len(R),'events',sum(len(r['mk']) for r in R),'outcomes')
