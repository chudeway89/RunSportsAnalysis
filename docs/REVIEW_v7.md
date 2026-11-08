# Panel review v7: the whole journey, Jun 9 → Nov 8, 2026

**Evidence used:**
- Every calibration block in `docs/HISTORY.md` (43 winning tickets, ~450 posted codes).
- `papertrade/legs.jsonl`: 1,783 unique legs, 1,681 decided, 1,151 with house p recorded at posting (Oct 26–Nov 7).
- `TICKETS.md`, re-settled locally Nov 8: 199 codes, 93 settled and not yet expired.
- `CLASSES.md`, `JOURNAL.md` (125k graded paper-trade outcomes), `TAPE.md` (1.09M full-board outcomes) and `FACTORS.md` (29.6k matches plus US sports).

**Panel:** actuary, statistician, quant/trader, financial modeller, analytic modeller, systems architect, design-thinking lead, professional punter, sports historian/analyst, behavioural economist. External perspectives were added where they matter: bookmaker risk-desk logic, the Kelly/bankroll literature, and the efficient-markets work on betting closing lines.

## 1. Headline numbers
| Measure | Value |
|---|---|
| Winning tickets, whole journey | 43, median ~5 legs, ~3x; 41 of 43 had ≤10 legs |
| Tickets with 13+ legs | ~250 posted, 1 won (SQWZVZ, with 3 voids) |
| Settled tickets Oct 26–Nov 7 | 93: 5 won, flat-stake ROI −76% |
| ROI by size (same 93) | 1–7 legs −50% (n=15); 8–12 legs +48% (n=10); 13+ legs −100% (n=68) |
| Legs, clean posting price | 811 won / 1,151, vs 738 expected (+6.3pp) |
| Same legs as singles, odds <2.2 | **+5% ROI** (n=976); <1.3: +4.7% ± 1.3; 1.3–1.6: +7.1% ± 3.1 |
| Same legs as singles, odds ≥2.2 | −25% (n=233) |
| User-picked legs <2.2 (singles) | +7.7% ± 2.1 (n=574) |
| Legs I picked <2.2 (singles) | +3.1% ± 2.5 (n=402) |
| Full-board tape | 0 of 408 market slices profitable; margin −5% (<1.3) to −26% (4.0+) |
| Paper-trade markets passing | 1 of 12 (team corners home, +4% on 1,396 picks, marginal) |

## 2. Findings by specialty
**Actuary.**
- The loss distribution is exactly what leg counts predict. Survival tracked the model within a leg or two on nearly every day, from Oct 11 to Nov 7.
- Ruin did not come from bad legs. It came from stake spread across 5–12 correlated tickets a day, 70% of them 13+ legs.
- At a 0.76 average leg, P(20-leg win) ≈ 0.4%. Sixty-eight such tickets producing zero wins is unremarkable.

**Statistician.**
- The +6pp leg edge holds across odds bands (+6–9pp in each), across sports, and in both weeks, which points to it being real.
- It is still only two weeks of data, and legs cluster by day (shared scoring environment), so effective n is smaller and the SE is understated by maybe ×1.5–2.
- The cleanest signal is short-priced legs under 1.3: +4.7% at 3.6 nominal SE.
- Earlier "leg beats house" figures (+8pp, Oct 26–28) were consistent with this.

**Quant.**
- If legs carry +5% EV, a k-leg acca has EV ≈ 1.05^k > 1 in expectation, but its variance explodes, and a small bankroll never collects the mean.
- Kelly sizing on a 20-leg 500x ticket with a real 1-in-700 chance recommends roughly zero stake. On a single at 1.3 with p 0.80 (+4%), it recommends about 2–3% of bankroll.
- **The format, not the selection, has been destroying the edge.** That is the single most important finding of the journey.

**Financial modeller.**
- Judge by money: return per unit, by format, on first-seen odds. Ticket counts and "wins" mislead.
- The 8–12-leg +48% comes from two wins (Q9T3U1 12.9x, H2EXYS); it is noise-level. The 1–7 leg −50% is also too few tickets to judge.
- Singles produce ~1,000 observations in two weeks, against ~25 for short tickets. That is the only format that can be validated in weeks rather than years.

**Analytic modeller.**
- The engine is sound and calibrated: the Poisson anchor, the 100k sims and the count models.
- It cannot beat the price. The independent model lost to closing odds (v5), and the factor study found everything priced except card context and shot form, both small.
- The edge we have is human or research selection (vetoes, absences, avoiding known traps), not modelling.
- Keep the engine for *pricing alt lines and joint probabilities*, not for finding value.

**Systems architect.**
- (1) **Critical bug:** CI settles tickets only from its own branch, whose tickets.txt froze at 56 lines on Oct 24. Every ticket since went unsettled by automation, and CLASSES/legs data on CI went stale. Fix: run settlement locally until the file is merged to that branch (needs user OK).
- (2) The always-loaded context was 498 KB (≈125k tokens) and grew every day, so each session paid for the whole history before working. It is now split: an operational core in CLAUDE.md (~25 KB) and the verbatim archive in docs/HISTORY.md.
- (3) Rules lived only as prose. Gates that matter are coded in pick.py, but several (+1.5 catch, weak-receiver basketball, away team-to-score) were enforced by hand and slipped repeatedly. Next step: code every §5 gate in one `gates.py` used by every builder (daypost, sim_acca, lad*.py, user-code edits).

**Design-thinking lead.**
- The user's job-to-be-done is "consequential odds that actually land". The system kept answering "big odds" with ladders that cannot land, then explaining why afterwards.
- A better product: a menu that shows the odds-vs-chance curve up front (singles ~1.3x at 80%; double ~2x at 60%; core ~4x at 25%; 500x at ~0.1%) and lets the user choose. Plus a daily singles sheet, which is the only tier with a measured edge.

**Professional punter.**
- Pros bet singles and the occasional double, at the best price, with flat or Kelly-fraction stakes, and track closing-line value.
- Accas are what bookmakers promote because their margin compounds per leg.
- The two strongest pockets in our data match professional instinct:
  - short-priced Overs and team Overs in leagues that score: team Over +28pp vs house;
  - avoiding Unders: −11pp, the house shades the Under in scoring leagues.

**Sports historian / analyst.** Calendar regime is real and repeated:
- Wins cluster in mid-season weeks: Jul 4–28, Aug 12–24, Oct 26–Nov 5.
- Losses cluster in transitions: the Aug pre-season, the Sep and Oct international breaks, and the basketball openers.
- Structural football facts the ledger rediscovered:
  - the modal favourite win is exactly 2 goals, which kills +1.5 catches;
  - cups settle on 90 minutes;
  - derbies and big-club games are fat-tailed;
  - pre-European-tie rotation is real;
  - South American away sides underperform.

**Behavioural economist.**
- Each painful loss produced a new rule: 82 L-rules plus R/v/V/D series. Many encoded variance as law, then were retracted (L8, the Under "window pattern", "trims work", "catches are protected").
- The ask for bigger odds after a loss is classic loss-chasing. The system should answer with the honest curve, not a bigger ladder.
- Rules now change only via the measured CLASSES.md trigger.

## 3. What worked (keep)
- Researched 4–6 leg cores and conversion edits of user codes: 14 of the user-code wins.
- Void-protected instruments: DNB, AH and integer refunds, To Qualify with a cushion.
- Overs and team Overs in scoring leagues; 1X2 home favourites at short prices (86% vs 81%).
- Research as a veto (dates, venues, absences, rotation).
- Concentration caps, when actually enforced.

## 4. What failed (stop)
- Ladders and megas as a daily product; fixed-count trims.
- Unders as "safe" legs.
- Thin-league Over 1.5 fill; +1.5/+2.5 catches against real favourites; weak-receiver basketball catches.
- Away team-to-score in cores; contrarian fades; narrative or pattern legs.
- Posting 8–12 slips a day on overlapping fixtures.

## 5. New rules written
See CLAUDE.md §5 (S1–S4, R1–R5, leg gates, user codes) and §6 (experiments E1–E4). New relative to v6:
- S2 singles sheet;
- the hard local-settlement step in the protocol;
- R4/R5 consolidated;
- basketball weak-receiver and away-TT-in-core bans made explicit;
- rules change only via CLASSES.md evidence.

## 6. Was the context reduced without losing information?
**Yes, with one honest qualification.**
- CLAUDE.md went from 498 KB to ~25 KB (≈95% fewer tokens loaded per turn).
- Every operational element was kept: protocol, API, settlement mechanics, market IDs, engine commands, every live gate, and all evidence numbers.
- The day-by-day narrative and superseded rules moved verbatim to docs/HISTORY.md. Nothing is deleted; it is one grep away.
- The qualification: past cases are no longer in front of the model automatically, so recalling a specific old fixture or rule wording costs one grep. Performance on the day protocol should improve (less context dilution), not degrade.
