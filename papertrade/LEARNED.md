# What the engine has learned (auto, 2026-11-22 01:48 UTC)

Rebuilt every night by `engine/learn.py` from **4,037,281 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-22). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (13 of 1149 slices; chance alone would give about 3.1)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,395 | -0.6pp | -4.2 | -0.5pp / -0.8pp | -23.0% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,134 | +1.7pp | +4.2 | +1.4pp / +2.0pp | -9.2% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 883 | -4.2pp | -3.9 | -2.8pp / -5.8pp | -44.2% | -1.5pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,470 | +2.6pp | +3.4 | +2.5pp / +2.6pp | -4.0% | +1.8pp |
| football | Goal Range | other | 1.60-2.19 | 3,130 | +3.0pp | +3.4 | +3.2pp / +2.9pp | -3.6% | +2.1pp |
| football | Goal Range | other | 2.20-3.99 | 3,445 | -1.9pp | -3.4 | -2.0pp / -1.7pp | -17.5% | -1.3pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,197 | +1.6pp | +3.4 | +1.3pp / +2.0pp | -1.6% | +1.2pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 872 | -3.6pp | -3.2 | -3.9pp / -3.2pp | -30.7% | -1.3pp |
| football | 2nd Half - Away Team Clean Sheet | Yes | 1.60-2.19 | 3,427 | +2.6pp | +3.0 | +2.3pp / +2.9pp | -4.4% | +1.8pp |
| football | GG/NG | Yes | 2.20-3.99 | 613 | +6.1pp | +3.0 | +4.3pp / +8.1pp | +3.4% | +1.8pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 1,920 | +3.3pp | +3.0 | +3.3pp / +3.4pp | -0.2% | +1.9pp |
| football | Winning Margin | other | 2.20-3.99 | 2,984 | +2.1pp | +3.0 | +2.2pp / +1.9pp | -5.2% | +1.4pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,478 | +3.5pp | +3.0 | +3.6pp / +3.3pp | -0.7% | +1.7pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 26,391 | 733 | +0.085 | 0.051 | +1.7 | 0.000 |
| basketball | 16,569 | 254 | +0.134 | 0.112 | +1.2 | 0.000 |
| ice hockey | 2,234 | 93 | +0.722 | 0.295 | +2.5 | 0.000 |
| volleyball | 115 | 62 | -0.336 | 0.368 | -0.9 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 6,253 | 1,042 | +2.5pp | +1.8 | -3.5% |
| all sports | form 15pp+ below price | 5,916 | 997 | -3.2pp | -2.1 | -12.1% |
| all sports | form 5-15pp above | 10,291 | 1,137 | +1.4pp | +1.5 | -5.3% |
| all sports | form 5-15pp below | 10,252 | 1,143 | -1.0pp | -1.1 | -9.5% |
| all sports | form within 5pp | 14,175 | 1,099 | +0.2pp | +1.6 | -8.0% |
| american football | form 15pp+ above price | 115 | 33 | +7.6pp | +0.8 | +7.3% |
| american football | form 15pp+ below price | 116 | 34 | -8.3pp | -0.9 | -21.2% |
| american football | form 5-15pp above | 228 | 44 | -3.9pp | -0.6 | -14.1% |
| american football | form 5-15pp below | 229 | 44 | +4.1pp | +0.7 | +0.8% |
| american football | form within 5pp | 327 | 42 | -0.2pp | -1.0 | -8.3% |
| basketball | form 15pp+ above price | 2,269 | 227 | +3.0pp | +1.0 | -0.7% |
| basketball | form 15pp+ below price | 2,310 | 228 | -2.9pp | -1.0 | -12.3% |
| basketball | form 5-15pp above | 3,581 | 247 | +1.8pp | +0.9 | -3.4% |
| basketball | form 5-15pp below | 3,580 | 247 | -1.7pp | -0.8 | -9.8% |
| basketball | form within 5pp | 4,829 | 235 | -0.0pp | -0.3 | -7.6% |
| football | form 15pp+ above price | 3,547 | 693 | +1.8pp | +1.3 | -6.2% |
| football | form 15pp+ below price | 3,188 | 640 | -3.0pp | -1.8 | -11.5% |
| football | form 5-15pp above | 5,790 | 716 | +0.9pp | +0.9 | -6.8% |
| football | form 5-15pp below | 5,756 | 717 | -0.3pp | -0.4 | -8.6% |
| football | form within 5pp | 8,110 | 707 | +0.3pp | +1.9 | -8.1% |
| ice hockey | form 15pp+ above price | 155 | 64 | +12.5pp | +1.9 | +17.1% |
| ice hockey | form 15pp+ below price | 162 | 66 | -13.6pp | -2.1 | -31.3% |
| ice hockey | form 5-15pp above | 572 | 93 | +8.2pp | +2.6 | +7.8% |
| ice hockey | form 5-15pp below | 568 | 93 | -7.9pp | -2.4 | -24.7% |
| ice hockey | form within 5pp | 777 | 86 | +0.3pp | +0.9 | -8.3% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 2,630 | 171 | -0.4pp | -0.6 | -7.4% |
| researched, not vetoed: same markets | 46,754 | 2,146 | -0.2pp | -0.7 | -6.2% |
| research picks | 1,054 | 819 | -1.1pp | -0.7 | -5.9% |
