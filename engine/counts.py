# Count-stat model (corners, cards): team for/against strengths with time decay + negative binomial
import csv,glob,math,collections,datetime as dt
from scipy.stats import nbinom,poisson
def f(x):
    try: return float(x)
    except: return None
def load_counts():
    rows=[]
    for fn in glob.glob('*_2*.csv'):
        lg=fn.split('_')[0]
        for r in csv.DictReader(open(fn,encoding='utf-8-sig',errors='ignore')):
            if not r.get('FTHG') or r.get('HC') in (None,''): continue
            try: d=dt.datetime.strptime(r['Date'],'%d/%m/%Y' if len(r['Date'])==10 else '%d/%m/%y')
            except: continue
            rows.append(dict(lg=lg,date=d,h=r['HomeTeam'],a=r['AwayTeam'],hc=f(r['HC']),ac=f(r['AC']),
              hy=f(r.get('HY')),ay=f(r.get('AY')),hr=f(r.get('HR')),ar=f(r.get('AR')),ref=r.get('Referee',''),
              hg=f(r['FTHG']),ag=f(r['FTAG'])))
    return [r for r in rows if r['hc'] is not None and r['ac'] is not None]
def fit(ms,ref,kh,ka,half=150,prior=4,iters=25):
    w=[math.exp(-math.log(2)*(ref-m['date']).days/half) for m in ms]
    T=set(m['h'] for m in ms)|set(m['a'] for m in ms)
    sw=sum(w); mh=sum(wi*m[kh] for wi,m in zip(w,ms))/sw; ma=sum(wi*m[ka] for wi,m in zip(w,ms))/sw
    F={t:1.0 for t in T}; A={t:1.0 for t in T}
    for _ in range(iters):
        nf=collections.defaultdict(float); df=collections.defaultdict(float)
        for wi,m in zip(w,ms):
            nf[m['h']]+=wi*m[kh]; df[m['h']]+=wi*mh*A[m['a']]
            nf[m['a']]+=wi*m[ka]; df[m['a']]+=wi*ma*A[m['h']]
        F={t:(nf[t]+prior)/(df[t]+prior) for t in T}
        na=collections.defaultdict(float); da=collections.defaultdict(float)
        for wi,m in zip(w,ms):
            na[m['a']]+=wi*m[kh]; da[m['a']]+=wi*mh*F[m['h']]
            na[m['h']]+=wi*m[ka]; da[m['h']]+=wi*ma*F[m['a']]
        A={t:(na[t]+prior)/(da[t]+prior) for t in T}
    # dispersion of match TOTAL via method of moments on residual variance
    res=[];mus=[]
    for wi,m in zip(w,ms):
        mu=mh*F[m['h']]*A[m['a']]+ma*F[m['a']]*A[m['h']]
        res.append((m[kh]+m[ka]-mu)**2); mus.append(mu)
    var=sum(res)/len(res); mu_bar=sum(mus)/len(mus)
    over=max(var-mu_bar,1e-6); r=mu_bar**2/over   # NB size parameter
    return dict(F=F,A=A,mh=mh,ma=ma,r=r)
def mean(M,h,a):
    return (M['mh']*M['F'].get(h,1)*M['A'].get(a,1), M['ma']*M['F'].get(a,1)*M['A'].get(h,1))
def p_over(mu,r,line):
    # P(total > line) under NB(mean mu, size r)
    p=r/(r+mu); k=math.floor(line)
    return 1-nbinom.cdf(k,r,p)
def p_team_over(mu,r,line):
    p=r/(r+mu); return 1-nbinom.cdf(math.floor(line),r,p)
