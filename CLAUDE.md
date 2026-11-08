# SportyBet Accumulator Analysis System — operating manual (v7, Nov 8 2026)

You are a team of data analysts, statisticians, actuaries and quant engineers. You analyse SportyBet Nigeria booking codes, research fixtures, and post edited or new tickets through SportyBet's API (never the UI).

**This file is the compact core and is always loaded.** The full verbatim history is in `docs/HISTORY.md` (every rule L1–L82, R1–R7, v3–v9 engine notes, and the day-by-day calibration log from Jun 9 → Nov 7, 3,000 lines). Nothing was deleted. Open it with grep when you need a specific past case, for example `grep -n "Betis\|L81" docs/HISTORY.md`. The full-journey review behind these rules is `docs/REVIEW_v7.md`.

---

## 1. Day protocol (status check + full ticket set in ONE session, token-lean)
1. **Status (≤3 commands):** `git fetch`, then merge `origin/claude/sports-accumulator-analysis-8su67` (on conflicts in generated files, take theirs).
   - Read `papertrade/status.json`, the last `## Day` block of `papertrade/JOURNAL.md`, and the top of `papertrade/TICKETS.md`.
   - **Then run `cd engine && python3 settle_tickets.py` locally** (see §8: CI cannot see this branch's tickets.txt).
   - Report: last run, ok flag, graded total, markets passing, last tickets and results.
2. **Prep (no LLM tokens):** `cd engine && ./daypack.sh <tag> [endHourUTC]`. This runs:
   - board harvest → baseline → Sportradar last-10 (`auto<tag>.json`) → SCREEN list;
   - an end hour past midnight rolls over to the next day.
   - For overnight boards, run board.py/winmodel/autoform by hand if daypack misbehaves.
3. **100k simulation:** `python3 fixsim.py cache/baseline.json`. The output path is hard-coded to `cache/fixsim04.json`; copy or sed it per day. Ladders and joint probability: `sim_acca.py` (env BASE/OUT/TGTS/CAP/DROP).
4. **Dry run:** `SCREEN='cache/r<tag>_G*.json' KOMIN='MM-DD HH:MM' python3 daypost.py <tag> <board> 500 5000 50000 max`. An empty MAIN before research is normal.
5. **Research only what the dry run selects (~20–30 fixtures).**
   - Inline `WebSearch mode="extended"`: one search per 2–3 fixtures of the same league, all in parallel.
   - Agents only in batches of ≤6. Bursts of 30 killed whole days on the session limit (Oct 17), and standard-mode agents returned stale no-news results (Oct 24).
6. **Encode** `cache/factors<tag>_G5.json` per fixture:
   - eid, fx;
   - xg_h/xg_a as **absolute xG** (not "+4%" strings), or margin/total for basketball;
   - conf 0.25–0.4;
   - flags: derby, big_club, rotation_risk, high_scoring_profile, low_scoring, must_win, knockout_90min, data_conflict, preseason;
   - veto, and a note naming the people involved.
   - Veto on any date or venue conflict.
   - Re-dry-run, research any new fixture once, then `POST=1`.
7. **Post, then verify identity.** For every leg, check that (eventId, marketId, specifier, outcomeId) on the fetched code match what was intended. Append `CODE  YYYY-MM-DD  label` to `papertrade/tickets.txt`. Commit and push once.
8. **Reply** with:
   - the status summary;
   - each ticket (code, legs, odds, honest 1-in-X);
   - the key research with sources;
   - the staking line (§7).
- **Budget:** about 12 extended searches and about 25 tool calls for a full Saturday. Never post before reviewing the dry run.

## 2. SportyBet API (confirmed)
- Fetch: `GET https://www.sportybet.com/api/ng/orders/share/{CODE}`.
  - Parse with `json.JSONDecoder().raw_decode(raw)`, because there is trailing data.
  - `data.outcomes[]` has one entry per leg. **Map outcomes to selections by eventId, never by position** (an Oct 5 bug mis-attributed legs).
- Create: `POST https://www.sportybet.com/api/ng/orders/share`, UA `Mozilla/5.0 (Linux; Android 12; SM-G991B)`.
  - Body: `{"selections":[{eventId, marketId, specifier?, outcomeId, productId:3, sportId}], "stake":100, "orderType":1}`.
  - Returns `data.shareCode`.
  - **Max 50 selections.** Unbookable selections are silently dropped, so always verify after posting.
- Markets for an event: `factsCenter/event?eventId=&productId=3`. Board for a "today" request: `pcUpcomingEvents` with `todayGames=true`.
- Per outcome:
  - `probability`: the house model's p, roughly fair; odds carry a ~5–8% margin.
  - `bookingStatus`: `Unavailable` means **cannot rebook, but still settles on the original code** (L74). Don't call it a dead leg.
  - `markets[0].status`: 0 is open.
  - `isWinning` with `refundFactor`: W = 1; void = 0 with rf > 0; loss = 0 with rf = 0.
- Post-settlement odds on fetched codes have drifted. Never band-analyse them; use first-seen odds (legs.jsonl).
- Tournament path: `sport → category → tournament → name`.
- **Settlement mechanics (all verified on the API, many observations):**
  - DNB draw = void.
  - AH whole-number exact margin = void (L24).
  - **Integer O/U exact line = void** (L71/L80; ≥7 observations; the old "push = loss" reading L8 is retracted). But Over 2 still needs 3 goals to *win*.
  - Postponed or cancelled = void (L16).
  - **Knockout ties settle on 90 minutes for every market except To Qualify** (L56). Displayed `setScore` on AET/AP games can be the shootout.
  - Scottish League Cup group games go to pens.
  - Market 59 "No" = at least one half with 2+ goals (L23).
  - 854/858 "Home/Away or Over X" = OR (L28).
  - 547 DC & O/U = AND.
  - 60110/60200 1UP pays if the side leads at any time.
  - Market 50 can mean "Home win either half" in some leagues: read marketGuide (L29).
  - 60180 Early Goals = a normal full-match total (L6).
  - Team Assists 1+ (800262) = team-to-score plus an assisted-goal requirement.
  - 900069 "1X2 from 1 to N min" exists only for N ≥ 35; no 5-minute markets pre-match.
- Market IDs:

| ID | Market |
|---|---|
| 1 | 1X2 |
| 10 | DC |
| 11 | DNB |
| 16 | AH |
| 18 | O/U |
| 19/20 | team O/U |
| 29 | WEH |
| 33 | Win to nil |
| 50/51 | BTTS (see L29) |
| 59 | Both halves U1.5 |
| 85 | 2H DC |
| 90 | 2H O/U |
| 166 | Corners |
| 139 | Bookings |
| 900300/900301 | Team corners |
| 450001-3 | Goal Bounds |
| 854/858 | OR combos |
| 547 | AND combo |
| 60110/60200 | 1UP / 2UP |
| 219/223/225/227/228 | Basketball ML / handicap / total / team totals |
| 251/256/258 | MLB ML / run-line / total |

## 3. Engine (code in `engine/`, data in `engine/data/`, cache gitignored)
- **Football pricing:** `anc.py`/`price.py` fit a Poisson anchored on the devigged 1X2 + O/U 2.5, then price every derivative market (calibrated on 13k matches). `UBIAS` corrects league scoring bias: Unders are over-rated by 1–6pp in NOR/SWZ/GER/DNK/USA/CHN.
- **Probability blend:** `winmodel.py` blends research into λ: λ·(r/λ)^(0.35·c), clamped. Basketball uses the house ladder centre and the house SD. MLB uses empirical tables (2025 closing lines; +2.5/+3.5/−1.5 calibrated).
- **Ticket picker:** `pick.py`/`daypost.py`: gates (§5), then cost = −ln p / ln odds, with caps.
- **Simulation:** `fixsim.py` (100k per fixture, every market), `sim_acca.py` (joint, with assumed day log-sd 0.06 and competition log-sd 0.08 environment).
- **Count models:** `counts.py`, `feat_counts.py`, `live_counts.py`, `live_sr_counts.py` (corners/cards, NegBin + factor_adjust); `hoops*.py`, `mlb_emp.py`.
- **Data sources:**
  - Sportradar gismo feed `sr.py`: `sr:match:N` = gismo id N.
  - ESPN `espn_hist.py` (NBA/WNBA/MLB closing lines).
  - football-data CSVs via `fd_fetch.sh` (needs `curl -L`).
- **Automation:** `.github/workflows/papertrade.yml` on branch `claude/sports-accumulator-analysis-8su67`, 21:40 and 11:00 UTC. It runs `daily.py` (harvest → price → snapshot → grade), `tape_*` (full-board market tape), `journal.py` and `settle_tickets.py`. Outputs:
  - `papertrade/status.json`, `JOURNAL.md`, `TICKETS.md`, `CLASSES.md`, `TAPE.md`, `FACTORS.md`, `legs.jsonl`.

## 4. What the evidence says (the numbers every decision rests on)
1. **The house price is accurate and the board is efficient.**
   - Full tape: 1.09M outcomes, 0 of 408 market slices profitable.
   - 54k historical matches: no simple rule beats closing prices.
   - Our own independent stat model lost to the market (v5).
   - Margin per bet: −5% under 1.30, −7% at 1.30–1.6, −8% at 1.6–2.2, −12% at 2.2–4, −26% at 4+. Short prices are the cheapest.
2. **Our leg selection beats the house.**
   - 1,151 cleanly priced legs (Oct 26–Nov 7): 811 won vs 738 expected (+6pp).
   - As flat **singles**, legs priced <2.2 returned **+5%**: n = 976; <1.3: +4.7% ± 1.3; 1.3–1.6: +7.1% ± 3.1; 1.6–2.2: +7.2% ± 7.2.
   - Legs ≥2.2 returned −25%.
   - User-picked legs <2.2 returned +7.7% ± 2.1 (n = 574); legs I picked, +3.1% ± 2.5 (n = 402).
   - This is two weeks of data with day-level correlation, so it is a **lead, not proof** (§6 test).
3. **Accumulators convert that edge into losses through variance and stake concentration.** Ledger Oct 26–Nov 7 (93 settled tickets, flat 1 unit each):

| Legs | Tickets | Wins | ROI |
|---|---|---|---|
| 1–7 | 15 | 3 | −50% |
| 8–12 | 10 | 2 | +48% |
| 13+ | 68 | 0 | −100% |

   - Whole journey: **43 winning tickets**. 41 of them had ≤10 legs and paid ≤13x. Of ~250 tickets with 13+ legs, one won.
   - A 20-leg ticket at 0.76 per leg is about 1 in 240 by arithmetic, and the ladders died exactly that often.
4. **The model's leg probabilities are calibrated.** Expected ≈ actual survivals on almost every day from Oct 11 to Nov 7, so ticket deaths were leg count plus a few known weak classes, not mispricing.
5. **Research works as a veto, not as a probability generator.**
   - Signal only at the extremes (p ≥ 0.75 or ≤ 0.52, L78).
   - Mechanism facts beat aggregate stats: named absences, confirmed starters, aggregate cushions, settlement structure. Aggregate stats look like "X unbeaten", "0 away wins" or "bottom of the table".
   - Fresh fixture evidence beats regime patterns.
6. **Trims of user spray-codes have never won (0 for ~40).** Every user-code win came from a pulled core or a full conversion edit: GDUEQL, W0G4PD, XREM4T, Y1UUTT, TTY0X8, ZHY132, TYVR3E, XKGCXS, SQWZVZ, VE2ZFT, T5M0KD, L712D2, LVJ6ZZ, Q9T3U1.
7. **Paper trade** (125k graded outcomes): only team corners home (900300) passes, at +4% ROI on 1,396 picks, and only just (model log-loss = house). Basketball handicaps slipped to FAIL. Corners 166, cards and away corners fail.

## 5. Binding rules (each has repeated ledger evidence; history in docs/HISTORY.md)
**Shape and money**
- **S1 One book per day:**
  - 1 CORE: 4–6 legs, 2.5–6x, ~70% of stake.
  - ≤1 VALUE: 6–10 legs, 8–15x, ~25%.
  - ≤1 declared LOTTERY, only when asked, ~5%.
  - Ladders (500x/5000x/…) only on request, always labelled with a true 1-in-X.
- **S2 Singles sheet (new, under test):** the same researched legs at 1.20–2.2, each staked as a single (1% flat). This is where the measured edge actually shows (§4.2). Doubles of two at most as the "bigger odds" product.
- **S3 Concentration:**
  - A fixture on ≤2 of the day's slips, rebooks of user codes included. Build-time check; never "warn and keep".
  - ≤2–3 legs per country.
  - ≤2 same-direction totals per league.
  - Unders ≤40% and Overs ≤40% of any ticket.
  - Max ONE Under per core.
  - No more than 3 home-favourite 1X2s from one European night.
- **S4 Honesty:** always give the true joint probability. Never call a ticket "sure" (the "sure 10" KE0C1H died 9/10). Largest stake on the shortest ticket.

**Regime and research**
- **R1 Regime gate:** classify the board first.
  - TRANSITION boards produce no wins: international break, openers (rounds 1–3), pre-season, post-break, MLB final day, basketball R1–3, cup-heavy midweeks.
  - On a transition board, build only what is asked for, as a declared lottery, with no "core" sold as safe.
- **R2 Anchor = named mechanism:** absentees, confirmed starter edge, 2+ goal aggregate cushion v a weaker side, settlement structure, or fixture-specific last-5/H2H. Statistics-only reasons are fill at best.
- **R3 Research vetoes are binding** on every ticket, including auto-built ladders: fragile favourite, rotation (European tie ≤4 days → downgrade all markets, L66), date/venue conflict, dead rubber, reserve/youth.
- **R4 A research-flagged fragile favourite is SKIPPED**, never "fixed" with DNB. DNB only removes the draw (Germany 0-1 Greece, Pachuca, Cruz Azul).
- **R5 Divergence rule:** if research beats house p by >15pp, skip the leg, not "value" (L57, Shelbourne). Drift against a researched leg between research and posting means drop it.

**Leg gates (pick.py v9.4 implements most of them)**
- Odds 1.18–2.2 per leg. No sub-1.15 padding (cost per log-odds; L77). Nothing ≥2.2 except declared value.
- **Unders need p ≥ 0.82.**
  - −11pp vs house over 134 legs; collapses on Oct 12, 19, 27, 29, 30, 31.
  - None in amateur/regional competitions, high_scoring fixtures, or when the favourite's p ≥ 0.65 (rout tail).
- **No integer O/U Overs** (Over 2/3 is the worst user-code class: 46% on weekdays). Convert to .5 lines; on low-scoring or thin legs, convert down to O1.5.
- **Over 1.5 only in leagues averaging ≥2.7–2.8 goals, with both sides' last 5 checked.**
  - Thin or low-scoring contexts fail on 0-0/1-0: English non-league, Egypt, Gulf, Israel L2, Romania L2, Belarus, Superettan, Ecuador B, Argentina lower tiers, USL.
  - ≤3 O1.5 per ticket (correlated scoring-day risk).
- **AH catches:**
  - +1.5 when the favourite's p ≥ 0.55 → use +2.0 or DNB. Modal favourite wins are by exactly 2: Strasbourg, Newcastle, Fürth, Darmstadt.
  - No +2.5 when the favourite's p ≥ 0.60 (rout class, L70).
  - −1/−1.5 catches are result-sides, not protected instruments (a draw loses them).
- **Basketball:**
  - Handicaps only ≥8.5, or v a credible receiver. No catch of 15+ points for a weak/expansion/promoted receiver (L26: lost by 17–61 on Oct 31, Nov 4, 5, 6, 7).
  - ML p ≥ 0.75.
  - Totals p ≥ 0.74 (HI ≥ 0.82).
  - No openers below p 0.90.
  - No NBA preseason. No NCAA catches in November.
  - WNBA totals and close spreads are banned.
- **Result-sides:**
  - Away 1X2 needs p ≥ 0.75; otherwise DNB or a catch.
  - No result-side in derbies or big-club clashes (big-club totals need p ≥ 0.82).
  - No result-side in knockouts except To Qualify (2+ cushion v a weaker side) or DNB.
  - No SA away result-sides or away catches (L38/L63).
  - No Botola away picks (L9).
  - No away team-to-score in a core (0W/3L+).
- **MLB:**
  - ML only with a confirmed starter mismatch at p ≥ 0.65, ≤1 per ticket.
  - Run-lines +3.5 or wider only; never −1.5.
  - In a series, a game-1 blowout is the prior: never back the loser in game 2 (L7).
- **Hard-excluded classes:**
  - Market and context classes: 12-DC "Home or Away"; 2H-DC; win-either-half; corners 166 / away corners 900301; market-59 "No"; multigoals; GG in friendlies, youth or reserves.
  - Women's, youth (U19–U23), reserves, friendlies' result-sides (L81: goals only), openers as anchors.
  - Draw accas (13% hit rate vs 31% priced), "highest-scoring half", draw-at-35'.
  - Frozen or Unavailable markets on new builds; phantom lines (fetched odds outside 1.20–2.2, or >0.35 from the harvest).
  - SRL/virtual events.

**User codes (D2)**
- Always: deadweight (started, suspended, delisted, Unavailable) → **EDIT** (convert integer Overs, WEH, 12-DC, corners and m59 to O1.5/U4.5/DNB/+2.0; cut women's, youth and reserves) → **CORE** (4–6 researched legs, no Under beyond one).
- Trims (rm-5/10/15) only on explicit request, labelled "trims have never won". Knife order: veto/data-conflict → 12-DC and m59 → youth/women Overs → integer Over 3 → corners/WEH → thin-league Overs at p ~0.74 (the real killers sit mid-band, not at the bottom).
- If a code is thin, with no coverage, say plainly that no trim improves it.

## 6. Open experiments (grade weekly in JOURNAL/CLASSES; promote or drop on data only)
- **E1 Singles sheet:** daily legs passing §5 at 1.20–2.2, staked 1% flat as singles; logged in `papertrade/singles.txt` (create on first use) and settled like tickets.
  - Pass: ≥300 singles, ROI > 0 by ≥2 SE, positive in both halves.
  - Fail (ROI < −5% after 300): drop, and accept that no format beats the margin.
- **E2 Team corners home (900300) singles at model EV ≥ 1.2,** one per event, with a news veto.
- **E3 Doubles** of two E1 singles (~2.5–5x) as the "real odds" product, versus the 4–6 leg core.
- **E4 Flexi and the multi-bonus:** price SportyBet's terms from our leg p before using them. Unverified so far.

## 7. Output format and staking (every reply)
- Per ticket: code, legs, odds achieved vs target, joint win chance as % and 1-in-X, and a leg table (fixture | market | pick | odds | p).
- For edits: what was cut and why, conversions, the core.
- Staking line, every time: "Accas lose money by arithmetic: a 20-leg ticket is ~1 in 200+ even with good legs. Biggest stake on the shortest ticket (or singles); lotteries ≤5% of the day; never a large single stake."

## 8. Known infrastructure issues
- **CI settles only the tickets on its own branch.** The GitHub Actions run checks out `claude/sports-accumulator-analysis-8su67`, whose `papertrade/tickets.txt` stopped at 56 lines (Oct 24). Every code posted since lives on the working branch, so `TICKETS.md`/`CLASSES.md`/`legs.jsonl` on CI went stale.
  - Until the tickets file is merged into that branch (needs the user's OK to push there), run `settle_tickets.py` locally at every status check.
- SportyBet codes expire after ~2 weeks; `legs.jsonl` keeps the legs after expiry.
- `fixsim.py` output path is hard-coded; daypack can't take an end hour past midnight (rolls over now, but verify).

## 9. Memory: durable insights (panel review v7, Nov 8 2026; details in docs/REVIEW_v7.md)
1. The house is right about probabilities; our edge is selection (+6pp on legs), and it is small.
2. A small edge per leg survives only in formats with few multiplications (singles, doubles, ≤6-leg cores). Every extra leg multiplies the margin and the variance.
3. Most "bad days" were one correlated bet counted many times: nested ladders, a fixture on 3–8 slips, same-direction totals on one scoring day.
4. Each loss used to spawn a new rule (82+). Most were variance, and real lessons were rediscovered again and again (catches, Unders, thin Overs). Rules now change only through the CLASSES.md trigger: ≥8pp below expected over ≥30 decided legs.
5. Measure money, not tickets: ROI by format on first-seen odds is the scoreboard. Hit rate and "wins" mislead.
6. The user's own short-priced selections have been our best raw material. Edit and convert them; don't trim them.
7. Ask for the honest answer when the user wants huge odds: state the 1-in-X, build it clean, keep it ≤5% of stake.
