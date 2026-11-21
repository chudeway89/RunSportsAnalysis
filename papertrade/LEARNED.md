# What the engine has learned (auto, 2026-11-21 21:43 UTC)

Rebuilt every night by `engine/learn.py` from **4,014,628 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-21). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (16 of 1146 slices; chance alone would give about 3.1)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,368 | -0.6pp | -4.3 | -0.4pp / -0.9pp | -23.0% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,109 | +1.7pp | +4.2 | +1.1pp / +2.3pp | -9.1% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 877 | -4.3pp | -4.0 | -2.5pp / -6.0pp | -44.9% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,452 | +2.6pp | +3.5 | +2.5pp / +2.8pp | -3.7% | +1.8pp |
| football | Goal Range | other | 1.60-2.19 | 3,112 | +3.1pp | +3.4 | +3.0pp / +3.1pp | -3.5% | +2.1pp |
| football | Goal Range | other | 2.20-3.99 | 3,425 | -1.9pp | -3.4 | -2.0pp / -1.8pp | -17.6% | -1.3pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,170 | +1.6pp | +3.3 | +1.5pp / +1.6pp | -1.7% | +1.2pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 870 | -3.6pp | -3.2 | -3.6pp / -3.5pp | -30.6% | -1.3pp |
| football | Winning Margin | other | 2.20-3.99 | 2,970 | +2.2pp | +3.1 | +2.0pp / +2.3pp | -4.9% | +1.4pp |
| football | Home Team Total Corners | Over | <1.30 | 966 | -4.3pp | -3.1 | -2.8pp / -6.1pp | -9.2% | -1.7pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 1,903 | +3.4pp | +3.1 | +3.3pp / +3.5pp | -0.0% | +1.9pp |
| football | GG/NG | Yes | 2.20-3.99 | 610 | +6.1pp | +3.1 | +4.7pp / +7.5pp | +3.5% | +1.8pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,471 | +3.5pp | +3.0 | +4.5pp / +2.7pp | -0.5% | +1.7pp |
| football | Exact Goals | other | 4.00+ | 3,481 | -0.4pp | -3.0 | -0.3pp / -0.5pp | -22.7% | -0.3pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 844 | -4.9pp | -3.0 | -5.7pp / -4.2pp | -11.5% | -1.8pp |
| football | Exact Goals | other | 2.20-3.99 | 3,126 | +1.5pp | +3.0 | +1.3pp / +1.8pp | -11.1% | +1.0pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 24,499 | 685 | +0.041 | 0.052 | +0.8 | 0.000 |
| basketball | 14,894 | 228 | +0.061 | 0.116 | +0.5 | 0.000 |
| ice hockey | 2,013 | 85 | +0.765 | 0.312 | +2.5 | 0.000 |
| volleyball | 108 | 58 | -0.331 | 0.372 | -0.9 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 5,564 | 949 | +1.1pp | +0.8 | -6.5% |
| all sports | form 15pp+ below price | 5,267 | 904 | -1.7pp | -1.1 | -9.4% |
| all sports | form 5-15pp above | 9,339 | 1,034 | +0.7pp | +0.7 | -6.6% |
| all sports | form 5-15pp below | 9,313 | 1,037 | -0.3pp | -0.3 | -8.0% |
| all sports | form within 5pp | 12,986 | 992 | +0.2pp | +1.4 | -7.7% |
| basketball | form 15pp+ above price | 1,979 | 203 | +1.2pp | +0.4 | -4.6% |
| basketball | form 15pp+ below price | 2,014 | 204 | -1.1pp | -0.4 | -8.9% |
| basketball | form 5-15pp above | 3,236 | 223 | +0.6pp | +0.3 | -5.7% |
| basketball | form 5-15pp below | 3,232 | 223 | -0.6pp | -0.3 | -7.5% |
| basketball | form within 5pp | 4,433 | 211 | -0.1pp | -0.4 | -7.2% |
| football | form 15pp+ above price | 3,243 | 647 | +0.7pp | +0.5 | -8.8% |
| football | form 15pp+ below price | 2,923 | 595 | -1.7pp | -1.0 | -9.2% |
| football | form 5-15pp above | 5,369 | 669 | +0.2pp | +0.2 | -8.1% |
| football | form 5-15pp below | 5,350 | 669 | +0.4pp | +0.4 | -7.2% |
| football | form within 5pp | 7,614 | 661 | +0.3pp | +1.8 | -7.9% |
| ice hockey | form 15pp+ above price | 146 | 58 | +12.6pp | +1.8 | +17.6% |
| ice hockey | form 15pp+ below price | 154 | 60 | -13.8pp | -2.0 | -31.1% |
| ice hockey | form 5-15pp above | 517 | 85 | +9.3pp | +2.7 | +10.2% |
| ice hockey | form 5-15pp below | 516 | 85 | -9.1pp | -2.6 | -26.4% |
| ice hockey | form within 5pp | 680 | 78 | +0.3pp | +0.7 | -8.0% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 2,377 | 157 | -0.6pp | -0.9 | -7.7% |
| researched, not vetoed: same markets | 45,154 | 2,062 | -0.1pp | -0.6 | -6.2% |
| research picks | 1,008 | 782 | -0.8pp | -0.5 | -5.5% |
