#!/bin/sh
# ONE-RUN DAY BUILD, step 1 of 2. Deterministic, no LLM tokens: harvest -> baselines -> Sportradar form -> research shortlist.
# Usage (from engine/):  ./daypack.sh <tag e.g. 24> [end hour UTC, default 23]
# Then: research the shortlist printed at the end (inline extended WebSearch, see CLAUDE.md "ONE-RUN DAY PROTOCOL"),
# write cache/factors<tag>_G5.json, dry-run daypost.py, then POST=1.
set -e
TAG=$1; END=${2:-23}
python3 -c "import scipy" 2>/dev/null || pip install -q scipy numpy pandas
mkdir -p cache data
H=$(python3 -c "import datetime as d;n=d.datetime.utcnow();e=n.replace(hour=$END,minute=0);print(max(1,round((e-n).total_seconds()/3600,2)))")
python3 -W ignore board.py "$H"
B=cache/board_$(date -u +%Y-%m-%d).json
python3 -W ignore winmodel.py base "$B" "$B" && cp cache/baseline.json cache/baseline17.json
python3 -W ignore autoform.py "$B" cache/auto$TAG.json
python3 -W ignore - "$B" "$TAG" <<'EOF'
import json,re,sys,time,datetime as dt
B=json.load(open(sys.argv[1])); tag=sys.argv[2]
W=re.compile(r'England / (Premier League|Championship|League One)|Spain / LaLiga|Italy / Serie A$|Germany / (Bundesliga|2\. Bundesliga)|France / Ligue 1|Netherlands / Eredivisie|Portugal / Liga Portugal$|Scotland / Premiership|Belgium / Pro League|Turkiye / Super Lig|Brazil / Brasileiro Serie A|Argentina / Liga Profesional|USA / MLS|Mexico / Liga MX|Saudi Arabia / Saudi Pro|Greece / Super League$|Austria / Bundesliga|Switzerland / Super League|Denmark / Superliga|Czechia / 1. Liga|Poland / Ekstraklasa|Japan / J.League$|NBA|Euroleague|Spain / ACB|Turkiye / Super Ligi',re.I)
S=[dict(eid=e['eid'],fx=e['home']+' v '+e['away'],lg=e['lg'],ko=dt.datetime.utcfromtimestamp(e['start']/1000).strftime('%m-%d %H:%M'),sport=e['sport'])
   for e in sorted(B,key=lambda e:e['start']) if e['start']>=time.time()*1000+40*60e3 and W.search(e['lg']) and 'women' not in e['lg'].lower()]
json.dump(S,open(f'cache/r{tag}_G1.json','w'),indent=0)
print(len(S),'screened fixtures in data-rich competitions -> cache/r%s_G1.json (SCREEN list)'%tag)
EOF
echo "next: SCREEN='cache/r${TAG}_G*.json' python3 daypost.py $TAG $B 500 5000 50000 max   (dry run; research the T500/MAIN legs it prints)"
