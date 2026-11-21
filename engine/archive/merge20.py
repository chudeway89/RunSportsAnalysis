import json,glob
auto={a['eid']:a for a in json.load(open('cache/auto20.json'))}
res={}
for f in sorted(glob.glob('cache/factors20_G*.json'))+sorted(glob.glob('cache/factorsNONE_G*.json')):
    try:
        for r in json.load(open(f)): res[r['eid']]=r
    except Exception as ex: print('bad',f,ex)
out=[]
for eid in auto:
    a=auto[eid]; r=res.get(eid)
    if r:
        m=dict(r); m['flags']=sorted(set(r.get('flags',[]))|set(a.get('flags',[])))
        if not m.get('confidence'): m['confidence']=a.get('confidence',0)
        m['researched']=True
    else: m=dict(a); m['researched']=False
    out.append(m)
json.dump(out,open('cache/factors_all_1020.json','w'))
print('merged',len(out),'researched',sum(1 for o in out if o['researched']))
