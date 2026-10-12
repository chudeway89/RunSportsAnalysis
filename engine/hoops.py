# Basketball engine: (1) residual spread of totals/margins around the market line, (2) walk-forward team model
# used to transfer that spread to leagues without odds history (scale = market SD / model SD measured on NBA/WNBA).
import json,datetime as dt,numpy as np,collections
def team_model(games,ref,half=120,lam=3.0):
    """games: list of dict(date,h,a,hs,as_). Returns predictor (h,a)->(exp home pts, exp away pts)."""
    T=sorted(set(g['h'] for g in games)|set(g['a'] for g in games)); ix={t:i for i,t in enumerate(T)}; n=len(T)
    rows=[];y=[];w=[]
    for g in games:
        wt=0.5**((ref-g['date']).days/half)
        for att,dfn,pts,home in ((g['h'],g['a'],g['hs'],1),(g['a'],g['h'],g['as_'],0)):
            r=np.zeros(2*n+2); r[0]=1; r[1]=home; r[2+ix[att]]=1; r[2+n+ix[dfn]]=1
            rows.append(r); y.append(pts); w.append(wt)
    X=np.array(rows);Y=np.array(y);W=np.sqrt(np.array(w))
    P=np.eye(2*n+2)*lam; P[0,0]=P[1,1]=0
    b=np.linalg.solve((X*W[:,None]**2).T@X+P,(X*W[:,None]**2).T@Y)
    def pred(h,a):
        ah=b[2+ix[h]] if h in ix else 0; aa=b[2+ix[a]] if a in ix else 0
        dh=b[2+n+ix[h]] if h in ix else 0; da=b[2+n+ix[a]] if a in ix else 0
        return b[0]+b[1]+ah+da, b[0]+aa+dh
    return pred
def walk(games,step=7,min_train=60,window=400):
    games=sorted(games,key=lambda g:g['date']); out=[]
    t=games[min(min_train,len(games)-1)]['date']
    while t<=games[-1]['date']:
        tr=[g for g in games if t-dt.timedelta(days=window)<=g['date']<t]; te=[g for g in games if t<=g['date']<t+dt.timedelta(days=step)]
        if len(tr)>=min_train and te:
            p=team_model(tr,t)
            for g in te: eh,ea=p(g['h'],g['a']); out.append((g,eh,ea))
        t+=dt.timedelta(days=step)
    return out
