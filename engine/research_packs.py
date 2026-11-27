# Split a harvested board into web-research packs for the daily research session (docs/DAILY_RESEARCH.md).
# Every fixture of every harvested sport lands in exactly one pack; packs are grouped by sport and country so one
# researcher covers related leagues, and ordered by earliest kick-off so the soonest games are researched first.
#   python3 research_packs.py <board.json> <allform.json> [pack size=30]
# Writes cache/packs/fx_NN.txt, cache/packs/prompt_NN.txt and prints the pack count. Each researcher writes
# ../papertrade/research/<date>_PNN.json; fixtures already present in a file of that date are skipped (resume).
import json,sys,os,glob,collections,datetime as dt
HERE=os.path.dirname(os.path.abspath(__file__))
board,form=os.path.abspath(sys.argv[1]),os.path.abspath(sys.argv[2]); size=int(sys.argv[3]) if len(sys.argv)>3 else 30
B=json.load(open(board)); today=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')
TAG=os.environ.get('PACKTAG','P')   # e.g. PACKTAG=S for a second board researched in parallel: own pack folder, own file prefix
RD=os.path.join(HERE,'..','papertrade','research'); PD=os.path.join(HERE,'cache','packs' if TAG=='P' else 'packs_'+TAG); os.makedirs(PD,exist_ok=True); os.makedirs(RD,exist_ok=True)
for f in glob.glob(os.path.join(PD,'*')): os.remove(f)
done=set()
for f in glob.glob(os.path.join(RD,f'{today}_*.json')):
    try: done|={x['eid'] for x in json.load(open(f)) if isinstance(x,dict) and x.get('eid')}
    except Exception: pass
now=dt.datetime.now(dt.timezone.utc).timestamp()*1000
R=[e for e in B if e['eid'] not in done and e['start']>now+20*60e3]
by=collections.defaultdict(list)
for e in R: by[(e['sport'],e['lg'])].append(e)
packs=[];cur=[]
for k in sorted(by,key=lambda k:(k[0],k[1].split(' / ')[0],min(e['start'] for e in by[k]))):
    v=sorted(by[k],key=lambda e:e['start'])
    while v:
        room=size-len(cur); cur+=v[:room]; v=v[room:]
        if len(cur)>=size: packs.append(cur);cur=[]
if cur: packs.append(cur)
packs.sort(key=lambda p:min(e['start'] for e in p))
first=len(glob.glob(os.path.join(RD,f'{today}_{TAG}*.json')))
T=open(os.path.join(HERE,'research_prompt.txt')).read()
for i,p in enumerate(packs,1):
    n=f'{first+i:02d}'; fx=os.path.join(PD,f'fx_{n}.txt'); out=os.path.abspath(os.path.join(RD,f'{today}_{TAG}{n}.json'))
    with open(fx,'w') as f:
        for e in sorted(p,key=lambda e:e['start']): f.write(f"{e['eid']} | {e['ko']} | {e['sport']} | {e['lg']} | {e['fx']}\n")
    open(os.path.join(PD,f'prompt_{n}.txt'),'w').write(T.replace('{FX}',fx).replace('{BOARD}',board).replace('{FORM}',form).replace('{OUT}',out).replace('{TODAY}',today))
print(f'{len(R)} fixtures to research in {len(packs)} packs ({len(done)} already researched today); prompts in {PD}')
print(collections.Counter(e['sport'] for e in R).most_common())
