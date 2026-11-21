# Architecture and the November 2026 engineering review

## Purpose

Harvest every fixture and market on SportyBet daily, research them independently, settle them after they are played,
and learn continuously from all of it, including fixtures and markets nobody bet on. Selection for tickets comes last.

## Data flow

```
SportyBet API ──harvest──▶ papertrade/tape/*.csv.gz        raw first-seen prices, append-only, committed
Sportradar    ──allform──▶ papertrade/form/*.csv.gz        pre-kick-off trend per market, append-only, committed
AI sessions   ──research─▶ papertrade/research/*.json      team news, vetoes, picks, committed
                    │
              tape_grade.py  (Sportradar results)
                    ▼
        engine/cache/tape_graded/<kick-off day>.jsonl.gz   settled outcomes, rebuildable, NOT committed
                    │
      ┌─────────────┼────────────────┐
 tape_report.py   learn.py      tape_insights.py (ad hoc deep study)
   TAPE.md      learned.json ──▶ build_tickets.py ──▶ SportyBet code ──▶ tickets.txt
                LEARNED.md                                   │
                learning_log.jsonl               settle_tickets.py ──▶ ticket_ledger.jsonl, TICKETS.md, CLASSES.md
```

Design rules:
- **Raw data is append-only and committed; anything derived can be rebuilt.** The graded tape lives in the cache and
  is rebuilt from the tape plus Sportradar by `python3 tape_grade.py all` (about 8 minutes).
- **Predictions are stored before kick-off.** Form trends and research files are written before the games, so grading
  them later cannot be contaminated by the result.
- **Learning has an evidence bar.** `learn.py` only writes a correction that holds in both halves of the period,
  clears 3 standard errors clustered by fixture, and is then shrunk by sample size. Chance findings stay at zero.
- **Nothing fails silently.** Every workflow step runs through `health.py`.
- **Streaming, bounded memory.** Graded rows are grouped by fixture, so reports compute fixture-clustered errors in
  one pass without holding rows in memory.

## Review findings (21 Nov 2026) and what was done

| # | Finding | Effect | Fix |
|---|---|---|---|
| 1 | `tape_grade.py` crashed on the `ft` period key | Grading of the whole board stopped for 16 days | Filter keys before sorting; unit test |
| 2 | Workflow steps ended in `\|\| echo "(non-fatal)"` | The crash above was invisible; runs showed green | `health.py` wrapper, journal line, final failing step |
| 3 | Sportradar lookups made before a match ended were cached for ever | About 1,100 fixtures never got a result | Re-fetch unfinished matches once kick-off is 2h past |
| 4 | Every run re-graded the entire tape and loaded all rows into memory | 27 min and several GB, growing daily | Per-day partitions, last 6 days re-graded, streaming report: under 2 min per night |
| 5 | The workflow re-stored every cached board each run and `tape_store.py` re-read the whole tape | Most of a 29-minute step | Store today's board only; de-duplicate against the last 5 days |
| 6 | `settle_tickets.py` rebuilt the ledger from live fetches | 215 of 294 tickets vanished from the ledger and the ROI table once their codes expired | Permanent `ticket_ledger.jsonl`; 197 tickets recovered from git history; settled tickets are never fetched again |
| 7 | No learning loop: tape insights were applied by hand | The model did not improve by itself | `learn.py` nightly; `build_tickets.py` reads `learned.json` |
| 8 | No stored predictions for unselected fixtures | Research could only be judged on picked legs | `allform.py` writes `papertrade/form/` for every fixture nightly |
| 9 | `fixsim.py` simulated a stale legs file without warning | Two days of simulations were of the wrong board | Refuses stale input; explicit input and output paths |
| 10 | Form trends counted overtime as regulation and volleyball sets as points | Wrong trends in hockey, basketball, volleyball | Those market and sport combinations are skipped |
| 11 | A hung HTTP call could kill a harvest thread pool | Partial harvests | `curl_get` and `curl_post` never raise; curl has its own time limit |
| 12 | A new dated script was written for every ticket day | 13 near-duplicate scripts, gates re-typed each time | One `build_tickets.py`; old scripts moved to `engine/archive/` |
| 13 | No tests, no compile check | Regressions reached the nightly run | `engine/tests/` (20 tests) and `ci.yml` |
| 14 | Ticket codes from a text file went straight into a URL | Malformed input reached the network call | Codes validated against `[A-Z0-9]{4,10}` |
| 15 | Unrelated website files (Netlify, WordPress) in the repository | Confusing, 4.7 MB | Removed |

Security notes: the repository holds no credentials; both APIs are public and unauthenticated. The workflow has
`contents: write` only, and CI has `contents: read`. Subprocess calls pass argument lists, not shell strings, except
`daily.py`, whose commands are fixed strings.

## Known limits and next steps

- **Web research cannot run on GitHub's runners.** Team news needs an AI session. The data research, settlement and
  learning are fully automatic; the web research is graded automatically whenever a session produces it.
- **Repository size.** The tape adds about 7 MB a day and the form files about 1 MB. Prune to monthly archives when
  the repository passes roughly 1 GB.
- **Sample.** The tape starts 12 Oct 2026. Corrections are small and will move as data accumulates;
  `learning_log.jsonl` tracks that movement run by run.
- **Simulation covers football, basketball and baseball only.** Other sports are judged on house price and form.
- `daily.py` and `grade.py` (our own corners, cards and basketball models) are unchanged apart from the health wrapper.
