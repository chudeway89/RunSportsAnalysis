# Tally the expert panel's votes (engine/panel_prompt.txt). A leg is approved when at least 3 seats vote yes and
# at most one seat votes no. Usage: python3 panel_tally.py <cands.json> <approved_out.json> <verdict files...>
import json,sys,collections
cands=json.load(open(sys.argv[1])); out=sys.argv[2]; V=collections.defaultdict(dict)
for f in sys.argv[3:]:
    seat=f.rsplit('_',1)[-1].split('.')[0]
    try:
        for x in json.load(open(f)): V[x['key']][seat]=(x.get('vote'),x.get('reason',''))
    except Exception as e: print('unreadable verdict file',f,e)
ok=[];rows=[]
for l in cands:
    v=V.get(l['key'],{}); y=sum(1 for a,_ in v.values() if a=='yes'); n=sum(1 for a,_ in v.values() if a=='no')
    good=y>=3 and n<=1
    if good: ok.append(l['key'])
    rows.append((good,y,n,l,[f"{s}: {r}" for s,(a,r) in v.items() if a=='no']))
json.dump(ok,open(out,'w'))
print(f'{len(ok)} of {len(cands)} legs approved (>=3 yes, <=1 no)')
for good,y,n,l,nos in sorted(rows,key=lambda r:(-r[0],-r[1],r[2])):
    print(('OK  ' if good else 'CUT ')+f"{y}y/{n}n | {l['fx'][:36]:36} | {(l['mdesc'] or '')[:22]:22} {l['desc'][:14]:14} | {l['odds']:.2f} p{l['p']:.2f}"+(' | '+' ; '.join(nos)[:150] if nos and not good else ''))
