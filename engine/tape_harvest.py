# Unfiltered market tape harvest: EVERY sport SportyBet lists, EVERY fixture (women's/youth/reserves included),
# EVERY market, for the next HOURS hours. No selection of any kind -> this is what the model learns the market from.
# Writes cache/tapeboard_<UTCdate>.json (same event format as board.py) and appends it to papertrade/tape/ via tape_store.
# Usage: python3 tape_harvest.py [HOURS=30]
import json,time,datetime,sys,os,subprocess
from concurrent.futures import ThreadPoolExecutor
from post_lib import curl_get
H=float(sys.argv[1]) if len(sys.argv)>1 else 30
now=time.time()*1000; end=now+H*3600*1000
MK='1,18,186,219,225,251,406,340,202,10,11'   # any primary market a sport may list under
def sport_probe(n):
    d=curl_get(f'https://www.sportybet.com/api/ng/factsCenter/pcUpcomingEvents?sportId=sr:sport:{n}&marketId={MK}&pageSize=1&pageNum=1') or {}
    t=(d.get('data') or {}).get('tournaments') or []
    return (f'sr:sport:{n}',t[0]['events'][0]['sport']['name']) if t and t[0].get('events') else None
with ThreadPoolExecutor(16) as ex: SPORTS=[s for s in ex.map(sport_probe,range(1,200)) if s]
print('sports',SPORTS,file=sys.stderr)
def events(sp):
    sid,name=sp; out=[]; seen=set()
    for pg in range(1,80):
        d=curl_get(f'https://www.sportybet.com/api/ng/factsCenter/pcUpcomingEvents?sportId={sid}&marketId={MK}&pageSize=100&pageNum={pg}') or {}
        ts=(d.get('data') or {}).get('tournaments') or []
        if not ts: break
        for t in ts:
            for e in t.get('events',[]):
                st=e.get('estimateStartTime',0)
                if st>end or st<now or e['eventId'] in seen: continue
                seen.add(e['eventId'])
                lg=(e.get('sport',{}).get('category',{}).get('name',''))+' / '+t.get('name','')
                out.append({'sport':name.lower(),'sid':sid,'eid':e['eventId'],'home':e['homeTeamName'],'away':e['awayTeamName'],'lg':lg,'start':st})
    print(name,len(out),file=sys.stderr); return out
with ThreadPoolExecutor(8) as ex: EV=[e for L in ex.map(events,SPORTS) for e in L]
def full(e):
    d=curl_get(f"https://www.sportybet.com/api/ng/factsCenter/event?eventId={e['eid']}&productId=3") or {}
    mk=[]
    for m in (d.get('data') or {}).get('markets',[]) or []:
        if m.get('status',0)!=0: continue
        for o in m.get('outcomes',[]):
            if not o.get('isActive',1): continue
            try: mk.append({'mid':str(m['id']),'spec':m.get('specifier'),'mdesc':m.get('desc',''),'desc':o.get('desc'),'odds':float(o['odds']),'p':float(o.get('probability') or 0),'oid':o['id']})
            except Exception: pass
    return dict(e,ko=datetime.datetime.utcfromtimestamp(e['start']/1000).strftime('%m-%d %H:%M'),fx=e['home']+' v '+e['away'],mk=mk)
with ThreadPoolExecutor(16) as ex: R=list(ex.map(full,EV))
os.makedirs('cache',exist_ok=True)
fn=os.path.join('cache','tapeboard_%s.json'%datetime.datetime.utcnow().strftime('%Y-%m-%d'))
json.dump(R,open(fn,'w')); print(fn,len(R),'events',sum(len(r['mk']) for r in R),'outcomes',file=sys.stderr)
subprocess.run([sys.executable,'tape_store.py',fn],check=True)
