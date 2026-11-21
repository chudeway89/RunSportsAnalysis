import json,datetime
from concurrent.futures import ThreadPoolExecutor
from post_lib import curl_get
MAP={('England','Premier League'):'E0',('England','Championship'):'E1',('England','League One'):'E2',('England','League Two'):'E3',
 ('Scotland','Premiership'):'SC0',('Scotland','Championship'):'SC1',('Scotland','League 1'):'SC2',('Scotland','League 2'):'SC3',
 ('Germany','Bundesliga'):'D1',('Germany','2. Bundesliga'):'D2',('Italy','Serie A'):'I1',('Italy','Serie B'):'I2',
 ('Spain','LaLiga'):'SP1',('Spain','LaLiga 2'):'SP2',('France','Ligue 1'):'F1',('France','Ligue 2'):'F2',
 ('Netherlands','Eredivisie'):'N1',('Belgium','Pro League'):'B1',('Portugal','Liga Portugal'):'P1',('Turkiye','Super Lig'):'T1',('Greece','Super League'):'G1'}
B=[dict(e,fd=MAP[(e['cat'],e['tour'])]) for e in json.load(open('board_wk.json')) if (e['cat'],e['tour']) in MAP]
def f(e):
    d=curl_get(f"https://www.sportybet.com/api/ng/factsCenter/event?eventId={e['eid']}&productId=3")
    mk=[]
    for m in (d.get('data') or {}).get('markets',[]) or []:
        if m.get('status',0)!=0: continue
        for o in m.get('outcomes',[]):
            if not o.get('isActive',1): continue
            try: mk.append({'mid':str(m['id']),'spec':m.get('specifier'),'mdesc':m.get('desc',''),'desc':o.get('desc'),'odds':float(o['odds']),'p':float(o.get('probability') or 0),'oid':o['id']})
            except Exception: pass
    return dict(e,ko=datetime.datetime.utcfromtimestamp(e['start']/1000).strftime('%m-%d %H:%M'),mk=mk)
with ThreadPoolExecutor(12) as ex: R=list(ex.map(f,B))
json.dump(R,open('m_wk.json','w'))
print(len(R),'events',sum(any(o['mid']=='166' for o in r['mk']) for r in R),'with corners O/U',sum(any(o['mid']=='139' for o in r['mk']) for r in R),'with bookings O/U')
