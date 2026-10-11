from counts import *
import sys,itertools
stat=sys.argv[1]; kh,ka=('hc','ac') if stat=='corners' else ('hy','ay')
lines=[8.5,9.5,10.5] if stat=='corners' else [3.5,4.5]
R=[r for r in load_counts() if r[kh] is not None and r[ka] is not None]
by=collections.defaultdict(list)
for r in R: by[r['lg']].append(r)
# precompute folds
folds=[]
for lg,ms in by.items():
    ms.sort(key=lambda m:m['date']); t=dt.datetime(2025,3,1)
    while t<dt.datetime(2026,10,10):
        tr=[m for m in ms if t-dt.timedelta(days=500)<=m['date']<t]; te=[m for m in ms if t<=m['date']<t+dt.timedelta(days=28)]
        if len(tr)>150 and te: folds.append((t,tr,te))
        t+=dt.timedelta(days=28)
clip=lambda q:min(max(q,1e-6),1-1e-6)
def run(prior,half,alpha,rr):
    ll=n=0
    for t,tr,te in folds:
        M=fit(tr,t,kh,ka,half=half,prior=prior); base=sum(m[kh]+m[ka] for m in tr)/len(tr)
        for m in te:
            h,a=mean(M,m['h'],m['a']); mu=alpha*(h+a)+(1-alpha)*base; tot=m[kh]+m[ka]
            for L in lines:
                p=p_over(mu,rr,L); y=tot>L; ll+=-math.log(clip(p) if y else clip(1-p)); n+=1
    return ll/n
base_ll=run(4,150,0.0,30)
print('league-avg baseline',round(base_ll,4))
for prior,half,alpha,rr in itertools.product([10,30],[200,365],[0.5,0.75],[12,30] if stat=='corners' else [15,1000]):
    print(prior,half,alpha,rr,round(run(prior,half,alpha,rr),4))
