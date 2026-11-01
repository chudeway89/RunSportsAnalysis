# Analyse ../papertrade/tape_graded.jsonl: flat-stake ROI and calibration for EVERY market slice on the
# unfiltered board.  Guards against data-mining: ROI SE is clustered by fixture, and a slice only counts
# as a candidate if it is positive in BOTH the early and the late half of the data (by kick-off).
# Writes ../papertrade/TAPE.md
import json,math,re,collections,statistics as st
rows=[json.loads(l) for l in open('../papertrade/tape_graded.jsonl')]
rows=[r for r in rows if r['res']!='V' or True]
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
def stats(G):
    n=len(G)
    if n==0: return None
    ev=collections.defaultdict(list)
    for r in G: ev[r['eid']].append(r['ret']-1)
    per=[sum(v)/len(v) for v in ev.values()]
    roi=sum(r['ret']-1 for r in G)/n
    se=(st.pstdev(per)/math.sqrt(len(per))) if len(per)>1 else 9
    dec=[r for r in G if r['res'] in ('W','L')]
    hit=sum(r['res']=='W' for r in dec)/len(dec) if dec else 0
    hp=[r['hp'] for r in dec if r.get('hp')]
    exp=sum(hp)/len(hp) if hp else 0
    return dict(n=n,ev=len(per),roi=roi,se=se,hit=hit,exp=exp,odds=sum(r['odds'] for r in G)/n)
rows.sort(key=lambda r:r.get('start') or 0)
cut=rows[len(rows)//2].get('start') or 0
def split(G): return [r for r in G if (r.get('start') or 0)<cut],[r for r in G if (r.get('start') or 0)>=cut]
out=['# Market tape — every market on every fixture (no selection)\n',
 f"{len(rows):,} settled outcomes on {len({r['eid'] for r in rows}):,} fixtures, priced at the earliest pre-match price we stored. Flat 1-unit stake on every outcome. ROI = return per unit staked; SE clustered by fixture. Voids return the stake.\n"]
# 1. calibration by odds band (is SportyBet's own probability honest?)
out.append('\n## 1. Does the house probability match reality? (all outcomes)\n\n| Sport | Odds band | n | Fixtures | House p | Actual win % | ROI | SE |\n|---|---|---|---|---|---|---|---|')
for sp in ('football','basketball'):
    for b in ('<1.30','1.30-1.59','1.60-2.19','2.20-3.99','4.00+'):
        s=stats([r for r in rows if r['sport']==sp and band(r['odds'])==b])
        if s: out.append(f"| {sp} | {b} | {s['n']:,} | {s['ev']:,} | {s['exp']:.3f} | {s['hit']:.3f} | {s['roi']:+.3f} | {s['se']:.3f} |")
# 2. market family level
fam=collections.defaultdict(list)
for r in rows: fam[(r['sport'],FAM.get(r['mid'],r['mid']),side(r))].append(r)
tab=[]
for k,G in fam.items():
    s=stats(G)
    if s and s['ev']>=60: a,b=split(G); s1,s2=stats(a),stats(b); tab.append((k,s,s1,s2))
tab.sort(key=lambda x:-x[1]['roi'])
hdr='| Sport | Market | Side | n | Fixtures | Avg odds | House p | Actual | ROI | SE | Early half | Late half |\n|---|---|---|---|---|---|---|---|---|---|---|---|'
def line(k,s,s1,s2): return f"| {k[0]} | {k[1]} | {k[2]} | {s['n']:,} | {s['ev']:,} | {s['odds']:.2f} | {s['exp']:.3f} | {s['hit']:.3f} | {s['roi']:+.3f} | {s['se']:.3f} | {(s1 or {}).get('roi',0):+.3f} | {(s2 or {}).get('roi',0):+.3f} |"
cand=[t for t in tab if t[1]['roi']-1.5*t[1]['se']>0 and t[2] and t[3] and t[2]['roi']>0 and t[3]['roi']>0]
out.append(f"\n## 2. Candidates: ROI positive by >1.5 SE AND positive in both halves ({len(cand)} of {len(tab)} slices)\n\n"+hdr)
out+= [line(*t) for t in cand] or ['| none | | | | | | | | | | | |']
out.append('\n## 3. Best 30 market slices by ROI (≥60 fixtures)\n\n'+hdr); out+=[line(*t) for t in tab[:30]]
out.append('\n## 4. Worst 20 market slices\n\n'+hdr); out+=[line(*t) for t in tab[-20:]]
# 5. market x odds band x tier for the families we actually bet
fb=collections.defaultdict(list)
for r in rows: fb[(r['sport'],FAM.get(r['mid'],r['mid']),side(r),band(r['odds']),tier(r['lg']))].append(r)
t5=[]
for k,G in fb.items():
    s=stats(G)
    if s and s['ev']>=80:
        a,b=split(G); s1,s2=stats(a),stats(b)
        if s1 and s2 and s1['roi']>0 and s2['roi']>0 and s['roi']-1.5*s['se']>0: t5.append((k,s,s1,s2))
t5.sort(key=lambda x:-(x[1]['roi']/max(x[1]['se'],1e-3)))
out.append(f"\n## 5. Finer slices (market × side × odds band × league tier), stable in both halves, ROI > 1.5 SE ({len(t5)})\n\n| Sport | Market | Side | Band | Tier | n | Fixtures | House p | Actual | ROI | SE | Early | Late |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for k,s,s1,s2 in t5[:40]:
    out.append(f"| {k[0]} | {k[1]} | {k[2]} | {k[3]} | {k[4]} | {s['n']:,} | {s['ev']:,} | {s['exp']:.3f} | {s['hit']:.3f} | {s['roi']:+.3f} | {s['se']:.3f} | {s1['roi']:+.3f} | {s2['roi']:+.3f} |")
n_tests=len(fb)
out.append(f"\n_Multiple-testing note: section 5 searched {n_tests:,} slices; at a 1.5-SE bar roughly {int(n_tests*0.067):,} would pass by chance alone before the both-halves filter. Treat everything here as a hypothesis to forward-test, not a proven edge._")
open('../papertrade/TAPE.md','w').write('\n'.join(out)+'\n')
print('\n'.join(out[:60]))
