# Automated quantitative panel: Sportradar last-10 form for both sides of every fixture on a board.
# Usage: python3 autoform.py <board.json> <out.json>
import json,sys,re,math,datetime as dt
from concurrent.futures import ThreadPoolExecutor
import sr
B=json.load(open(sys.argv[1])); base={b['eid']:b for b in json.load(open('cache/baseline17.json'))}
now=dt.datetime.utcnow().timestamp()
CUP=re.compile(r'cup|copa|pokal|coupe|coppa|taca|beker|trophy|play-?off|knockout|kupa|cupa|puchar',re.I)
def form(uid,sport):
    ms=[m for m in sr.team_lastx(uid,12) if sr.finished(m) and (m.get('time') or {}).get('uts',0)<now-3600][:10]
    gf=ga=0; n=0; res=[]; opp=[]
    for m in ms:
        r=m['result']; h=m['teams']['home']['uid']==uid
        f,a=(r['home'],r['away']) if h else (r['away'],r['home'])
        if f is None or a is None: continue
        gf+=f; ga+=a; n+=1; res.append(f'{f}-{a}'); opp.append(m['teams']['away' if h else 'home']['uid'])
    return dict(n=n,gf=gf/n if n else None,ga=ga/n if n else None,res=res[:6],opp=opp,ms=ms)
def run(e):
    try:
        mid=int(e['eid'].split(':')[-1]); m=sr.match_info(mid)
        if not m: return dict(eid=e['eid'],fx=e['fx'],auto='no_sr')
        hu,au=m['teams']['home']['uid'],m['teams']['away']['uid']
        H,A=form(hu,e['sport']),form(au,e['sport'])
        rnd=m.get('round'); flags=[]
        if isinstance(rnd,int) and rnd<=2: flags.append('season_opener')
        if CUP.search(e['lg']): flags.append('knockout_90min')
        h2h=[f"{x['result']['home']}-{x['result']['away']}" for x in H['ms'] if au in (x['teams']['home']['uid'],x['teams']['away']['uid'])]
        out=dict(eid=e['eid'],fx=e['fx'],lg=e['lg'],round=rnd,flags=flags,h2h=h2h[:3],
                 home=dict(n=H['n'],gf=H['gf'],ga=H['ga'],last=H['res']),away=dict(n=A['n'],gf=A['gf'],ga=A['ga'],last=A['res']))
        b=base.get(e['eid'])
        if e['sport']=='football' and b and H['n']>=5 and A['n']>=5:
            # form xG: geometric blend of own attack and opponent defence, then half-way to the market
            fh=math.sqrt(max(H['gf'],0.2)*max(A['ga'],0.2)); fa=math.sqrt(max(A['gf'],0.2)*max(H['ga'],0.2))
            out.update(xg_h=round(0.5*b['lh']+0.5*fh,2),xg_a=round(0.5*b['la']+0.5*fa,2),confidence=0.15)
            tot=(H['gf']+H['ga']+A['gf']+A['ga'])/2
            if tot>=3.4: flags.append('high_scoring_profile')
            if tot<=2.0: flags.append('low_scoring_profile')
        elif e['sport']=='basketball' and b and H['n']>=4 and A['n']>=4:
            tot=(H['gf']+H['ga']+A['gf']+A['ga'])/2; mar=((H['gf']-H['ga'])-(A['gf']-A['ga']))/2+2.5
            out.update(total=round(tot,1),margin=round(mar,1),confidence=0.15)
        else: out['confidence']=0.0
        return out
    except Exception as ex: return dict(eid=e['eid'],fx=e['fx'],auto='err '+str(ex)[:60])
with ThreadPoolExecutor(16) as ex: R=list(ex.map(run,[e for e in B if e['sport'] in('football','basketball')]))
json.dump(R,open(sys.argv[2],'w'))
print(len(R),'fixtures;',sum(1 for r in R if r.get('confidence',0)>0),'with form;',sum(1 for r in R if 'auto' in r),'no data')
