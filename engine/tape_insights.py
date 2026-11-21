# Deep read of the graded tape (every market, every fixture, not just ticket legs).
# Question asked of every slice: does the result differ from the HOUSE probability (resid = won - p_house),
# and would flat 1-unit bets on it have made money (ROI on first-seen odds)?
# Guards: SE clustered by fixture; a finding must have the same sign in both halves (by kick-off);
# |z| thresholds account for the number of slices tested.  Context features (team form, league scoring,
# H2H within the window) are built ONLY from matches that kicked off earlier (no look-ahead).
# Usage: python3 tape_insights.py  -> ../papertrade/INSIGHTS.md
import json,math,re,collections,glob,os,sys
OUT='../papertrade/INSIGHTS.md'
import sys as _s
def _load():
    from tapelib import iter_graded
    for r in iter_graded():
        if not r.get('hp') or r['res'] not in ('W','L','Q') or not r.get('start'): continue
        for k in ('ko','oid','ht'): r.pop(k,None)
        for k in ('eid','sport','lg','fx','mid','mdesc','desc','spec','res','score'):
            if isinstance(r.get(k),str): r[k]=_s.intern(r[k])
        yield r
R=list(_load())
R=[r for r in R if r.get('hp') and r['res'] in ('W','L','Q') and r.get('start')]
for r in R:
    r['y']=1.0 if r['res']=='W' else 0.0 if r['res']=='L' else (1.0 if r['ret']>1 else 0.0 if r['ret']<1 else 0.5)
    r['pnl']=r['ret']-1
starts=sorted(r['start'] for r in R); MID=starts[len(starts)//2]
def stat(rows):
    n=len(rows)
    if n==0: return None
    res=sum(r['y']-r['hp'] for r in rows)/n; roi=sum(r['pnl'] for r in rows)/n
    ce=collections.defaultdict(lambda:[0.0,0.0])
    for r in rows: c=ce[r['eid']]; c[0]+=r['y']-r['hp']-res; c[1]+=r['pnl']-roi
    se_r=math.sqrt(sum(a*a for a,_ in ce.values()))/n; se_p=math.sqrt(sum(b*b for _,b in ce.values()))/n
    a=[r for r in rows if r['start']<MID]; b=[r for r in rows if r['start']>=MID]
    h=lambda s,k:(sum(x[k] for x in s)/len(s) if s else float('nan'))
    ra=sum(x['y']-x['hp'] for x in a)/len(a) if a else float('nan'); rb=sum(x['y']-x['hp'] for x in b)/len(b) if b else float('nan')
    return dict(n=n,ev=len(ce),hit=sum(r['y'] for r in rows)/n,p=sum(r['hp'] for r in rows)/n,res=res,se=se_r or 1e-9,
                roi=roi,se_roi=se_p or 1e-9,ra=ra,rb=rb,roia=h(a,'pnl'),roib=h(b,'pnl'),odds=sum(r['odds'] for r in rows)/n)
def fmt(name,s):
    if not s: return f'| {name} | 0 |'
    z=s['res']/s['se']; st='both' if (s['ra']>0)==(s['rb']>0) else 'FLIPS'
    return (f"| {name} | {s['n']} ({s['ev']} fx) | {s['odds']:.2f} | {100*s['p']:.1f}% | {100*s['hit']:.1f}% | "
            f"{100*s['res']:+.1f}pp ±{100*s['se']:.1f} (z {z:+.1f}) | {100*s['roi']:+.1f}% ±{100*s['se_roi']:.1f} | "
            f"{100*s['ra']:+.1f}/{100*s['rb']:+.1f} {st} |")
HDR='| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |\n|---|---|---|---|---|---|---|---|'
def band(o): return '<1.30' if o<1.3 else '1.30-1.59' if o<1.6 else '1.60-2.19' if o<2.2 else '2.20-3.99' if o<4 else '4.00+'
def pband(p): return '<.40' if p<.4 else '.40-.55' if p<.55 else '.55-.65' if p<.65 else '.65-.75' if p<.75 else '.75-.82' if p<.82 else '.82-.90' if p<.9 else '.90+'
def tier(lg):
    l=(lg or '').lower()
    if any(t in l for t in ('women',' w ','(w)')): return 'women'
    if any(t in l for t in ('u17','u18','u19','u20','u21','u23','youth','reserve','primavera','junior')): return 'youth/res'
    if 'friendl' in l: return 'friendly'
    if any(t in l for t in ('cup','copa','coupe','pokal','coppa','taca','beker','trophy','shield','knockout','play-off','playoff')): return 'cup'
    top=('england / premier league','spain / laliga','italy / serie a','germany / bundesliga','france / ligue 1','uefa champions','uefa europa')
    if any(t in l for t in top): return 'top5+UEFA'
    return 'other league'
def side(r):
    d=r['desc']
    if d.startswith(('Over','Under')): return d.split()[0]
    return d
def line(r):
    m=re.search(r'total=([\d.]+)',r.get('spec') or ''); return float(m[1]) if m else None
L=[]; out=L.append
fb=[r for r in R if r['sport']=='football']
out(f"# Tape insights — every market on every fixture\n\nBuilt by `engine/tape_insights.py` from the graded tape (`cache/tape_graded/`). "
    f"{len(R):,} settled outcomes on {len({r['eid'] for r in R}):,} fixtures, kick-offs {__import__('datetime').datetime.utcfromtimestamp(starts[0]/1000):%Y-%m-%d} → "
    f"{__import__('datetime').datetime.utcfromtimestamp(starts[-1]/1000):%Y-%m-%d}. Halves split at {__import__('datetime').datetime.utcfromtimestamp(MID/1000):%Y-%m-%d %H:%M}.\n\n"
    "Read: *actual − house* is the calibration error of SportyBet's own probability; *flat ROI* is what 1 unit on every outcome in the slice returned at first-seen odds. "
    "± is one SE clustered by fixture. A slice is only worth anything if |z| is large (≥3 here, many slices are tested) AND the sign holds in both halves.\n")
# 1. overall by sport/band
out('## 1. Calibration and margin by sport and odds band\n'+HDR)
for sp in [s for s,_ in collections.Counter(r['sport'] for r in R).most_common(8)]:
    for b in ('<1.30','1.30-1.59','1.60-2.19','2.20-3.99','4.00+'):
        s=stat([r for r in R if r['sport']==sp and band(r['odds'])==b])
        if s and s['n']>=300: out(fmt(f'{sp} {b}',s))
# 2. every football market family × side × odds band, sorted by z
out('\n## 2. Strongest slices on the whole board (market × side × odds band, n ≥ 400, |z| ≥ 2.5)\n'+HDR)
G=collections.defaultdict(list)
for r in R: G[(r['sport'],r.get('mdesc') or r['mid'],side(r) if r['mid'] not in ('45','46','81','98') else 'score',band(r['odds']))].append(r)
cand=[]
for k,v in G.items():
    if len(v)<400: continue
    s=stat(v); z=s['res']/s['se']
    if abs(z)>=2.5: cand.append((z,k,s))
cand.sort(key=lambda x:-abs(x[0]))
ntest=sum(1 for v in G.values() if len(v)>=400)
for z,k,s in cand[:45]: out(fmt(' / '.join(k),s))
out(f'\n{ntest} slices tested; by chance alone ~{ntest*0.0124:.0f} would show |z| ≥ 2.5 and ~{ntest*0.0027:.1f} |z| ≥ 3.')
# 3. Rule audit on the full board
out('\n## 3. Rule audit — each binding rule tested on the whole board, not just our legs\n'+HDR)
def _feat():
    return globals().get('FEAT',{})
def F(cond,rows=fb): return [r for r in rows if cond(r)]
def ou(r,s,l=None): return r['mid']=='18' and r['desc'].startswith(s) and (l is None or line(r)==l)
p1={}
for r in fb:
    if r['mid']=='1': p1.setdefault(r['eid'],{})[r['desc']]=r['hp']
fav=lambda r: max(p1.get(r['eid'],{}).values() or [0])
audit=[
 ('Unders p<0.82 (all lines)',F(lambda r:ou(r,'Under') and r['hp']<0.82 and r['odds']<2.2)),
 ('Unders p≥0.82',F(lambda r:ou(r,'Under') and r['hp']>=0.82)),
 ('Unders 1.18-2.2 when favourite p≥0.65',F(lambda r:ou(r,'Under') and 1.18<=r['odds']<2.2 and fav(r)>=0.65)),
 ('Overs 1.18-2.2 (.5 lines)',F(lambda r:ou(r,'Over') and 1.18<=r['odds']<2.2 and line(r) and line(r)%1)),
 ('Overs integer line (Over 2/3) 1.18-2.2',F(lambda r:ou(r,'Over') and 1.18<=r['odds']<2.2 and line(r) and line(r)%1==0)),
 ('Over 1.5 all',F(lambda r:ou(r,'Over',1.5))),
 ('Away 1X2 p<0.75 (odds<2.2)',F(lambda r:r['mid']=='1' and r['desc']=='Away' and r['odds']<2.2 and r['hp']<0.75)),
 ('Away 1X2 p≥0.75',F(lambda r:r['mid']=='1' and r['desc']=='Away' and r['hp']>=0.75)),
 ('Home 1X2 odds<2.2',F(lambda r:r['mid']=='1' and r['desc']=='Home' and r['odds']<2.2)),
 ('Draw (all)',F(lambda r:r['mid']=='1' and r['desc']=='Draw')),
 ('AH +1.5 receiver when fav p≥0.55',F(lambda r:r['mid']=='16' and '(+1.5)' in r['desc'] and fav(r)>=0.55)),
 ('AH +2.5 receiver when fav p≥0.60',F(lambda r:r['mid']=='16' and '(+2.5)' in r['desc'] and fav(r)>=0.60)),
 ('DC 12 (Home or Away)',F(lambda r:r['mid']=='10' and ('Home or Away' in r['desc'] or r['desc'] in ('12','Home/Away')))),
 ('DC 1X / X2',F(lambda r:r['mid']=='10' and not ('Home or Away' in r['desc'] or r['desc'] in ('12','Home/Away')))),
 ('DNB 1.18-2.2',F(lambda r:r['mid']=='11' and 1.18<=r['odds']<2.2)),
 ('BTTS Yes',F(lambda r:r['mid']=='29' and r['desc'] in ('Yes','GG'))),
 ('BTTS No',F(lambda r:r['mid']=='29' and r['desc'] in ('No','NG'))),
 ('Both halves U1.5 (m59) No',F(lambda r:r['mid']=='59' and r['desc']=='No')),
 ('Corners 166 Over',F(lambda r:r['mid']=='166' and r['desc'].startswith('Over'))),
 ('Corners 166 Under',F(lambda r:r['mid']=='166' and r['desc'].startswith('Under'))),
 ('Team corners home 900300 Over',F(lambda r:r['mid']=='900300' and r['desc'].startswith('Over'))),
 ('Team corners home 900300 Under',F(lambda r:r['mid']=='900300' and r['desc'].startswith('Under'))),
 ('Team corners away 900301 Over',F(lambda r:r['mid']=='900301' and r['desc'].startswith('Over'))),
 ('Team corners away 900301 Under',F(lambda r:r['mid']=='900301' and r['desc'].startswith('Under'))),
 ('Bookings 139 Over',F(lambda r:r['mid']=='139' and r['desc'].startswith('Over'))),
 ('Bookings 139 Under',F(lambda r:r['mid']=='139' and r['desc'].startswith('Under'))),
 ('Women — Over (1.18-2.2)',F(lambda r:tier(r['lg'])=='women' and ou(r,'Over') and 1.18<=r['odds']<2.2)),
 ('Women — Under (1.18-2.2)',F(lambda r:tier(r['lg'])=='women' and ou(r,'Under') and 1.18<=r['odds']<2.2)),
 ('Youth/reserves — Over (1.18-2.2)',F(lambda r:tier(r['lg'])=='youth/res' and ou(r,'Over') and 1.18<=r['odds']<2.2)),
 ('Friendlies — 1X2 favourite',F(lambda r:tier(r['lg'])=='friendly' and r['mid']=='1' and r['hp']>=0.5)),
 ('Cup — fav 1X2 p≥0.65',F(lambda r:tier(r['lg'])=='cup' and r['mid']=='1' and r['hp']>=0.65)),
 ('League — fav 1X2 p≥0.65',F(lambda r:tier(r['lg']) in ('other league','top5+UEFA') and r['mid']=='1' and r['hp']>=0.65)),
]
bb=[r for r in R if r['sport']=='basketball']
def hcp(r):
    m=re.search(r'\(([+-]?[\d.]+)\)',r['desc']) or re.search(r'hcp=([+-]?[\d.]+)',r.get('spec') or ''); return float(m[1]) if m else None
audit+=[
 ('BB handicap receiving ≥15 pts',[r for r in bb if r['mid']=='223' and (hcp(r) or 0)>=15]),
 ('BB handicap receiving 8.5-14.5',[r for r in bb if r['mid']=='223' and 8.5<=(hcp(r) or 0)<15]),
 ('BB handicap giving',[r for r in bb if r['mid']=='223' and (hcp(r) or 0)<0]),
 ('BB ML p≥0.75',[r for r in bb if r['mid']=='219' and r['hp']>=0.75]),
 ('BB totals Over 1.18-2.2',[r for r in bb if r['mid']=='225' and r['desc'].startswith('Over') and 1.18<=r['odds']<2.2]),
 ('BB totals Under 1.18-2.2',[r for r in bb if r['mid']=='225' and r['desc'].startswith('Under') and 1.18<=r['odds']<2.2]),
]
for name,rows in audit: out(fmt(name,stat(rows)))
# 4. football context: team form / league scoring / H2H from earlier matches only
out('\n## 4. Does form, league scoring or history add anything the price lacks? (football, prior matches only)\n')
games={}
for r in fb:
    if r.get('score') and r['eid'] not in games and ' v ' in (r['fx'] or ''):
        h,a=r['fx'].split(' v ',1); hs,as_=map(int,r['score'].split(':'))
        games[r['eid']]=dict(t=r['start'],lg=r['lg'],h=h,a=a,hs=hs,as_=as_)
ordered=sorted(games.items(),key=lambda kv:kv[1]['t'])
team=collections.defaultdict(list); lgg=collections.defaultdict(list); h2h=collections.defaultdict(list); FEAT={}
for eid,g in ordered:
    th,ta=team[g['h']][-5:],team[g['a']][-5:]; lgv=lgg[g['lg']]
    FEAT[eid]=dict(nh=len(th),na=len(ta),
        h_pts=sum(x[2] for x in th)/len(th) if th else None,a_pts=sum(x[2] for x in ta)/len(ta) if ta else None,
        h_gfga=sum(x[0]+x[1] for x in th)/len(th) if th else None,a_gfga=sum(x[0]+x[1] for x in ta)/len(ta) if ta else None,
        lg_avg=sum(lgv)/len(lgv) if len(lgv)>=8 else None,
        h_home_pts=(lambda v:sum(v)/len(v) if v else None)([x[2] for x in team[g['h']] if x[3]][-3:]),
        a_away_pts=(lambda v:sum(v)/len(v) if v else None)([x[2] for x in team[g['a']] if not x[3]][-3:]))
    hp_=3 if g['hs']>g['as_'] else 1 if g['hs']==g['as_'] else 0; ap_=3 if g['as_']>g['hs'] else 1 if g['hs']==g['as_'] else 0
    team[g['h']].append((g['hs'],g['as_'],hp_,True)); team[g['a']].append((g['as_'],g['hs'],ap_,False)); lgg[g['lg']].append(g['hs']+g['as_'])
def ctx(title,rows,key,bins):
    out(f'\n**{title}**\n\n'+HDR)
    for lab,lo,hi in bins:
        sel=[r for r in rows if (v:=key(r)) is not None and lo<=v<hi]
        s=stat(sel)
        if s and s['n']>=150: out(fmt(lab,s))
f_=lambda r,k:FEAT.get(r['eid'],{}).get(k)
ov25=[r for r in fb if ou(r,'Over',2.5)]; un25=[r for r in fb if ou(r,'Under',2.5)]; ov15=[r for r in fb if ou(r,'Over',1.5)]
ctx('Over 2.5 by league scoring so far (avg goals of earlier games in the same competition, ≥8 games)',ov25,lambda r:f_(r,'lg_avg'),
    [('league avg <2.3',0,2.3),('2.3-2.6',2.3,2.6),('2.6-2.9',2.6,2.9),('2.9-3.2',2.9,3.2),('≥3.2',3.2,99)])
ctx('Over 1.5 by league scoring so far',ov15,lambda r:f_(r,'lg_avg'),
    [('league avg <2.3',0,2.3),('2.3-2.6',2.3,2.6),('2.6-2.9',2.6,2.9),('2.9-3.2',2.9,3.2),('≥3.2',3.2,99)])
gsum=lambda r:(f_(r,'h_gfga')+f_(r,'a_gfga'))/2 if f_(r,'h_gfga') is not None and f_(r,'a_gfga') is not None and f_(r,'nh')>=3 and f_(r,'na')>=3 else None
ctx('Over 2.5 by both teams\' recent match goals (last ≤5 each, avg of GF+GA per game)',ov25,gsum,
    [('<2.0',0,2.0),('2.0-2.5',2.0,2.5),('2.5-3.0',2.5,3.0),('3.0-3.5',3.0,3.5),('≥3.5',3.5,99)])
ctx('Under 2.5 by both teams\' recent match goals',un25,gsum,[('<2.0',0,2.0),('2.0-2.5',2.0,2.5),('2.5-3.0',2.5,3.0),('3.0-3.5',3.0,3.5),('≥3.5',3.5,99)])
h1x2=[r for r in fb if r['mid']=='1' and r['desc']=='Home']; a1x2=[r for r in fb if r['mid']=='1' and r['desc']=='Away']; d1x2=[r for r in fb if r['mid']=='1' and r['desc']=='Draw']
fd=lambda r:(f_(r,'h_pts')-f_(r,'a_pts')) if f_(r,'h_pts') is not None and f_(r,'a_pts') is not None and f_(r,'nh')>=3 and f_(r,'na')>=3 else None
bins=[('away in much better form (≤-1.0 pts/g)',-9,-1.0),('-1.0 to -0.4',-1.0,-0.4),('similar (-0.4 to 0.4)',-0.4,0.4),('0.4 to 1.0',0.4,1.0),('home much better (≥1.0)',1.0,9)]
ctx('Home win by form gap (home last-5 pts/game − away last-5 pts/game)',h1x2,fd,bins)
ctx('Away win by form gap',a1x2,fd,bins)
ctx('Draw by form gap',d1x2,fd,bins)
# form vs price disagreement: hot team that the price does NOT rate
dis=lambda r:(f_(r,'h_pts')-f_(r,'a_pts'))/3-(p1[r['eid']].get('Home',0)-p1[r['eid']].get('Away',0)) if fd(r) is not None and r['eid'] in p1 else None
ctx('Home win when FORM disagrees with PRICE (form gap/3 minus price gap; + = form likes home more than the price does)',h1x2,dis,
    [('form much less keen (≤-0.4)',-9,-0.4),('-0.4 to -0.15',-0.4,-0.15),('agree (±0.15)',-0.15,0.15),('0.15 to 0.4',0.15,0.4),('form much keener (≥0.4)',0.4,9)])
ctx('Home win by home side\'s last-3 HOME pts/game',h1x2,lambda r:f_(r,'h_home_pts'),[('0-0.67',0,0.7),('0.67-1.34',0.7,1.4),('1.34-2.0',1.4,2.05),('2.0-2.67',2.05,2.7),('3.0',2.7,9)])
# tier tables
out('\n## 5. By competition type (football, odds 1.18–2.2 only)\n'+HDR)
for t in ('top5+UEFA','other league','cup','friendly','youth/res','women'):
    for nm,cond in (('Over',lambda r:ou(r,'Over')),('Under',lambda r:ou(r,'Under')),('Home 1X2',lambda r:r['mid']=='1' and r['desc']=='Home'),('Away 1X2',lambda r:r['mid']=='1' and r['desc']=='Away'),('BTTS Yes',lambda r:r['mid']=='29' and r['desc'] in ('Yes','GG'))):
        s=stat([r for r in fb if tier(r['lg'])==t and 1.18<=r['odds']<2.2 and cond(r)])
        if s and s['n']>=200: out(fmt(f'{t} — {nm}',s))
# 6. by country (O/U and 1X2 short prices), largest |z|
out('\n## 6. Competitions with the biggest goal-total miscalibration (O/U 1.18–2.2, n ≥ 120)\n'+HDR)
C=collections.defaultdict(list)
for r in fb:
    if r['mid']=='18' and 1.18<=r['odds']<2.2: C[(r['lg'],side(r))].append(r)
cc=[(stat(v)['res']/stat(v)['se'],k,stat(v)) for k,v in C.items() if len(v)>=120]
cc.sort(key=lambda x:-abs(x[0]))
for z,k,s in cc[:25]: out(fmt(f'{k[0]} — {k[1]}',s))
out(f'\n{len(cc)} competition×side slices tested (chance: ~{len(cc)*0.0124:.0f} at |z|≥2.5).')
# 7. day/time
out('\n## 7. Weekend vs midweek, kick-off hour (football O/U and 1X2 favourites, odds 1.18–2.2)\n'+HDR)
import datetime as dt
wd=lambda r:dt.datetime.utcfromtimestamp(r['start']/1000).weekday()
for nm,cond in (('Over',lambda r:ou(r,'Over')),('Under',lambda r:ou(r,'Under')),('fav 1X2',lambda r:r['mid']=='1' and r['hp']>=0.5)):
    for lab,c2 in (('Sat-Sun',lambda r:wd(r)>=5),('Mon-Fri',lambda r:wd(r)<5)):
        out(fmt(f'{nm} {lab}',stat([r for r in fb if 1.18<=r['odds']<2.2 and cond(r) and c2(r)])))
pass
# 8. corners / cards vs teams' own history (Sportradar stats, 2 seasons, prior dates only)
out('\n## 8. Corners and cards: do the teams\' own averages beat the house line?\n')
CN=[json.loads(l) for l in open('data/sr_fb_counts.jsonl')]; CN.sort(key=lambda c:c['date'])
hist=collections.defaultdict(list)   # team -> [(date, for_c, against_c, cards_for, fouls_for)]
for c in CN:
    if c.get('hc') is None: continue
    hist[c['hn']].append((c['date'],c['hc'],c['ac'],(c.get('hy') or 0)+(c.get('hr') or 0),c.get('hf'),(c.get('ay') or 0)+(c.get('ar') or 0)))
    hist[c['an']].append((c['date'],c['ac'],c['hc'],(c.get('ay') or 0)+(c.get('ar') or 0),c.get('af'),(c.get('hy') or 0)+(c.get('hr') or 0)))
import bisect
def prior(tm,date,n=10):
    v=hist.get(tm) or []; i=bisect.bisect_left([x[0] for x in v],date); return v[max(0,i-n):i]
def expc(r):
    if ' v ' not in (r['fx'] or ''): return None
    h,a=r['fx'].split(' v ',1); d=dt.datetime.utcfromtimestamp(r['start']/1000).strftime('%Y-%m-%d')
    H,A=prior(h,d),prior(a,d)
    if len(H)<5 or len(A)<5: return None
    m=lambda v,k:sum(x[k] for x in v)/len(v)
    return dict(corn=0.5*(m(H,1)+m(A,2))+0.5*(m(A,1)+m(H,2)), cards=0.5*(m(H,3)+m(A,5))+0.5*(m(A,3)+m(H,5)))
EX={}
def gap(r,k):
    if r['eid'] not in EX: EX[r['eid']]=expc(r)
    e=EX[r['eid']]; l=line(r)
    return None if (e is None or l is None) else e[k]-l
co=[r for r in fb if r['mid']=='166' and r['desc'].startswith('Over')]; cu=[r for r in fb if r['mid']=='166' and r['desc'].startswith('Under')]
gb=[('teams avg ≥2 below line',-99,-2),('-2 to -1',-2,-1),('-1 to 0',-1,0),('0 to +1',0,1),('+1 to +2',1,2),('≥2 above line',2,99)]
ctx('Corners OVER by (teams\' last-10 expected corners − line)',co,lambda r:gap(r,'corn'),gb)
ctx('Corners UNDER by the same gap',cu,lambda r:gap(r,'corn'),gb)
ko=[r for r in fb if r['mid']=='139' and r['desc'].startswith('Over')]; ku=[r for r in fb if r['mid']=='139' and r['desc'].startswith('Under')]
gb2=[('≤-1.5',-99,-1.5),('-1.5 to -0.5',-1.5,-0.5),('-0.5 to +0.5',-0.5,0.5),('+0.5 to +1.5',0.5,1.5),('≥+1.5',1.5,99)]
ctx('Bookings OVER by (teams\' last-10 cards − line)',ko,lambda r:gap(r,'cards'),gb2)
ctx('Bookings UNDER by the same gap',ku,lambda r:gap(r,'cards'),gb2)
open(OUT,'w').write('\n'.join(L)+'\n')
# 9. Our own research (team news, absences, form write-ups) tested against the board
out('\n## 9. Does our research (team news, absences, form) add to the house price?\n')
IDX={(r['eid'],r['mid'],(r.get('spec') or ''),r['desc']):r for r in R}
byev=collections.defaultdict(list)
for r in R: byev[r['eid']].append(r)
picks=[]; vetoed=set(); researched=set()
for f in glob.glob('../papertrade/research/*.json'):
    try: J=json.load(open(f))
    except Exception: continue
    for x in (J if isinstance(J,list) else [J]):
        e=x.get('eid'); 
        if not e: continue
        e=e if str(e).startswith('sr:') else f'sr:match:{e}'; researched.add(e)
        if x.get('veto'): vetoed.add(e)
        for p in x.get('picks') or []:
            k=(e,str(p.get('mid')),p.get('spec') or '',p.get('desc'))
            if k in IDX: picks.append((IDX[k],p.get('p')))
pk=[dict(r,rp=rp) for r,rp in picks if isinstance(rp,(int,float))]
out(f'{len(researched)} researched fixtures in papertrade/research, {len(vetoed)} vetoed; {len(picks)} research picks found on the graded tape.\n\n'+HDR)
out(fmt('all research picks',stat([r for r,_ in picks])))
for lab,lo,hi in (('research p ≤ house p',-1,0.0),('research 0–5pp above house',0.0,0.05),('5–10pp above',0.05,0.10),('10–15pp above',0.10,0.15),('>15pp above (R5 says skip)',0.15,1)):
    s=stat([r for r in pk if lo<r['rp']-r['hp']<=hi]); 
    if s: out(fmt(lab,s))
def short(rows): return [r for r in rows if 1.18<=r['odds']<2.2 and r['mid'] in ('1','10','11','18','29','16')]
out(fmt('VETOED fixtures — all short-priced main markets',stat(short([r for e in vetoed for r in byev.get(e,[])]))))
out(fmt('researched, not vetoed — same markets',stat(short([r for e in researched-vetoed for r in byev.get(e,[])]))))
fav_short=lambda rows:[r for r in rows if r['mid']=='1' and r['hp']>=0.55]
out(fmt('VETOED fixtures — the 1X2 favourite',stat(fav_short([r for e in vetoed for r in byev.get(e,[])]))))
out(fmt('not vetoed — the 1X2 favourite',stat(fav_short([r for e in researched-vetoed for r in byev.get(e,[])]))))
open(OUT,'w').write('\n'.join(L)+'\n')
