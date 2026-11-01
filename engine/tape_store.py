# Keep the FULL board harvest (every fixture, every score-settleable market) as a compact, committed tape:
#   papertrade/tape/<date>.csv.gz   columns: eid,sport,lg,fx,start,mid,mdesc,spec,desc,oid,odds,hp
# Player props (8002xx/77x) are dropped (not settleable from the score). Usage: python3 tape_store.py cache/board_<date>.json
import json,sys,os,gzip,csv,re
f=sys.argv[1]; d=re.search(r'(\d{4}-\d{2}-\d{2})',f); d=d[1] if d else os.path.basename(f)[6:-5]
os.makedirs('../papertrade/tape',exist_ok=True)
out=f'../papertrade/tape/{d}.csv.gz'
ev=json.load(open(f)); ev=ev if isinstance(ev,list) else ev.get('events',[])
SKIP=re.compile(r'^(8002\d\d|80009\d|77\d|900[0-9]{3})$')
KEEP_900={'900036','900037','900038','900052','900029','900030','900031','900032','900300','900301'}
seen=set(); n=0
if os.path.exists(out):
    with gzip.open(out,'rt') as g:
        for r in csv.reader(g): seen.add((r[0],r[5],r[7],r[9]))
with gzip.open(out,'at',newline='') as g:
    w=csv.writer(g)
    for e in ev:
        for o in e.get('mk',[]):
            m=o['mid']
            if SKIP.match(m) and m not in KEEP_900: continue
            k=(e['eid'],m,o.get('spec') or '',o['oid'])
            if k in seen or not o.get('odds'): continue
            seen.add(k); n+=1
            w.writerow([e['eid'],e['sport'],e.get('lg'),e.get('fx'),e.get('start'),m,o.get('mdesc'),o.get('spec') or '',o['desc'],o['oid'],o['odds'],o.get('p')])
print('tape',out,'+',n,'outcomes')
