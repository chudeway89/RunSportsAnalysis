# What the engine has learned (auto, 2026-11-23 02:11 UTC)

Rebuilt every night by `engine/learn.py` from **4,233,543 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-23). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (14 of 1182 slices; chance alone would give about 3.2)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,604 | -0.6pp | -4.5 | -0.5pp / -0.8pp | -23.4% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,334 | +1.7pp | +4.4 | +1.4pp / +2.1pp | -9.0% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 924 | -4.1pp | -3.9 | -2.8pp / -5.6pp | -44.4% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,686 | +2.7pp | +3.7 | +2.5pp / +2.9pp | -3.5% | +1.9pp |
| football | Winning Margin | other | 2.20-3.99 | 3,096 | +2.4pp | +3.6 | +2.2pp / +2.7pp | -4.0% | +1.6pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,400 | +1.6pp | +3.4 | +1.3pp / +2.0pp | -1.6% | +1.2pp |
| football | Goal Range | other | 2.20-3.99 | 3,586 | -1.8pp | -3.4 | -2.0pp / -1.6pp | -17.3% | -1.3pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 929 | -3.6pp | -3.2 | -3.9pp / -3.1pp | -30.8% | -1.4pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,587 | +3.6pp | +3.2 | +3.6pp / +3.5pp | -0.4% | +1.8pp |
| football | Goal Range | other | 1.60-2.19 | 3,261 | +2.8pp | +3.2 | +3.2pp / +2.3pp | -4.1% | +1.9pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,003 | +3.4pp | +3.1 | +3.3pp / +3.5pp | -0.1% | +1.9pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 895 | -4.9pp | -3.1 | -4.7pp / -5.2pp | -11.5% | -1.8pp |
| football | 2nd Half - Away Team Clean Sheet | Yes | 1.60-2.19 | 3,571 | +2.6pp | +3.1 | +2.3pp / +2.8pp | -4.5% | +1.8pp |
| football | 1X2 & Over/Under 4.5 | other | 4.00+ | 5,592 | -0.4pp | -3.0 | -0.2pp / -0.7pp | -28.6% | -0.3pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 44,724 | 1,303 | +0.042 | 0.037 | +1.1 | 0.000 |
| basketball | 31,786 | 469 | +0.184 | 0.082 | +2.2 | 0.000 |
| ice hockey | 5,129 | 222 | +0.318 | 0.192 | +1.7 | 0.000 |
| american football | 1,764 | 74 | +0.094 | 0.297 | +0.3 | 0.000 |
| volleyball | 215 | 118 | -0.169 | 0.291 | -0.6 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 11,024 | 1,879 | +2.5pp | +2.5 | -4.0% |
| all sports | form 15pp+ below price | 10,321 | 1,813 | -3.1pp | -2.8 | -12.3% |
| all sports | form 5-15pp above | 18,419 | 2,084 | +1.0pp | +1.4 | -6.2% |
| all sports | form 5-15pp below | 18,348 | 2,096 | -0.8pp | -1.1 | -9.2% |
| all sports | form within 5pp | 26,115 | 2,003 | +0.0pp | +0.2 | -7.6% |
| american football | form 15pp+ above price | 221 | 57 | +4.5pp | +0.7 | +0.5% |
| american football | form 15pp+ below price | 222 | 58 | -4.9pp | -0.7 | -16.0% |
| american football | form 5-15pp above | 387 | 72 | -2.6pp | -0.5 | -11.9% |
| american football | form 5-15pp below | 389 | 72 | +2.7pp | +0.5 | -1.8% |
| american football | form within 5pp | 545 | 69 | -0.1pp | -1.0 | -7.6% |
| basketball | form 15pp+ above price | 3,974 | 416 | +4.9pp | +2.3 | +1.6% |
| basketball | form 15pp+ below price | 4,058 | 418 | -4.7pp | -2.2 | -16.4% |
| basketball | form 5-15pp above | 6,911 | 459 | +2.0pp | +1.4 | -3.6% |
| basketball | form 5-15pp below | 6,912 | 458 | -2.0pp | -1.3 | -10.9% |
| basketball | form within 5pp | 9,931 | 436 | -0.0pp | -0.4 | -6.7% |
| football | form 15pp+ above price | 6,254 | 1,221 | +0.9pp | +0.9 | -8.0% |
| football | form 15pp+ below price | 5,472 | 1,140 | -1.8pp | -1.5 | -9.4% |
| football | form 5-15pp above | 9,712 | 1,268 | +0.2pp | +0.2 | -8.3% |
| football | form 5-15pp below | 9,652 | 1,271 | +0.2pp | +0.2 | -7.8% |
| football | form within 5pp | 13,634 | 1,247 | +0.0pp | +0.3 | -8.2% |
| ice hockey | form 15pp+ above price | 396 | 148 | +5.7pp | +1.3 | +4.8% |
| ice hockey | form 15pp+ below price | 411 | 150 | -6.2pp | -1.4 | -17.2% |
| ice hockey | form 5-15pp above | 1,258 | 217 | +3.4pp | +1.5 | -0.7% |
| ice hockey | form 5-15pp below | 1,240 | 217 | -3.5pp | -1.5 | -14.7% |
| ice hockey | form within 5pp | 1,824 | 196 | +0.2pp | +1.0 | -8.2% |
| volleyball | form 15pp+ below price | 31 | 31 | +4.2pp | +0.6 | +2.5% |
| volleyball | form 5-15pp above | 45 | 45 | +2.5pp | +0.3 | -2.7% |
| volleyball | form 5-15pp below | 53 | 53 | -0.5pp | -0.1 | -6.6% |
| volleyball | form within 5pp | 65 | 33 | +0.3pp | +1.0 | -12.6% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 4,111 | 272 | +0.1pp | +0.1 | -6.9% |
| researched, not vetoed: same markets | 61,507 | 2,982 | -0.2pp | -1.1 | -6.4% |
| research picks | 1,357 | 1,083 | -0.6pp | -0.5 | -5.3% |
