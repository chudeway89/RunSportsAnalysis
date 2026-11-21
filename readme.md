# SportyBet learning engine

This repository does one thing: it watches **every fixture and every market SportyBet Nigeria lists**, researches them,
settles them when they have been played, and learns from the difference between what was predicted and what happened.
Tickets are built from what it has learned. Day-to-day operating rules are in `CLAUDE.md`.

## What runs every night (no person or AI session needed)

`.github/workflows/papertrade.yml` runs at 21:40 and 11:00 UTC on GitHub's runners:

| Step | Script | What it does | Output |
|---|---|---|---|
| Harvest | `tape_harvest.py`, `tape_store.py` | Every team sport, every fixture, every market, first-seen price and house probability | `papertrade/tape/` |
| Research | `allform.py` | Sportradar last-10 for both teams of every fixture; a trend rate for every market it can evaluate, stored before kick-off | `papertrade/form/` |
| Settle | `tape_grade.py` | Settles every outcome from the final score (90-minute rules, voids, overtime, corners, cards) | `engine/cache/tape_graded/` |
| Report | `tape_report.py` | Calibration and flat-stake return of every market slice | `papertrade/TAPE.md` |
| Learn | `learn.py` | Where the house price misses, whether form research beat the price, how our web research did | `papertrade/learned.json`, `LEARNED.md`, `learning_log.jsonl` |
| Tickets | `settle_tickets.py` | Settles every posted ticket once and keeps it for ever | `papertrade/ticket_ledger.jsonl`, `TICKETS.md`, `CLASSES.md` |
| Model grading | `daily.py`, `grade.py`, `journal.py` | Prices corners, cards, basketball and baseball with our own models and grades them against the house | `papertrade/JOURNAL.md` |
| Health | `health.py` | Records every step; any failure turns the run red after results are pushed | `papertrade/health.json` |

`ci.yml` compiles every script and runs the unit tests (`engine/tests/`) on each push.

## What a session adds

Web research (team news, absences, date and venue conflicts) needs an AI session. Its output goes to
`papertrade/research/` and is graded by `learn.py` the next night like everything else. Tickets are built with
`engine/build_tickets.py`, which applies the binding gates, re-prices live, uses the learned corrections, posts,
verifies every leg and logs the code.

## Layout

- `engine/` code. `engine/archive/` holds dated one-off scripts kept for reference only.
- `papertrade/` all data and reports the engine produces.
- `docs/ARCHITECTURE.md` design, data flow, the November 2026 review and known limits. `docs/HISTORY.md` the full rule history.

## Run it locally

```
cd engine
python3 -m unittest discover -s tests          # checks
python3 tape_harvest.py 30 && python3 tape_grade.py && python3 tape_report.py && python3 learn.py
```
