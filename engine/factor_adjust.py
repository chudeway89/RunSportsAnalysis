# Live use of the factor study (factor_coefs.json 'inc'): multipliers for team goals / corners / cards from the factors
# that the existing pricers do NOT already use.  Team names are football-data names (fdcsv).  Missing feature -> neutral.
#   from factor_adjust import mult;  mult('E0','Arsenal','Chelsea',home=True) -> {'y_g':1.01,'y_c':0.99,'y_y':1.03}
import json,math,collections
import factors as F
C=json.load(open('factor_coefs.json'))['inc']
_R=F.load(); F.build(_R); HIST,TAB=F.STATE
SEASON={}
for (lg,s,t) in TAB: SEASON[lg]=max(SEASON.get(lg,''),s)
def _m(L,k,n):
    v=[x[k] for x in L[-n:] if x[k] is not None]
    return sum(v)/len(v) if len(L)>=min(n,5) and v else None
def _rank(lg,t):
    s=SEASON.get(lg); me=TAB.get((lg,s,t))
    if not me or me['n']<5: return None
    ks=[k for k in TAB if k[0]==lg and k[1]==s]; key=lambda k:(TAB[k]['p']/TAB[k]['n'],TAB[k]['gd']/TAB[k]['n']) if TAB[k]['n'] else (0,0)
    o=sorted((key(k) for k in ks),reverse=True); return o.index(key((lg,s,t)))/max(len(o)-1,1)
def team(lg,t):
    H=HIST.get(t,[]); gf,sot=_m(H,'gf',10),_m(H,'sotf',10)
    return dict(gf10=gf,sotf10=sot,sota10=_m(H,'sota',10),ga5=_m(H,'ga',5),pts5=_m(H,'pts',5),fouls10=_m(H,'ff',10),
                fin10=(gf-0.30*sot) if gf is not None and sot is not None else None,rank=_rank(lg,t))
def feats(lg,t,o):
    a,b=team(lg,t),team(lg,o)
    return dict(sotf10=a['sotf10'],o_sota10=b['sota10'],o_ga5=b['ga5'],fin10=a['fin10'],gf10=a['gf10'],rank=a['rank'],
                o_rank=b['rank'],pts5=a['pts5'],o_pts5=b['pts5'],fouls10=a['fouls10'],o_fouls10=b['fouls10'])
CAP={'y_g':(0.95,1.05),'y_c':(0.92,1.08),'y_y':(0.85,1.15)}
def mult(lg,t,o,home=True):
    x=feats(lg,t,o); out={}
    for k,c in C.items():
        s=0.0
        for fe,b in zip(c['feats'],c['beta']):
            if x.get(fe) is not None: m,sd=c['stats'][fe]; s+=b*(x[fe]-m)/sd
        lo,hi=CAP[k]; out[k]=min(max(math.exp(s),lo),hi)
    return out
if __name__=='__main__':
    import sys
    print(mult(*(sys.argv[1:4] if len(sys.argv)>3 else ('E0','Arsenal','Chelsea'))))
