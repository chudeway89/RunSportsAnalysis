# Daily research session (scheduled, runs on Opus 5.5)

Goal: web research (team news, absences, context, date and venue conflicts) on **every fixture of every sport the
harvest lists**, stored before kick-off in `papertrade/research/`, so `engine/learn.py` can grade it the next night.
This session builds no tickets and posts nothing to SportyBet.

Work on branch `claude/sports-accumulator-analysis-8su67` only (`git checkout` it, `git pull`).

1. **Harvest and data research (no AI needed, about 10 minutes):**
   ```
   cd engine && pip install -q numpy scipy
   python3 -W ignore tape_harvest.py 30
   B=cache/tapeboard_$(date -u +%F).json
   python3 -W ignore allform.py $B cache/allform_day.json ../papertrade/form/$(date -u +%F_%H%M)_session.csv.gz
   python3 research_packs.py $B cache/allform_day.json 30
   ```
   `research_packs.py` prints the number of packs and writes `cache/packs/prompt_NN.txt`. It skips fixtures that
   already have an entry in today's research files, so the session can be re-run after an interruption.
2. **Research every pack.** For each `prompt_NN.txt`, start one background agent (`subagent_type: general-purpose`,
   `model: opus`) with the prompt: "Read <absolute path of prompt_NN.txt> and follow it exactly. It is your full task."
   - At most **6 agents running at once**; start the next pack each time one finishes. Packs are already ordered by
     earliest kick-off.
   - Do not cut, sample or prioritise fixtures: every pack is researched.
3. **Save as you go.** After every 6 finished packs: `git add papertrade/research papertrade/form papertrade/tape &&
   git commit -m "daily research <date>: packs a-b" && git pull --no-rebase --no-edit && git push`. If the session
   is cut short by a usage limit, what was researched is already saved.
4. **Finish.** When all packs are done, commit and push, then reply with: fixtures researched, packs, vetoes found
   (with reasons), and any pack that failed. If a pack's file is missing or has fewer entries than its fixture list,
   re-run that pack once.

Rules: never invent facts; a fixture with nothing found gets "no news found". Research files are never edited after
kick-off.
