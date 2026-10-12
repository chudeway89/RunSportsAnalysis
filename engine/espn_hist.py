# Historical results + CLOSING lines (total, spread, moneyline) from ESPN for NBA / WNBA / MLB.
# Usage: python3 espn_hist.py nba 2024-10-20 2026-06-25   -> data/espn_nba.jsonl (append, de-duplicated)
import json,sys,os,datetime as dt,subprocess,hashlib
from concurrent.futures import ThreadPoolExecutor
SP={'nba':'basketball/nba','wnba':'basketball/wnba','mlb':'baseball/mlb'}
lg,d0,d1=sys.argv[1],sys.argv[2],sys.argv[3]
C=os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache')
def get(url,keep=True):
    fn=os.path.join(C,'espn_'+hashlib.md5(url.encode()).hexdigest()+'.json')
    if keep and os.path.exists(fn):
        try: return json.load(open(fn))
        except Exception: pass
    for i in range(3):
        r=subprocess.run(['curl','-s','-m','25',url],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout)
            if 'error' not in d: json.dump(d,open(fn,'w'))
            return d
        except Exception: pass
    return {}
OUT=f'data/espn_{lg}.jsonl'; have=set()
if os.path.exists(OUT): have={json.loads(l)['id'] for l in open(OUT)}
days=[];t=dt.date.fromisoformat(d0)
while t<=min(dt.date.fromisoformat(d1),dt.date.today()-dt.timedelta(days=1)): days.append(t); t+=dt.timedelta(days=1)
def sb(day): return get(f'https://site.api.espn.com/apis/site/v2/sports/{SP[lg]}/scoreboard?dates={day:%Y%m%d}&limit=50')
G=[]
with ThreadPoolExecutor(12) as ex:
    for day,d in zip(days,ex.map(sb,days)):
        for e in d.get('events',[]):
            c=e['competitions'][0]
            if not c.get('status',{}).get('type',{}).get('completed') or e['id'] in have: continue
            H=[x for x in c['competitors'] if x['homeAway']=='home'][0]; A=[x for x in c['competitors'] if x['homeAway']=='away'][0]
            try: G.append(dict(id=e['id'],date=str(day),season_type=e.get('season',{}).get('slug',''),h=H['team']['abbreviation'],a=A['team']['abbreviation'],
                            hs=int(H['score']),as_=int(A['score']),periods=c.get('status',{}).get('period')))
            except Exception: pass
print(lg,'completed games',len(G))
def odds(g):
    d=get(f"https://sports.core.api.espn.com/v2/sports/{SP[lg].split('/')[0]}/leagues/{lg}/events/{g['id']}/competitions/{g['id']}/odds")
    for it in d.get('items',[]):
        if it.get('overUnder') is None: continue
        ho=(it.get('homeTeamOdds') or {}); ao=(it.get('awayTeamOdds') or {})
        return dict(g,ou=it.get('overUnder'),spread=it.get('spread'),hml=ho.get('moneyLine'),aml=ao.get('moneyLine'),prov=it['provider']['name'])
    return None
n=0
with open(OUT,'a') as f, ThreadPoolExecutor(12) as ex:
    for r in ex.map(odds,G):
        if r: f.write(json.dumps(r)+'\n'); n+=1
print('written',n)
