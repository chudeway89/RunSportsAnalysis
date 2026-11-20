# Automated data research on EVERY fixture of a board (all sports): Sportradar last-10 for both teams,
# venue form, H2H, and a "trend hit-rate" for every market outcome we can evaluate from past scores
# (results, DNB, double chance, handicaps, game totals, team totals, 1st-half totals, BTTS).
# Usage: python3 allform.py cache/allboard_sat21.json cache/allform21.json
import json,sys,re,collections,concurrent.futures as cf
import sr
B=json.load(open(sys.argv[1])); OUT=sys.argv[2]
def teams(eid):
    m=sr.match_info(eid.split(':')[-1],maxage=6*3600) or {}
    t=m.get('teams') or {}
    h,a=t.get('home') or {},t.get('away') or {}
    return (h.get('uid') or h.get('_id'),a.get('uid') or a.get('_id'),(m.get('_dt') or {}).get('uts'))
def games(uid,before):
    out=[]
    for m in sr.team_lastx(uid,15) or []:
        if not sr.finished(m): continue
        uts=(m.get('time') or {}).get('uts') or 0
        if before and uts>=before: continue
        t=m.get('teams') or {}; home=(t.get('home') or {}); away=(t.get('away') or {})
        ish=str(home.get('uid') or home.get('_id'))==str(uid)
        r=m['result']; p=m.get('periods') or {}; p1=p.get('p1') or {}
        gf,ga=(r['home'],r['away']) if ish else (r['away'],r['home'])
        h1=(p1.get('home'),p1.get('away')) if p1.get('home') is not None else None
        h1f,h1a=((h1[0],h1[1]) if ish else (h1[1],h1[0])) if h1 else (None,None)
        opp=str((away if ish else home).get('uid') or (away if ish else home).get('_id'))
        out.append(dict(uts=uts,home=ish,gf=gf,ga=ga,h1f=h1f,h1a=h1a,opp=opp))
    out.sort(key=lambda g:-g['uts']); return out[:10]
def research(e):
    try:
        hu,au,ts=teams(e['eid'])
        if not hu or not au: return e['eid'],None
        H,A=games(hu,ts),games(au,ts)
        return e['eid'],dict(hu=str(hu),au=str(au),H=H,A=A)
    except Exception as x: return e['eid'],None
def rate(vals):
    v=[x for x in vals if x is not None]; return (sum(v)/len(v),len(v)) if v else (None,0)
def trend(o,e,F):
    """fraction of past games (both teams, own perspective) in which this outcome would have won"""
    H,A=F['H'],F['A']; d=o['desc']; md=(o.get('mdesc') or '').lower(); sp=o.get('spec') or ''
    hn,an=e['home'].lower(),e['away'].lower()
    tl=re.search(r'total=([\d.]+)',sp); hc=re.search(r'hcp=([-\d.:]+)',sp)
    half='1st half' in md or '1st' in md and 'half' in md
    def res(g,side):   # side: +1 = this team is the one the outcome backs
        return g['gf']-g['ga']
    if d.startswith(('Over','Under')) and tl:
        L=float(tl[1]); over=d.startswith('Over')
        def ev(x): return None if x is None else (0.5 if x==L else (1.0 if (x>L)==over else 0.0))
        if hn.split()[0] in md and not half and 'total' not in md.split(hn.split()[0])[0][-3:]:
            vals=[ev(g['gf']) for g in H]+[ev(g['ga']) for g in A]; return rate(vals)
        if an.split()[0] in md and not half:
            vals=[ev(g['gf']) for g in A]+[ev(g['ga']) for g in H]; return rate(vals)
        if half and ('over/under' in md or 'total' in md) and hn.split()[0] not in md and an.split()[0] not in md:
            vals=[ev(None if g['h1f'] is None else g['h1f']+g['h1a']) for g in H+A]; return rate(vals)
        if not half and (md.startswith('over/under') or md.startswith('total') or 'incl. overtime' in md and 'over/under' in md):
            vals=[ev(g['gf']+g['ga']) for g in H+A]; return rate(vals)
        return (None,0)
    if half: return (None,0)
    if md in ('1x2','winner','moneyline','1x2 (incl. overtime)','winner (incl. overtime)') or md.startswith('1x2') or md.startswith('winner'):
        if d=='Home': return rate([float(g['gf']>g['ga']) for g in H]+[float(g['ga']>g['gf']) for g in A])
        if d=='Away': return rate([float(g['gf']>g['ga']) for g in A]+[float(g['ga']>g['gf']) for g in H])
        if d=='Draw': return rate([float(g['gf']==g['ga']) for g in H+A])
    if md.startswith('double chance'):
        if d=='Home or Draw': return rate([float(g['gf']>=g['ga']) for g in H]+[float(g['ga']>=g['gf']) for g in A])
        if d=='Draw or Away': return rate([float(g['gf']>=g['ga']) for g in A]+[float(g['ga']>=g['gf']) for g in H])
        if d=='Home or Away': return rate([float(g['gf']!=g['ga']) for g in H+A])
    if md.startswith('draw no bet'):
        f=lambda m:None if m==0 else float(m>0)
        if d=='Home': return rate([f(g['gf']-g['ga']) for g in H]+[f(g['ga']-g['gf']) for g in A])
        if d=='Away': return rate([f(g['gf']-g['ga']) for g in A]+[f(g['ga']-g['gf']) for g in H])
    if hc and ('handicap' in md):
        try: x=float(hc[1].split(':')[-1])
        except Exception: return (None,0)
        m=re.search(r'\(([-+]?[\d.]+)\)',d); x=float(m[1]) if m else x
        f=lambda mg:0.5 if mg+x==0 else float(mg+x>0)
        if d.startswith('Home'): return rate([f(g['gf']-g['ga']) for g in H]+[f(g['ga']-g['gf']) for g in A])
        if d.startswith('Away'): return rate([f(g['gf']-g['ga']) for g in A]+[f(g['ga']-g['gf']) for g in H])
    if md.startswith('gg/ng') or md=='both teams to score':
        both=lambda g:float(g['gf']>0 and g['ga']>0)
        if d in ('Yes','GG'): return rate([both(g) for g in H+A])
        if d in ('No','NG'): return rate([1-both(g) for g in H+A])
    return (None,0)
EV=[e for e in B]
R={}
with cf.ThreadPoolExecutor(16) as ex:
    for i,(eid,f) in enumerate(ex.map(research,EV)):
        R[eid]=f
        if i%200==0: print('researched',i,len(EV),flush=True)
out={}; ntr=0
for e in EV:
    F=R.get(e['eid'])
    if not F: out[e['eid']]=dict(fx=e['home']+' v '+e['away'],lg=e['lg'],sport=e['sport'],data=False); continue
    H,A=F['H'],F['A']
    h2h=[g for g in H if g['opp']==F['au']]
    summ=lambda G,venue=None:dict(n=len(G),w=sum(g['gf']>g['ga'] for g in G),d=sum(g['gf']==g['ga'] for g in G),l=sum(g['gf']<g['ga'] for g in G),
                                  gf=round(sum(g['gf'] for g in G)/len(G),2) if G else None,ga=round(sum(g['ga'] for g in G)/len(G),2) if G else None)
    tr=[]
    for o in e['mk']:
        r,n=trend(o,e,F)
        if r is not None and n>=8:
            tr.append(dict(mid=o['mid'],spec=o.get('spec'),desc=o['desc'],mdesc=o.get('mdesc'),odds=o.get('odds'),p=o.get('p'),trend=round(r,3),n=n)); ntr+=1
    out[e['eid']]=dict(fx=e['home']+' v '+e['away'],lg=e['lg'],sport=e['sport'],start=e['start'],data=True,
        home=summ(H),home_at_home=summ([g for g in H if g['home']]),away=summ(A),away_away=summ([g for g in A if not g['home']]),
        h2h=[f"{g['gf']}-{g['ga']}" for g in h2h],last_h=[f"{'H' if g['home'] else 'A'} {g['gf']}-{g['ga']}" for g in H[:6]],
        last_a=[f"{'H' if g['home'] else 'A'} {g['gf']}-{g['ga']}" for g in A[:6]],trends=tr)
json.dump(out,open(OUT,'w'))
print(len(out),'fixtures;',sum(1 for v in out.values() if v.get('data')),'with Sportradar form;',ntr,'market outcomes with a trend hit-rate')
print(collections.Counter((v['sport'],v.get('data')) for v in out.values()).most_common(20))
