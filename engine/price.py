import json,re,sys,numpy as np
from anc import fit,grid,devig,K
I=np.arange(K)[:,None]; Jx=np.arange(K)[None,:]; T=I+Jx; Dm=I-Jx
BAD=re.compile(r'women|\bw\b|u1[0-9]|u2[0-3]|youth|reserve|srl|simulated|friendl|amateur|futsal|esoccer|beach|\(w\)|u-?2[01]|academy|ii$| b$',re.I)
def rng(s):
    if s.endswith('+'): return int(s[:-1]),99
    if '-' in s:
        a,b=s.split('-'); return int(a),(99 if b.endswith('+') else int(b))
    return int(s),int(s)
def price(P,o):
    m,spec,d=o['mid'],o['spec'] or '',o['desc']
    win=None;push=None
    if m=='1': win={'Home':I>Jx,'Draw':I==Jx,'Away':I<Jx}.get(d)
    elif m=='10': win={'Home or Draw':I>=Jx,'Home or Away':I!=Jx,'Draw or Away':I<=Jx}.get(d)
    elif m=='11': win={'Home':I>Jx,'Away':I<Jx}.get(d); push=(I==Jx)
    elif m in('18','19','20') and spec.startswith('total='):
        t=float(spec[6:]); x={'18':T,'19':I*np.ones_like(Jx),'20':Jx*np.ones_like(I)}[m]
        win=(x>t) if d.startswith('Over') else (x<t) if d.startswith('Under') else None
        if t==int(t): push=(x==t)
    elif m=='16' and spec.startswith('hcp='):
        h=float(spec[4:])
        if abs(h*2-round(h*2))>1e-9: return None   # quarter lines skipped
        v=Dm+h
        win=(v>0) if d.startswith('Home') else (v<0) if d.startswith('Away') else None
        if h==int(h): push=(v==0)
    elif m=='29': win={'Yes':(I>0)&(Jx>0),'No':(I==0)|(Jx==0)}.get(d)
    elif m=='30': win={'Both teams':(I>0)&(Jx>0),'None':(I==0)&(Jx==0),'Only Home':(I>0)&(Jx==0),'Only Away':(I==0)&(Jx>0)}.get(d)
    elif m in('548','450001','450002','450003'):
        try: a,b=rng(d)
        except: return None
        x={'548':T,'450001':T,'450002':I*np.ones_like(Jx),'450003':Jx*np.ones_like(I)}[m]
        win=(x>=a)&(x<=b)
    if win is None: return None
    pw=float((P*win).sum()); pp=float((P*push).sum()) if push is not None else 0.0
    return pw,pp
from scipy.optimize import brentq
def pdv(*o):
    q=[1/x for x in o]
    k=brentq(lambda k:sum(x**k for x in q)-1,0.5,3)
    return [x**k for x in q]
# v5.1 league goal-bias: (actual - model) on U3.5 from 2024-26 history; negative = Unders overrated
UBIAS={'Norway':-0.014,'Switzerland':-0.045,'Netherlands':-0.010,'Germany':-0.044,'Denmark':-0.060,'USA':-0.037,'China':-0.059}
if __name__=='__main__':
    R=json.load(open(sys.argv[1] if len(sys.argv)>1 else '../m12.json'))
    out=[]
    for r in R:
        if r['sport']!='football' or BAD.search(r['lg']+' '+r['fx']): continue
        mk=r['mk']; g=lambda mid,spec,desc:[o['odds'] for o in mk if o['mid']==mid and (o['spec'] or None)==spec and o['desc']==desc]
        h,d,a=g('1',None,'Home'),g('1',None,'Draw'),g('1',None,'Away'); ov,un=g('18','total=2.5','Over 2.5'),g('18','total=2.5','Under 2.5')
        if not(h and d and a): continue
        marg=1/h[0]+1/d[0]+1/a[0]-1
        pH,pD,pA=devig(h[0],d[0],a[0]); pO=devig(ov[0],un[0])[0] if ov and un else None
        P=grid(*fit(pH,pD,pA,pO))
        for o in mk:
            res=price(P,o)
            if not res: continue
            pw,pp=res
            b=UBIAS.get(r['lg'].split(' / ')[0],0)
            if b and o['mid']=='18' and o['desc'].startswith('Under'): pw=max(pw+b,0)
            if b and o['mid']=='18' and o['desc'].startswith('Over'): pw=min(pw-b,1)
            pl=1-pw-pp
            ev=pw*o['odds']+pp
            out.append(dict(eid=r['eid'],sid=r['sid'],fx=r['fx'],lg=r['lg'],ko=r['ko'],mid=o['mid'],spec=o['spec'],desc=o['desc'],mdesc=o['mdesc'],
                oid=o['oid'],odds=o['odds'],hp=o['p'],pw=pw,pp=pp,pl=pl,ev=ev,marg=marg,o25=bool(pO)))
    json.dump(out,open('cache/priced_goals.json','w'))
    print('events priced',len(set(x['eid'] for x in out)),'outcomes',len(out))
    import collections
    evs=collections.defaultdict(list)
    for x in out:
        if 1.15<=x['odds']<=3: evs[x['mid']].append(x['ev'])
    for m,v in sorted(evs.items(),key=lambda kv:-np.mean(kv[1])): print(f'mid {m:<7} n={len(v):5} mean EV {np.mean(v):.3f}  share EV>=1: {np.mean(np.array(v)>=1):.2f}')
