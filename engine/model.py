import math,collections,datetime as dt
from load import load
def pois(k,l): return math.exp(-l)*l**k/math.factorial(k)
def fit(matches, ref, half=120, iters=30):
    # time-decayed Poisson attack/defence per league, iterative (Maher-style), with home adv
    w=[math.exp(-math.log(2)*(ref-m['date']).days/half) for m in matches]
    teams=set([m['h'] for m in matches]+[m['a'] for m in matches])
    att={t:1.0 for t in teams}; de={t:1.0 for t in teams}
    sw=sum(w); mh=sum(wi*m['hg'] for wi,m in zip(w,matches))/sw; ma=sum(wi*m['ag'] for wi,m in zip(w,matches))/sw
    for _ in range(iters):
        na=collections.defaultdict(float); da=collections.defaultdict(float)
        for wi,m in zip(w,matches):
            na[m['h']]+=wi*m['hg']; da[m['h']]+=wi*mh*de[m['a']]
            na[m['a']]+=wi*m['ag']; da[m['a']]+=wi*ma*de[m['h']]
        att={t:(na[t]+2*1.0)/(da[t]+2) for t in teams}   # shrink toward 1 (2 pseudo-games)
        nd=collections.defaultdict(float); dd=collections.defaultdict(float)
        for wi,m in zip(w,matches):
            nd[m['a']]+=wi*m['hg']; dd[m['a']]+=wi*mh*att[m['h']]
            nd[m['h']]+=wi*m['ag']; dd[m['h']]+=wi*ma*att[m['a']]
        de={t:(nd[t]+2)/(dd[t]+2) for t in teams}
    return dict(att=att,de=de,mh=mh,ma=ma)
def probs(M,h,a,rho=-0.06):
    lh=M['mh']*M['att'].get(h,1)*M['de'].get(a,1); la=M['ma']*M['att'].get(a,1)*M['de'].get(h,1)
    P={}
    for i in range(11):
        for j in range(11):
            p=pois(i,lh)*pois(j,la)
            if i==0 and j==0: p*=1-lh*la*rho
            elif i==0 and j==1: p*=1+lh*rho
            elif i==1 and j==0: p*=1+la*rho
            elif i==1 and j==1: p*=1-rho
            P[(i,j)]=p
    s=sum(P.values()); P={k:v/s for k,v in P.items()}
    return P,lh,la
def mk(P):
    g=lambda f:sum(v for k,v in P.items() if f(*k))
    return dict(H=g(lambda i,j:i>j),D=g(lambda i,j:i==j),A=g(lambda i,j:i<j),
      O15=g(lambda i,j:i+j>=2),O25=g(lambda i,j:i+j>=3),U35=g(lambda i,j:i+j<=3),U45=g(lambda i,j:i+j<=4))
