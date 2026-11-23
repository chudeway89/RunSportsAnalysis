# What the engine has learned (auto, 2026-11-23 22:40 UTC)

Rebuilt every night by `engine/learn.py` from **4,271,645 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-23). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (17 of 1190 slices; chance alone would give about 3.2)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,654 | -0.6pp | -4.6 | -0.5pp / -0.9pp | -23.5% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,382 | +1.7pp | +4.4 | +1.4pp / +2.1pp | -9.0% | +1.4pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 931 | -4.2pp | -4.1 | -2.8pp / -5.7pp | -44.8% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,715 | +2.7pp | +3.8 | +2.5pp / +3.0pp | -3.4% | +1.9pp |
| football | Winning Margin | other | 2.20-3.99 | 3,120 | +2.5pp | +3.7 | +2.2pp / +2.9pp | -3.7% | +1.7pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,450 | +1.6pp | +3.5 | +1.3pp / +2.1pp | -1.6% | +1.3pp |
| football | Goal Range | other | 2.20-3.99 | 3,624 | -1.8pp | -3.3 | -2.0pp / -1.5pp | -17.2% | -1.3pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,602 | +3.6pp | +3.3 | +3.6pp / +3.6pp | -0.2% | +1.9pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,015 | +3.5pp | +3.3 | +3.3pp / +3.8pp | +0.3% | +2.0pp |
| football | Goal Range | other | 1.60-2.19 | 3,294 | +2.7pp | +3.2 | +3.2pp / +2.2pp | -4.2% | +1.9pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 937 | -3.5pp | -3.1 | -3.9pp / -2.9pp | -30.2% | -1.3pp |
| football | GG/NG | Yes | 2.20-3.99 | 644 | +6.1pp | +3.1 | +4.3pp / +8.0pp | +3.3% | +1.8pp |
| football | GG/NG | No | 2.20-3.99 | 2,666 | +2.9pp | +3.1 | +1.9pp / +4.0pp | -3.6% | +1.9pp |
| football | 1X2 & Over/Under 4.5 | other | 4.00+ | 5,642 | -0.4pp | -3.0 | -0.2pp / -0.7pp | -28.7% | -0.4pp |
| football | 2nd Half - Away Team Clean Sheet | Yes | 1.60-2.19 | 3,602 | +2.5pp | +3.0 | +2.3pp / +2.7pp | -4.6% | +1.8pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 901 | -4.8pp | -3.0 | -4.7pp / -4.9pp | -11.4% | -1.8pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,706 | -3.5pp | -3.0 | -2.8pp / -4.4pp | -9.7% | -1.9pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 48,066 | 1,388 | +0.046 | 0.036 | +1.3 | 0.000 |
| basketball | 34,342 | 505 | +0.156 | 0.080 | +1.9 | 0.000 |
| ice hockey | 5,523 | 240 | +0.277 | 0.186 | +1.5 | 0.000 |
| american football | 1,790 | 75 | +0.102 | 0.294 | +0.3 | 0.000 |
| volleyball | 232 | 127 | -0.256 | 0.281 | -0.9 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 11,741 | 2,006 | +2.3pp | +2.3 | -4.5% |
| all sports | form 15pp+ below price | 11,020 | 1,937 | -2.8pp | -2.6 | -11.9% |
| all sports | form 5-15pp above | 19,871 | 2,228 | +0.8pp | +1.2 | -6.6% |
| all sports | form 5-15pp below | 19,755 | 2,241 | -0.6pp | -0.9 | -8.9% |
| all sports | form within 5pp | 28,199 | 2,146 | +0.0pp | +0.0 | -7.7% |
| american football | form 15pp+ above price | 224 | 58 | +4.3pp | +0.6 | +0.0% |
| american football | form 15pp+ below price | 225 | 59 | -4.6pp | -0.7 | -15.6% |
| american football | form 5-15pp above | 393 | 73 | -2.0pp | -0.4 | -10.8% |
| american football | form 5-15pp below | 395 | 73 | +2.2pp | +0.4 | -2.8% |
| american football | form within 5pp | 553 | 70 | -0.1pp | -1.0 | -7.7% |
| basketball | form 15pp+ above price | 4,227 | 447 | +4.2pp | +2.0 | +0.1% |
| basketball | form 15pp+ below price | 4,317 | 449 | -4.0pp | -1.9 | -15.0% |
| basketball | form 5-15pp above | 7,503 | 495 | +1.3pp | +0.9 | -5.1% |
| basketball | form 5-15pp below | 7,494 | 494 | -1.2pp | -0.9 | -9.6% |
| basketball | form within 5pp | 10,801 | 471 | -0.0pp | -0.5 | -7.0% |
| football | form 15pp+ above price | 6,694 | 1,299 | +1.0pp | +1.0 | -7.8% |
| football | form 15pp+ below price | 5,885 | 1,214 | -1.9pp | -1.6 | -9.8% |
| football | form 5-15pp above | 10,461 | 1,353 | +0.5pp | +0.6 | -7.8% |
| football | form 5-15pp below | 10,363 | 1,356 | -0.0pp | -0.1 | -8.2% |
| football | form within 5pp | 14,663 | 1,330 | +0.0pp | +0.1 | -8.3% |
| ice hockey | form 15pp+ above price | 412 | 160 | +5.0pp | +1.2 | +3.6% |
| ice hockey | form 15pp+ below price | 429 | 162 | -5.4pp | -1.3 | -15.6% |
| ice hockey | form 5-15pp above | 1,355 | 232 | +2.8pp | +1.3 | -2.1% |
| ice hockey | form 5-15pp below | 1,339 | 232 | -2.7pp | -1.2 | -13.2% |
| ice hockey | form within 5pp | 1,988 | 213 | +0.2pp | +0.9 | -7.6% |
| volleyball | form 15pp+ below price | 34 | 34 | +5.8pp | +0.8 | +4.4% |
| volleyball | form 5-15pp above | 47 | 47 | +0.7pp | +0.1 | -6.8% |
| volleyball | form 5-15pp below | 55 | 55 | +0.9pp | +0.1 | -4.1% |
| volleyball | form within 5pp | 73 | 37 | +0.3pp | +1.0 | -11.5% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 4,236 | 281 | +0.1pp | +0.2 | -6.8% |
| researched, not vetoed: same markets | 63,627 | 3,084 | -0.1pp | -0.8 | -6.4% |
| research picks | 1,411 | 1,122 | -0.7pp | -0.5 | -5.3% |
