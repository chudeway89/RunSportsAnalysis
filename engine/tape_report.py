# Analyse the graded tape (cache/tape_graded/, see tapelib.py) in ONE streaming pass (constant memory): flat-stake ROI and calibration for EVERY market slice on the
# unfiltered board.  Guards against data-mining: ROI SE is clustered by fixture, and a slice only counts
# as a candidate if it is positive in BOTH the early and the late half of the data (by kick-off).
# Writes ../papertrade/TAPE.md
import json,math,re,collections,datetime as dt
from tapelib import iter_graded,part_days,part_path
FAM={'1':'1X2','10':'Double Chance','11':'DNB','12':'Home No Bet','13':'Away No Bet','14':'Euro Handicap','15':'Winning Margin',
 '16':'Asian Handicap','18':'Total O/U','19':'Home team O/U','20':'Away team O/U','21':'Exact Goals','23':'Home Exact Goals',
 '24':'Away Exact Goals','25':'Goal Range','26':'Odd/Even','27':'Home Odd/Even','28':'Away Odd/Even','29':'GG/NG','30':'Teams to Score',
 '31':'Home Clean Sheet','32':'Away Clean Sheet','45':'Correct Score','46':'HT/FT Correct Score','47':'HT/FT','55':'1H/2H GG',
 '56':'Home score both halves','57':'Away score both halves','58':'Both halves Over','59':'Both halves Under','60':'1H 1X2',
 '63':'1H Double Chance','64':'1H DNB','65':'1H Euro Hcp','66':'1H Asian Hcp','68':'1H O/U','69':'1H Home O/U','70':'1H Away O/U',
 '71':'1H Exact Goals','74':'1H Odd/Even','75':'1H GG','76':'1H Home CS','77':'1H Away CS','78':'1H 1X2&GG','79':'1H 1X2&O/U',
 '81':'1H Correct Score','83':'2H 1X2','85':'2H Double Chance','86':'2H DNB','87':'2H Euro Hcp','88':'2H Asian Hcp','90':'2H O/U',
 '91':'2H Home O/U','92':'2H Away O/U','93':'2H Exact Goals','94':'2H Odd/Even','95':'2H GG','96':'2H Home CS','97':'2H Away CS',
 '98':'2H Correct Score','450001':'Goal Bounds','450002':'Goal Bounds Home','450003':'Goal Bounds Away','450004':'Excluded Goals',
 '450005':'Excluded Goals Home','450006':'Excluded Goals Away','548':'Multigoals','552':'1H Multigoals','553':'2H Multigoals',
 '810001':'1H Goal Bounds','810002':'1H Excluded Goals','818':'HT/FT & O/U','819':'HT/FT & 1H O/U','854':'Home or Over',
 '858':'Away or Over','547':'DC & O/U','219':'BB Winner','223':'BB Handicap','225':'BB Total','227':'BB Home total',
 '228':'BB Away total','251':'MLB Winner','256':'MLB Run line','258':'MLB Total','900036':'1H Home win-to-nil','900037':'1H Away win-to-nil',
 '900038':'2H Home win-to-nil','900052':'2H Away win-to-nil','33':'Home win-to-nil','34':'Away win-to-nil'}
def side(r):
    d=r['desc']; m=r['mid']
    if d.startswith(('Over','Under')): return d.split()[0]
    if m in ('16','66','88','223','256'):
        sgn=re.search(r'\(([+-]?[\d.]+)\)',d); x=float(sgn[1]) if sgn else 0
        return ('Home' if d.startswith('Home') else 'Away')+(' giving' if x<0 else ' receiving' if x>0 else ' level')
    if m in ('45','46','81','98'): return 'any score'
    if m in ('547','818','819','79','78'): return d.split(' & ')[0]+' & '+('Over' if 'Over' in d else 'Under' if 'Under' in d else d.split(' & ')[-1])
    return d
def band(o):
    return '<1.30' if o<1.3 else '1.30-1.59' if o<1.6 else '1.60-2.19' if o<2.2 else '2.20-3.99' if o<4 else '4.00+'
def tier(lg):
    l=(lg or '').lower()
    top=('england / premier','spain / laliga','italy / serie a','germany / bundesliga','france / ligue 1','champions league','europa league',
         'netherlands / eredivisie','portugal / liga portugal','nba','euroleague')
    if any(t in l for t in top): return 'top'
    if any(t in l for t in ('women','u19','u20','u21','u23','youth','reserve','amateur','friendly')): return 'junk'
    return 'other'
class Acc:
    """Running totals for one slice. Rows arrive grouped by fixture, so the fixture-clustered SE is accumulated
    from per-fixture mean returns without keeping any rows in memory."""
    __slots__=('n','pnl','odds','dec','hit','hpn','hps','k','m1','m2','_e','_s','_c')
    def __init__(s): s.n=s.pnl=s.odds=s.dec=s.hit=s.hpn=s.hps=s.k=s.m1=s.m2=0.0; s._e=None; s._s=0.0; s._c=0
    def _flush(s):
        if s._c: m=s._s/s._c; s.k+=1; s.m1+=m; s.m2+=m*m
        s._s=0.0; s._c=0
    def add(s,r):
        if r['eid']!=s._e: s._flush(); s._e=r['eid']
        p=r['ret']-1; s.n+=1; s.pnl+=p; s.odds+=r['odds']; s._s+=p; s._c+=1
        if r['res'] in ('W','L'):
            s.dec+=1; s.hit+=r['res']=='W'
            if r.get('hp'): s.hpn+=1; s.hps+=r['hp']
    def stats(s):
        s._flush()
        if not s.n: return None
        var=max(s.m2/s.k-(s.m1/s.k)**2,0.0) if s.k else 0.0
        return dict(n=int(s.n),ev=int(s.k),roi=s.pnl/s.n,se=(math.sqrt(var)/math.sqrt(s.k)) if s.k>1 else 9,
                    hit=s.hit/s.dec if s.dec else 0,exp=s.hps/s.hpn if s.hpn else 0,odds=s.odds/s.n)
# halves: split at the kick-off day where the cumulative row count passes one half (counted from partition sizes)
import gzip
days=part_days(); cnt={}
for d in days:
    with gzip.open(part_path(d),'rb') as f: cnt[d]=sum(1 for _ in f)
tot=sum(cnt.values()); run=0; cut_day=days[-1] if days else None
for d in days:
    run+=cnt[d]
    if run>=tot/2: cut_day=d; break
cut=dt.datetime.strptime(cut_day,'%Y-%m-%d').replace(tzinfo=dt.timezone.utc).timestamp()*1000+86400e3 if cut_day else 0
def trio(): return [Acc(),Acc(),Acc()]            # whole, early half, late half
S1=collections.defaultdict(Acc); FAMS=collections.defaultdict(trio); FINE=collections.defaultdict(trio)
nrows=0; nfx=0; last=None
for r in iter_graded(days):
    nrows+=1
    if r['eid']!=last: nfx+=1; last=r['eid']
    b=band(r['odds']); f=FAM.get(r['mid'],r['mid']); sd=side(r); h=1 if (r.get('start') or 0)<cut else 2
    if r['sport'] in ('football','basketball'): S1[(r['sport'],b)].add(r)
    for key,store in (((r['sport'],f,sd),FAMS),((r['sport'],f,sd,b,tier(r['lg'])),FINE)):
        t=store[key]; t[0].add(r); t[h].add(r)
out=['# Market tape — every market on every fixture (no selection)\n',
 f"{nrows:,} settled outcomes on {nfx:,} fixtures (kick-offs {days[0] if days else '-'} to {days[-1] if days else '-'}), priced at the earliest pre-match price we stored. "
 f"Flat 1-unit stake on every outcome. ROI = return per unit staked; SE clustered by fixture. Voids return the stake. Halves split after {cut_day}.\n"]
out.append('\n## 1. Does the house probability match reality? (all outcomes)\n\n| Sport | Odds band | n | Fixtures | House p | Actual win % | ROI | SE |\n|---|---|---|---|---|---|---|---|')
for sp in ('football','basketball'):
    for b in ('<1.30','1.30-1.59','1.60-2.19','2.20-3.99','4.00+'):
        s=S1[(sp,b)].stats() if (sp,b) in S1 else None
        if s: out.append(f"| {sp} | {b} | {s['n']:,} | {s['ev']:,} | {s['exp']:.3f} | {s['hit']:.3f} | {s['roi']:+.3f} | {s['se']:.3f} |")
tab=[]
for k,t in FAMS.items():
    s=t[0].stats()
    if s and s['ev']>=60: tab.append((k,s,t[1].stats(),t[2].stats()))
tab.sort(key=lambda x:-x[1]['roi'])
hdr='| Sport | Market | Side | n | Fixtures | Avg odds | House p | Actual | ROI | SE | Early half | Late half |\n|---|---|---|---|---|---|---|---|---|---|---|---|'
def line(k,s,s1,s2): return f"| {k[0]} | {k[1]} | {k[2]} | {s['n']:,} | {s['ev']:,} | {s['odds']:.2f} | {s['exp']:.3f} | {s['hit']:.3f} | {s['roi']:+.3f} | {s['se']:.3f} | {(s1 or {}).get('roi',0):+.3f} | {(s2 or {}).get('roi',0):+.3f} |"
cand=[t for t in tab if t[1]['roi']-1.5*t[1]['se']>0 and t[2] and t[3] and t[2]['roi']>0 and t[3]['roi']>0]
out.append(f"\n## 2. Candidates: ROI positive by >1.5 SE AND positive in both halves ({len(cand)} of {len(tab)} slices)\n\n"+hdr)
out+= [line(*t) for t in cand] or ['| none | | | | | | | | | | | |']
out.append('\n## 3. Best 30 market slices by ROI (≥60 fixtures)\n\n'+hdr); out+=[line(*t) for t in tab[:30]]
out.append('\n## 4. Worst 20 market slices\n\n'+hdr); out+=[line(*t) for t in tab[-20:]]
t5=[]
for k,t in FINE.items():
    s=t[0].stats()
    if s and s['ev']>=80:
        s1,s2=t[1].stats(),t[2].stats()
        if s1 and s2 and s1['roi']>0 and s2['roi']>0 and s['roi']-1.5*s['se']>0: t5.append((k,s,s1,s2))
t5.sort(key=lambda x:-(x[1]['roi']/max(x[1]['se'],1e-3)))
out.append(f"\n## 5. Finer slices (market × side × odds band × league tier), stable in both halves, ROI > 1.5 SE ({len(t5)})\n\n| Sport | Market | Side | Band | Tier | n | Fixtures | House p | Actual | ROI | SE | Early | Late |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for k,s,s1,s2 in t5[:40]:
    out.append(f"| {k[0]} | {k[1]} | {k[2]} | {k[3]} | {k[4]} | {s['n']:,} | {s['ev']:,} | {s['exp']:.3f} | {s['hit']:.3f} | {s['roi']:+.3f} | {s['se']:.3f} | {s1['roi']:+.3f} | {s2['roi']:+.3f} |")
n_tests=len(FINE)
out.append(f"\n_Multiple-testing note: section 5 searched {n_tests:,} slices; at a 1.5-SE bar roughly {int(n_tests*0.067):,} would pass by chance alone before the both-halves filter. Treat everything here as a hypothesis to forward-test, not a proven edge._")
if nrows:
    open('../papertrade/TAPE.md','w').write('\n'.join(out)+'\n')
    json.dump(dict(rows=nrows,fixtures=nfx,first=days[0],last=days[-1],candidates=len(cand)),open('../papertrade/tape_status.json','w'))
print('\n'.join(out[:14]))
