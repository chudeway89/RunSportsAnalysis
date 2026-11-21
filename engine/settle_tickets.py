# Deterministic ticket settlement, run by the scheduled workflow after grading (no Claude session needed).
# Reads papertrade/tickets.txt ("CODE  YYYY-MM-DD  label" per line), re-fetches every share code from SportyBet,
# and rewrites papertrade/TICKETS.md with each ticket's W/L/V/pending count, status and the legs that lost.
# Settlement semantics (CLAUDE.md L16/L24/L71): isWinning=1 won; isWinning=0 with refundFactor>0 void; else lost.
import json,os,datetime as dt,sys,collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,'.')
from post_lib import curl_get
T,M='../papertrade/tickets.txt','../papertrade/TICKETS.md'
# Persistent leg ledger: share codes expire after ~10 days, so every leg is kept in papertrade/legs.jsonl with the odds and
# house probability first seen (= posting price; later fetches show drifted odds, L47) and its result once settled.
LJ='../papertrade/legs.jsonl'
LEGS={}
if os.path.exists(LJ):
    for l in open(LJ): r=json.loads(l); LEGS[r['key']]=r
def leg_class(sport,mid,spec,desc):
    d=desc or ''; line=spec.split('=')[-1] if spec and '=' in spec else ''
    if mid in('18','19','20','225','258'):
        side='Over' if d.startswith('Over') else 'Under'
        try: integer=float(line)%1==0
        except ValueError: integer=False
        return f"{'team ' if mid in('19','20') else ''}{side}{' integer' if integer else ''}"+(' (bball)' if mid=='225' else '')
    if mid in('16','223'):
        try: h=float(d.split('(')[1].rstrip(')'))
        except Exception: h=0
        return ('bball ' if mid=='223' else '')+('AH catch +'+('0.5-1' if h<=1 else '1.5' if h==1.5 else '2+') if h>0 else f'AH give {h:g}')
    return {'1':'1X2 '+d,'11':'DNB','10':'Double Chance','219':'bball ML','251':'MLB ML','256':'MLB run-line','50':'GG/BTTS','51':'GG/BTTS',
            '450001':'Goal Bounds','450002':'Goal Bounds team','450003':'Goal Bounds team','166':'corners','139':'cards'}.get(mid,'other m'+str(mid))
# Ticket ledger: a settled ticket (WON/DEAD) is final, so it is stored once in papertrade/ticket_ledger.jsonl and never
# fetched again. Before Nov 21 the ledger was rebuilt from live fetches only, so every ticket whose share code had
# expired dropped out of the table and of the ROI figures (215 of 294). History was recovered from git.
import re,itertools
TL='../papertrade/ticket_ledger.jsonl'
LED={}
if os.path.exists(TL):
    for l in open(TL):
        if l.strip(): r=json.loads(l); LED[r['code']]=r
CODE=re.compile(r'^[A-Z0-9]{4,10}$')
rows,tot=[],collections.Counter()
def row(t):
    res=f"{t['W']}W/{t['L']}L/{t['V']}V/{t['P']}P" if t.get('legs') else '–'
    st={'WON':'**WON**'}.get(t['status'],t['status'])
    return f"| {t['day']} | {t['code']} | {t['label']} | {t.get('legs') or '–'} | {res} | {st} | {t.get('lost','')} |"
for line in itertools.chain(open(T),open('../papertrade/singles.txt') if os.path.exists('../papertrade/singles.txt') else []):
    line=line.split('#')[0].strip()
    if not line: continue
    code,*rest=line.split(); day=rest[0] if rest else '?'; lab=' '.join(rest[1:])  # tolerate a bare code (Oct 28 bug)
    if not CODE.match(code): print('skipping malformed code',repr(code)[:20]); continue   # codes go into a URL
    t=LED.get(code)
    if t and t['status'] in ('WON','DEAD'):
        t.update(day=day,label=lab); rows.append(row(t)); tot[t['status']]+=1; continue
    resp=curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}')
    d=(resp or {}).get('data')
    if not d:
        if t:    # seen before, now expired or unreachable: keep what we knew
            if resp: t['status']='EXPIRED' if t['status']=='ALIVE' else t['status']
            t.update(day=day,label=lab); rows.append(row(t)); tot[t['status']]+=1
        else:
            LED[code]=t=dict(code=code,day=day,label=lab,legs=0,W=0,L=0,V=0,P=0,status='N/A',lost='',ret=None,source='never seen live')
            rows.append(row(t)); tot['N/A']+=1
        continue
    W=L=V=P=0; lost=[]; ret=1.0
    for o in d.get('outcomes',[]):
        mk=o['markets'][0]; oc=mk['outcomes'][0]; w=oc.get('isWinning'); rf=float(oc.get('refundFactor') or 0)
        key=f"{o['eventId']}|{mk['id']}|{mk.get('specifier') or ''}|{oc['id']}"
        r=LEGS.setdefault(key,dict(key=key,first_code=code,posted=day,ko=o.get('estimateStartTime'),sport=(o.get('sport') or {}).get('id'),
            lg=((o.get('sport') or {}).get('category') or {}).get('name','')+' / '+(((o.get('sport') or {}).get('category') or {}).get('tournament') or {}).get('name',''),
            fx=f"{o['homeTeamName']} v {o['awayTeamName']}",mid=str(mk['id']),spec=mk.get('specifier') or '',pick=oc.get('desc'),
            odds=float(oc.get('odds') or 0),hp=float(oc.get('probability') or 0),res=None))
        if w is not None: r['score']=o.get('setScore')
        if w==1: r['res']='W'; W+=1; ret*=r['odds']
        elif w==0 and rf>0: r['res']='V'; V+=1
        elif w==0:
            r['res']='L'; L+=1; lost.append(f"{o['homeTeamName']} v {o['awayTeamName']} — {mk.get('desc')} {oc['desc']} ({o.get('setScore')})")
        else: P+=1
    st='DEAD' if L else ('ALIVE' if P else 'WON')
    LED[code]=t=dict(code=code,day=day,label=lab,legs=W+L+V+P,W=W,L=L,V=V,P=P,status=st,lost='; '.join(lost),
                     ret=(round(ret,3) if st=='WON' else 0.0 if st=='DEAD' else None),source='live')
    rows.append(row(t)); tot[st]+=1
with open(TL+'.tmp','w') as f:
    for t in LED.values(): f.write(json.dumps(t)+'\n')
os.replace(TL+'.tmp',TL)
roi=[(t['legs'],t['status'],t['ret']) for t in LED.values() if t['status'] in ('WON','DEAD') and t.get('ret') is not None]
unk=sum(1 for t in LED.values() if t['status']=='WON' and t.get('ret') is None)
now=dt.datetime.utcnow()
out=['# Ticket ledger (auto-settled)','',
     f'Written by `engine/settle_tickets.py` on every scheduled run. Last update {now:%Y-%m-%d %H:%M} UTC. '
     f"Totals: {tot['WON']} won · {tot['DEAD']} dead · {tot['ALIVE']} alive · {tot['EXPIRED']} expired before settling · {tot['N/A']} never seen live.",'',
     f'## Return per 1-unit stake (all settled tickets, from papertrade/ticket_ledger.jsonl; odds as first seen; {unk} early wins with unrecorded odds left out)','','| Ticket size | Tickets | Won | Staked | Returned | ROI |','|---|---|---|---|---|---|',
     *[f"| {nm} | {len(g)} | {sum(x[1]=='WON' for x in g)} | {len(g)} | {sum(x[2] for x in g):.1f} | {100*(sum(x[2] for x in g)/len(g)-1):+.0f}% |"
       for nm,g in (('1-7 legs',[x for x in roi if x[0]<=7]),('8-12 legs',[x for x in roi if 8<=x[0]<=12]),('13+ legs',[x for x in roi if x[0]>=13])) if g],'',
     '| Date | Code | Ticket | Legs | Result | Status | Losing legs |','|---|---|---|---|---|---|---|',*rows,'']
open(M,'w').write('\n'.join(out)); print('\n'.join(out[:4]))
open(LJ,'w').write(''.join(json.dumps(r)+'\n' for r in LEGS.values()))
# Class scorecard: every lesson is measured from here, not from memory (weekday = Mon-Thu, weekend = Fri-Sun, Lagos time)
C=collections.defaultdict(lambda:collections.Counter())
for r in LEGS.values():
    if r['res'] is None or not r.get('ko'): continue
    k=dt.datetime.utcfromtimestamp(r['ko']/1000)+dt.timedelta(hours=1)
    grp='weekend' if k.weekday()>=4 else 'weekday'
    cl=leg_class(r['sport'],r['mid'],r['spec'],r['pick'])
    p=r['hp'] if 0<r['hp']<1 else (0.95/r['odds'] if r['odds'] else 0)
    for g in (grp,'all'):
        c=C[(cl,g)]; c[r['res']]+=1
        if r['res']!='V': c['exp']+=p
out=['# Leg-class scorecard (auto)','',f'From `papertrade/legs.jsonl` ({len(LEGS)} unique legs). Expected = house probability at first sighting. '
     'A class whose actual win rate sits well below expected over 30+ decided legs is a candidate pick.py gate.','',
     '| Class | Split | Decided | W | L | V | Win % | Expected % | Gap (pp) |','|---|---|---|---|---|---|---|---|---|']
for (cl,g),c in sorted(C.items(),key=lambda kv:(-sum(kv[1][x] for x in 'WL'),kv[0])):
    n=c['W']+c['L']
    if n<3: continue
    out.append(f"| {cl} | {g} | {n} | {c['W']} | {c['L']} | {c['V']} | {100*c['W']/n:.0f} | {100*c['exp']/n:.0f} | {100*(c['W']-c['exp'])/n:+.0f} |")
open('../papertrade/CLASSES.md','w').write('\n'.join(out)+'\n')
