# Sportradar "gismo" public stats feed (same provider/IDs as SportyBet: sr:match:N <-> match id N).
# Covers every league SportyBet lists (football, basketball, baseball...), incl. South America and Asia.
# All calls are cached on disk (engine/cache/, gitignored); finished-match docs never change.
import json,os,time,hashlib,subprocess
BASE='https://stats.fn.sportradar.com/betradar/en/Europe:Berlin/gismo/'
CACHE=os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache')
os.makedirs(CACHE,exist_ok=True)
def get(ep,maxage=None,tries=3):
    fn=os.path.join(CACHE,hashlib.md5(ep.encode()).hexdigest()+'.json')
    if os.path.exists(fn) and (maxage is None or time.time()-os.path.getmtime(fn)<maxage):
        try: return json.load(open(fn))
        except Exception: pass
    for i in range(tries):
        try:
            r=subprocess.run(['curl','-s','-m','25','-A','Mozilla/5.0',BASE+ep],capture_output=True,text=True)
            d=json.loads(r.stdout)['doc'][0]
            if d.get('event')=='exception': return None
            data=d.get('data'); json.dump(data,open(fn,'w')); return data
        except Exception: time.sleep(1+i)
    return None
def match_info(mid,maxage=6*3600): 
    d=get(f'match_info/{mid}',maxage); return (d or {}).get('match')
def match_stats(mid):
    """corners/cards/fouls etc for a FINISHED match -> {'hc','ac','hy','ay','hr','ar','hf','af'} or None"""
    d=get(f'match_details/{mid}')
    v=(d or {}).get('values') or {}
    def g(k):
        x=(v.get(k) or {}).get('value')
        return (x['home'],x['away']) if isinstance(x,dict) and 'home' in x else (None,None)
    hc,ac=g('124')
    if hc is None: return None
    hy,ay=g('40'); hr,ar=g('50'); yr=g('45'); hf,af=g('129')
    return dict(hc=hc,ac=ac,hy=hy,ay=ay,hr=(hr or 0)+(yr[0] or 0),ar=(ar or 0)+(yr[1] or 0),hf=hf,af=af)
def season_matches(sid,maxage=12*3600):
    d=get(f'stats_season_fixtures2/{sid}',maxage); return (d or {}).get('matches') or []
def team_lastx(uid,n=30,maxage=12*3600):
    d=get(f'stats_team_lastx/{uid}/{n}',maxage); return (d or {}).get('matches') or []
def finished(m):
    r=m.get('result') or {}
    return r.get('home') is not None and r.get('period') in ('nt','ot','ap','ft',None) and not m.get('canceled') and not m.get('postponed') and (m.get('status') or {}).get('name','Ended') in ('Ended','AET','AP','')
