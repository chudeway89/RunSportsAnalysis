# What the engine has learned (auto, 2026-11-25 04:47 UTC)

Rebuilt every night by `engine/learn.py` from **4,354,192 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-25). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (16 of 1213 slices; chance alone would give about 3.3)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,759 | -0.6pp | -4.5 | -0.6pp / -0.7pp | -23.4% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,482 | +1.7pp | +4.4 | +1.6pp / +1.8pp | -9.1% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 955 | -4.2pp | -4.1 | -3.2pp / -5.2pp | -44.7% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,770 | +2.8pp | +3.8 | +2.7pp / +2.8pp | -3.3% | +2.0pp |
| football | Winning Margin | other | 2.20-3.99 | 3,178 | +2.5pp | +3.6 | +2.7pp / +2.2pp | -3.8% | +1.7pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,549 | +1.7pp | +3.6 | +1.2pp / +2.2pp | -1.5% | +1.3pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,059 | +3.7pp | +3.5 | +3.0pp / +4.6pp | +0.7% | +2.1pp |
| football | Goal Range | other | 2.20-3.99 | 3,701 | -1.8pp | -3.3 | -1.9pp / -1.7pp | -17.1% | -1.3pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 951 | -3.6pp | -3.3 | -4.3pp / -2.7pp | -30.8% | -1.4pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,616 | +3.6pp | +3.2 | +3.9pp / +3.3pp | -0.4% | +1.9pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,743 | -3.7pp | -3.2 | -2.8pp / -4.9pp | -10.1% | -2.0pp |
| football | Goal Range | other | 1.60-2.19 | 3,369 | +2.7pp | +3.2 | +2.9pp / +2.5pp | -4.2% | +1.9pp |
| football | GG/NG | Yes | 2.20-3.99 | 652 | +6.2pp | +3.2 | +3.9pp / +8.7pp | +3.5% | +1.9pp |
| football | 1st Half - Over/Under | Over | 4.00+ | 5,258 | -1.4pp | -3.1 | -0.8pp / -2.2pp | -33.7% | -1.1pp |
| football | GG/NG | No | 2.20-3.99 | 2,721 | +2.9pp | +3.1 | +1.7pp / +4.2pp | -3.6% | +1.9pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 926 | -4.8pp | -3.1 | -4.2pp / -5.4pp | -11.3% | -1.8pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 54,636 | 1,548 | +0.034 | 0.034 | +1.0 | 0.000 |
| basketball | 43,398 | 633 | +0.083 | 0.071 | +1.2 | 0.000 |
| ice hockey | 7,497 | 314 | +0.214 | 0.158 | +1.4 | 0.000 |
| american football | 1,878 | 78 | +0.186 | 0.289 | +0.6 | 0.000 |
| volleyball | 270 | 147 | -0.322 | 0.261 | -1.2 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 14,337 | 2,332 | +1.4pp | +1.6 | -6.2% |
| all sports | form 15pp+ below price | 13,532 | 2,262 | -1.9pp | -1.9 | -10.3% |
| all sports | form 5-15pp above | 23,751 | 2,595 | +0.6pp | +1.0 | -6.8% |
| all sports | form 5-15pp below | 23,552 | 2,609 | -0.4pp | -0.7 | -8.5% |
| all sports | form within 5pp | 33,169 | 2,498 | -0.0pp | -0.0 | -7.7% |
| american football | form 15pp+ above price | 237 | 61 | +6.2pp | +0.9 | +3.7% |
| american football | form 15pp+ below price | 238 | 62 | -6.5pp | -1.0 | -18.9% |
| american football | form 5-15pp above | 415 | 76 | -1.0pp | -0.2 | -8.8% |
| american football | form 5-15pp below | 417 | 76 | +1.1pp | +0.2 | -4.7% |
| american football | form within 5pp | 571 | 73 | -0.1pp | -1.0 | -7.4% |
| basketball | form 15pp+ above price | 5,651 | 562 | +1.8pp | +1.0 | -4.7% |
| basketball | form 15pp+ below price | 5,768 | 564 | -1.7pp | -0.9 | -10.8% |
| basketball | form 5-15pp above | 9,462 | 620 | +1.1pp | +0.8 | -5.5% |
| basketball | form 5-15pp below | 9,447 | 619 | -1.1pp | -0.8 | -9.4% |
| basketball | form within 5pp | 13,070 | 582 | -0.0pp | -0.4 | -6.6% |
| football | form 15pp+ above price | 7,714 | 1,451 | +1.0pp | +1.1 | -7.8% |
| football | form 15pp+ below price | 6,779 | 1,360 | -1.8pp | -1.7 | -9.7% |
| football | form 5-15pp above | 11,864 | 1,509 | +0.2pp | +0.2 | -8.3% |
| football | form 5-15pp below | 11,714 | 1,513 | +0.2pp | +0.3 | -7.5% |
| football | form within 5pp | 16,565 | 1,481 | +0.0pp | +0.0 | -8.4% |
| ice hockey | form 15pp+ above price | 545 | 210 | +3.9pp | +1.1 | +0.3% |
| ice hockey | form 15pp+ below price | 573 | 213 | -4.2pp | -1.2 | -13.5% |
| ice hockey | form 5-15pp above | 1,840 | 304 | +2.3pp | +1.2 | -2.7% |
| ice hockey | form 5-15pp below | 1,799 | 304 | -2.2pp | -1.1 | -12.0% |
| ice hockey | form within 5pp | 2,740 | 285 | +0.1pp | +0.6 | -7.9% |
| volleyball | form 15pp+ below price | 39 | 39 | +8.1pp | +1.3 | +7.2% |
| volleyball | form 5-15pp above | 52 | 52 | +1.4pp | +0.2 | -5.3% |
| volleyball | form 5-15pp below | 60 | 60 | +0.2pp | +0.0 | -5.1% |
| volleyball | form within 5pp | 93 | 47 | +0.2pp | +1.0 | -9.9% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 4,908 | 312 | +0.3pp | +0.5 | -6.6% |
| researched, not vetoed: same markets | 70,264 | 3,388 | -0.1pp | -0.8 | -6.4% |
| research picks | 1,550 | 1,241 | -0.4pp | -0.4 | -4.9% |
