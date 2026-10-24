# Deterministic ticket settlement, run by the scheduled workflow after grading (no Claude session needed).
# Reads papertrade/tickets.txt ("CODE  YYYY-MM-DD  label" per line), re-fetches every share code from SportyBet,
# and rewrites papertrade/TICKETS.md with each ticket's W/L/V/pending count, status and the legs that lost.
# Settlement semantics (CLAUDE.md L16/L24/L71): isWinning=1 won; isWinning=0 with refundFactor>0 void; else lost.
import json,os,datetime as dt,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,'.')
from post_lib import curl_get
T,M='../papertrade/tickets.txt','../papertrade/TICKETS.md'
rows,tot=[],{'WON':0,'DEAD':0,'ALIVE':0,'N/A':0}
for line in open(T):
    line=line.split('#')[0].strip()
    if not line: continue
    code,day,*lab=line.split(); lab=' '.join(lab)
    d=(curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}') or {}).get('data')
    if not d:
        rows.append(f'| {day} | {code} | {lab} | – | – | N/A (expired) | |'); tot['N/A']+=1; continue
    W=L=V=P=0; lost=[]
    for o in d.get('outcomes',[]):
        oc=o['markets'][0]['outcomes'][0]; w=oc.get('isWinning'); rf=float(oc.get('refundFactor') or 0)
        if w==1: W+=1
        elif w==0 and rf>0: V+=1
        elif w==0:
            L+=1; lost.append(f"{o['homeTeamName']} v {o['awayTeamName']} — {o['markets'][0].get('desc')} {oc['desc']} ({o.get('setScore')})")
        else: P+=1
    st='DEAD' if L else ('ALIVE' if P else 'WON'); tot[st]+=1
    rows.append(f"| {day} | {code} | {lab} | {W+L+V+P} | {W}W/{L}L/{V}V/{P}P | {'**WON**' if st=='WON' else st} | {'; '.join(lost)} |")
now=dt.datetime.utcnow()
out=['# Ticket ledger (auto-settled)','',
     f'Written by `engine/settle_tickets.py` on every scheduled run. Last update {now:%Y-%m-%d %H:%M} UTC. '
     f"Totals: {tot['WON']} won · {tot['DEAD']} dead · {tot['ALIVE']} alive · {tot['N/A']} expired.",'',
     '| Date | Code | Ticket | Legs | Result | Status | Losing legs |','|---|---|---|---|---|---|---|',*rows,'']
open(M,'w').write('\n'.join(out)); print('\n'.join(out[:4]))
