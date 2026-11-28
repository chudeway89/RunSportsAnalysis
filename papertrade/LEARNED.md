# What the engine has learned (auto, 2026-11-28 03:54 UTC)

Rebuilt every night by `engine/learn.py` from **4,570,559 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-28). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (21 of 1247 slices; chance alone would give about 3.4)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 6,037 | -0.6pp | -4.6 | -0.6pp / -0.7pp | -23.4% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,749 | +1.7pp | +4.6 | +1.7pp / +1.8pp | -9.0% | +1.4pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,813 | +2.0pp | +4.5 | +1.2pp / +2.9pp | -1.2% | +1.6pp |
| football | 1st Half - Over/Under | Over | 4.00+ | 5,510 | -1.7pp | -3.9 | -0.8pp / -2.9pp | -35.4% | -1.4pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 1,009 | -3.7pp | -3.7 | -3.5pp / -4.0pp | -42.9% | -1.5pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,916 | +2.6pp | +3.7 | +2.8pp / +2.4pp | -3.9% | +1.9pp |
| football | Winning Margin | other | 2.20-3.99 | 3,319 | +2.4pp | +3.6 | +2.5pp / +2.3pp | -4.0% | +1.6pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,161 | +3.7pp | +3.6 | +3.4pp / +4.0pp | +0.6% | +2.2pp |
| football | Handicap 0:5 | Away level | <1.30 | 165 | +4.6pp | +3.5 | +0.6pp / +8.0pp | +2.4% | +0.5pp |
| football | GG/NG | Yes | 2.20-3.99 | 684 | +6.4pp | +3.4 | +3.9pp / +9.2pp | +4.1% | +2.0pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,822 | -3.8pp | -3.4 | -3.4pp / -4.3pp | -10.2% | -2.1pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,666 | +3.6pp | +3.3 | +3.9pp / +3.3pp | -0.3% | +1.9pp |
| football | 1st Half - Multigoals | other | 4.00+ | 5,859 | -0.8pp | -3.2 | -0.5pp / -1.2pp | -41.0% | -0.7pp |
| football | Goal Range | other | 1.60-2.19 | 3,550 | +2.7pp | +3.2 | +2.8pp / +2.5pp | -4.3% | +1.9pp |
| football | Teams to Score | Both teams | 2.20-3.99 | 671 | +6.1pp | +3.2 | +4.5pp / +7.9pp | +3.7% | +1.9pp |
| football | Goal Range | other | 2.20-3.99 | 3,892 | -1.7pp | -3.2 | -1.7pp / -1.6pp | -16.8% | -1.2pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 965 | -4.8pp | -3.1 | -4.4pp / -5.2pp | -11.3% | -1.9pp |
| football | Away Team Total Corners | Over | <1.30 | 1,364 | -3.6pp | -3.1 | -2.4pp / -5.0pp | -8.2% | -1.7pp |
| football | GG/NG | No | 1.30-1.59 | 863 | -5.1pp | -3.1 | -1.8pp / -8.9pp | -15.1% | -1.9pp |
| football | GG/NG | No | 2.20-3.99 | 2,847 | +2.8pp | +3.0 | +1.9pp / +3.7pp | -3.8% | +1.8pp |
| football | 1st Half - Handicap | Home level | 4.00+ | 6,247 | -0.9pp | -3.0 | -0.2pp / -1.8pp | -29.0% | -0.8pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 71,740 | 1,984 | +0.019 | 0.030 | +0.6 | 0.000 |
| basketball | 59,375 | 877 | +0.033 | 0.061 | +0.5 | 0.000 |
| ice hockey | 14,149 | 597 | +0.092 | 0.112 | +0.8 | 0.000 |
| american football | 2,273 | 94 | +0.089 | 0.257 | +0.3 | 0.000 |
| volleyball | 409 | 223 | -0.323 | 0.193 | -1.7 | 0.000 |
| cricket | 131 | 66 | -0.287 | 0.455 | -0.6 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 19,973 | 3,217 | +0.7pp | +0.9 | -7.4% |
| all sports | form 15pp+ below price | 18,974 | 3,151 | -0.9pp | -1.1 | -8.4% |
| all sports | form 5-15pp above | 32,765 | 3,596 | +0.4pp | +0.7 | -7.1% |
| all sports | form 5-15pp below | 32,465 | 3,610 | -0.2pp | -0.3 | -7.7% |
| all sports | form within 5pp | 45,010 | 3,481 | +0.0pp | +0.2 | -7.5% |
| american football | form 15pp+ above price | 278 | 74 | +3.0pp | +0.5 | -2.3% |
| american football | form 15pp+ below price | 280 | 75 | -3.5pp | -0.6 | -13.4% |
| american football | form 5-15pp above | 502 | 92 | -1.1pp | -0.3 | -9.2% |
| american football | form 5-15pp below | 504 | 92 | +1.3pp | +0.3 | -4.5% |
| american football | form within 5pp | 709 | 89 | -0.1pp | -1.0 | -7.5% |
| basketball | form 15pp+ above price | 7,845 | 790 | +0.5pp | +0.3 | -6.9% |
| basketball | form 15pp+ below price | 8,022 | 792 | -0.5pp | -0.3 | -8.3% |
| basketball | form 5-15pp above | 13,068 | 857 | +0.7pp | +0.7 | -6.0% |
| basketball | form 5-15pp below | 13,040 | 856 | -0.8pp | -0.7 | -8.7% |
| basketball | form within 5pp | 17,400 | 812 | -0.0pp | -0.5 | -6.9% |
| cricket | form 5-15pp below | 30 | 30 | -5.3pp | -0.7 | -22.7% |
| football | form 15pp+ above price | 10,373 | 1,857 | +0.7pp | +0.9 | -8.3% |
| football | form 15pp+ below price | 9,207 | 1,759 | -1.2pp | -1.3 | -8.6% |
| football | form 5-15pp above | 15,515 | 1,939 | +0.2pp | +0.4 | -7.8% |
| football | form 5-15pp below | 15,303 | 1,942 | +0.2pp | +0.3 | -7.4% |
| football | form within 5pp | 21,342 | 1,906 | +0.1pp | +0.7 | -8.0% |
| ice hockey | form 15pp+ above price | 1,101 | 401 | +2.9pp | +1.1 | -1.2% |
| ice hockey | form 15pp+ below price | 1,148 | 407 | -3.1pp | -1.2 | -11.4% |
| ice hockey | form 5-15pp above | 3,388 | 569 | +0.2pp | +0.2 | -6.5% |
| ice hockey | form 5-15pp below | 3,333 | 571 | +0.2pp | +0.1 | -6.4% |
| ice hockey | form within 5pp | 5,179 | 542 | -0.0pp | -0.3 | -8.0% |
| volleyball | form 15pp+ above price | 46 | 46 | -7.8pp | -1.3 | -34.4% |
| volleyball | form 15pp+ below price | 67 | 67 | +8.0pp | +1.7 | +5.9% |
| volleyball | form 5-15pp above | 72 | 72 | +0.8pp | +0.1 | -9.6% |
| volleyball | form 5-15pp below | 79 | 79 | +0.6pp | +0.1 | -5.1% |
| volleyball | form within 5pp | 145 | 75 | +0.6pp | +2.3 | -6.8% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 5,499 | 344 | +0.1pp | +0.2 | -6.8% |
| researched, not vetoed: same markets | 78,044 | 3,759 | -0.1pp | -0.7 | -6.3% |
| research picks | 1,711 | 1,372 | -0.3pp | -0.3 | -4.7% |
