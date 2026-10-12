# DAILY PAPER-TRADE RUN (scheduled ~22:50 Africa/Lagos). Run from engine/:  python3 daily.py
# 1 refresh data  2 harvest SportyBet board (next 30h)  3 grow Sportradar histories  4 price corners/cards/basketball/baseball
# 5 save papertrade/<date>_snapshot.json  6 grade all past snapshots  7 write papertrade/<date>_picks.md + LOG.md line
import subprocess,json,datetime as dt,glob,os,collections,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FAIL=[]; T0=dt.datetime.utcnow()
D=dt.datetime.utcnow().strftime('%Y-%m-%d'); BF=f'cache/board_{D}.json'
def run(c,t=3000):
    print('>>',c,flush=True)
    try:
        if subprocess.run(c,shell=True,timeout=t).returncode: FAIL.append(c)
    except subprocess.TimeoutExpired: print('TIMEOUT',c); FAIL.append('TIMEOUT '+c)
for f in glob.glob('cache/priced_*.json'): os.remove(f)
run('./fd_fetch.sh'); run('python3 board.py 30')
run(f'python3 sr_football.py {BF}'); run(f'python3 sr_scores.py {BF}'); run('python3 hoops_sr.py')
run(f'python3 live_counts.py {BF}'); run(f'python3 live_sr_counts.py {BF}'); run(f'python3 live_sports.py {BF}')
K=['eid','sid','sport','lg','fx','ko','mid','spec','desc','oid','odds','hp','mp','ev','src','line']
snap=[]
for f in glob.glob('cache/priced_*.json'):
    for x in json.load(open(f)):
        if 1.15<=x['odds']<=5: x.setdefault('sport','football'); snap.append({k:(round(x[k],4) if isinstance(x.get(k),float) else x.get(k)) for k in K})
json.dump(snap,open(f'../papertrade/{D}_snapshot.json','w'))
run('python3 grade.py')
# shortlist (PAPER ONLY until a market passes the grade criteria): best model-EV leg per event, odds 1.25-2.5
best={}
for x in snap:
    if 1.25<=x['odds']<=2.5 and (x['eid'] not in best or x['ev']>best[x['eid']]['ev']): best[x['eid']]=x
top=sorted(best.values(),key=lambda x:-x['ev'])[:25]
by=collections.Counter((x['sport'],x['mid']) for x in snap)
md=[f'# Paper-trade picks {D} (model EV, NOT staked)','',f'Snapshot: {len(snap)} priced outcomes on {len(set(x["eid"] for x in snap))} events.  By market: '+', '.join(f'{s}/{m}:{n}' for (s,m),n in by.most_common()),'',
    '| KO (UTC) | Fixture | League | Market | Pick | Odds | Model p | House p | EV | Source |','|---|---|---|---|---|---|---|---|---|---|']
md+=[f"| {x['ko']} | {x['fx']} | {x['lg']} | {x['mid']} {x['spec'] or ''} | {x['desc']} | {x['odds']} | {x['mp']:.3f} | {x['hp']:.3f} | {x['ev']:.3f} | {x['src']} |" for x in top]
md+=['','## Grade report (all snapshots to date)','```',open('../papertrade/grade_report.txt').read() if os.path.exists('../papertrade/grade_report.txt') else 'none yet','```']
open(f'../papertrade/{D}_picks.md','w').write('\n'.join(md)+'\n')
gr=open('../papertrade/grade_report.txt').readline().strip() if os.path.exists('../papertrade/grade_report.txt') else ''
open('../papertrade/LOG.md','a').write(f'- {D}: snapshot {len(snap)} outcomes / {len(best)} events; {gr}\n')
# heartbeat: lets the workflow / any monitor see at a glance whether today's run really did its job
ok=os.path.exists(BF) and len(snap)>=200
st=dict(date=D,started=f'{T0:%Y-%m-%d %H:%M}',finished=f'{dt.datetime.utcnow():%Y-%m-%d %H:%M}',snapshot_outcomes=len(snap),
        events=len(set(x['eid'] for x in snap)),failed_steps=FAIL,graded_line=gr,ok=ok)
json.dump(st,open('../papertrade/status.json','w'),indent=1)
print('DONE' if ok else 'FAILED',D,len(snap),FAIL)
sys.exit(0 if ok else 1)
