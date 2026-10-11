import csv,glob,datetime as dt
def f(x):
    try: return float(x)
    except: return None
def load():
    rows=[]
    for fn in glob.glob('*_2*.csv'):
        lg,season=fn[:-4].split('_')
        try: rd=list(csv.DictReader(open(fn,encoding='utf-8-sig',errors='ignore')))
        except Exception: continue
        for r in rd:
            if not r.get('FTHG') or not r.get('HomeTeam'): continue
            try: d=dt.datetime.strptime(r['Date'],'%d/%m/%Y' if len(r['Date'])==10 else '%d/%m/%y')
            except: continue
            rows.append(dict(lg=lg,season=season,date=d,h=r['HomeTeam'],a=r['AwayTeam'],hg=int(r['FTHG']),ag=int(r['FTAG']),
              hthg=f(r.get('HTHG')),htag=f(r.get('HTAG')),
              oh=f(r.get('AvgCH')) or f(r.get('AvgH')),od=f(r.get('AvgCD')) or f(r.get('AvgD')),oa=f(r.get('AvgCA')) or f(r.get('AvgA')),
              ph=f(r.get('PSCH')),pd=f(r.get('PSCD')),pa=f(r.get('PSCA')),
              o25=f(r.get('AvgC>2.5')) or f(r.get('Avg>2.5')),u25=f(r.get('AvgC<2.5')) or f(r.get('Avg<2.5')),
              ahl=f(r.get('AHCh')),ahh=f(r.get('AvgCAHH')),aha=f(r.get('AvgCAHA')),hxg=f(r.get('HxG')),axg=f(r.get('AxG'))))
    for fn in glob.glob('new_*.csv'):
        for r in csv.DictReader(open(fn,encoding='utf-8-sig',errors='ignore')):
            try: d=dt.datetime.strptime(r['Date'],'%d/%m/%Y' if len(r['Date'])==10 else '%d/%m/%y'); hg=int(r['HG']);ag=int(r['AG'])
            except: continue
            if d.year<2022: continue
            rows.append(dict(lg=fn[4:-4],season=r['Season'],date=d,h=r['Home'],a=r['Away'],hg=hg,ag=ag,hthg=None,htag=None,
              oh=f(r.get('AvgCH')),od=f(r.get('AvgCD')),oa=f(r.get('AvgCA')),ph=f(r.get('PSCH')),pd=f(r.get('PSCD')),pa=f(r.get('PSCA')),
              o25=None,u25=None,ahl=None,ahh=None,aha=None,hxg=None,axg=None))
    return rows
