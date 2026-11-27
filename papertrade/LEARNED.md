# What the engine has learned (auto, 2026-11-27 04:01 UTC)

Rebuilt every night by `engine/learn.py` from **4,479,268 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-27). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (19 of 1233 slices; chance alone would give about 3.3)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,918 | -0.7pp | -4.8 | -0.6pp / -0.7pp | -23.6% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,633 | +1.8pp | +4.7 | +1.8pp / +1.9pp | -8.7% | +1.4pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,701 | +1.8pp | +4.1 | +1.1pp / +2.7pp | -1.3% | +1.4pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,843 | +2.7pp | +3.8 | +2.8pp / +2.6pp | -3.5% | +1.9pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 989 | -3.8pp | -3.7 | -3.3pp / -4.4pp | -43.1% | -1.5pp |
| football | 1st Half - Over/Under | Over | 4.00+ | 5,405 | -1.6pp | -3.6 | -0.8pp / -2.6pp | -34.7% | -1.3pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,130 | +3.7pp | +3.5 | +3.4pp / +4.0pp | +0.6% | +2.2pp |
| football | Handicap 0:5 | Away level | <1.30 | 164 | +4.6pp | +3.4 | +0.5pp / +8.0pp | +2.4% | +0.5pp |
| football | Winning Margin | other | 2.20-3.99 | 3,255 | +2.3pp | +3.4 | +2.5pp / +2.0pp | -4.4% | +1.6pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,798 | -3.8pp | -3.4 | -3.2pp / -4.5pp | -10.2% | -2.1pp |
| football | GG/NG | Yes | 2.20-3.99 | 669 | +6.4pp | +3.3 | +4.2pp / +8.8pp | +4.0% | +2.0pp |
| football | Goal Range | other | 1.60-2.19 | 3,478 | +2.7pp | +3.2 | +2.8pp / +2.7pp | -4.2% | +1.9pp |
| football | 1st Half - Multigoals | other | 4.00+ | 5,744 | -0.8pp | -3.2 | -0.5pp / -1.3pp | -41.0% | -0.7pp |
| football | Goal Range | other | 2.20-3.99 | 3,819 | -1.7pp | -3.2 | -1.7pp / -1.7pp | -16.9% | -1.2pp |
| football | Teams to Score | Both teams | 2.20-3.99 | 657 | +6.1pp | +3.2 | +4.8pp / +7.6pp | +3.8% | +1.9pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 951 | -4.8pp | -3.1 | -4.1pp / -5.6pp | -11.3% | -1.9pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 981 | -3.3pp | -3.0 | -4.1pp / -2.4pp | -29.0% | -1.3pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,650 | +3.3pp | +3.0 | +3.6pp / +3.1pp | -1.3% | +1.7pp |
| football | 1X2 & Over/Under 4.5 | other | 4.00+ | 5,906 | -0.4pp | -3.0 | -0.3pp / -0.6pp | -29.3% | -0.3pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 64,451 | 1,798 | +0.026 | 0.032 | +0.8 | 0.000 |
| basketball | 53,867 | 787 | +0.047 | 0.064 | +0.7 | 0.000 |
| ice hockey | 10,763 | 448 | +0.252 | 0.130 | +1.9 | 0.000 |
| american football | 1,959 | 81 | +0.174 | 0.283 | +0.6 | 0.000 |
| volleyball | 364 | 200 | -0.287 | 0.204 | -1.4 | 0.000 |
| cricket | 119 | 60 | -0.401 | 0.510 | -0.8 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 17,834 | 2,823 | +1.0pp | +1.2 | -6.7% |
| all sports | form 15pp+ below price | 16,936 | 2,762 | -1.4pp | -1.5 | -9.2% |
| all sports | form 5-15pp above | 28,912 | 3,150 | +0.6pp | +1.0 | -6.8% |
| all sports | form 5-15pp below | 28,669 | 3,165 | -0.4pp | -0.6 | -8.2% |
| all sports | form within 5pp | 39,879 | 3,048 | +0.0pp | +0.1 | -7.6% |
| american football | form 15pp+ above price | 245 | 63 | +5.2pp | +0.8 | +1.9% |
| american football | form 15pp+ below price | 247 | 64 | -5.8pp | -0.9 | -17.3% |
| american football | form 5-15pp above | 431 | 79 | -0.7pp | -0.1 | -8.3% |
| american football | form 5-15pp below | 433 | 79 | +0.8pp | +0.2 | -5.3% |
| american football | form within 5pp | 603 | 76 | -0.1pp | -1.0 | -7.1% |
| basketball | form 15pp+ above price | 7,164 | 709 | +0.8pp | +0.5 | -6.4% |
| basketball | form 15pp+ below price | 7,322 | 711 | -0.8pp | -0.5 | -8.9% |
| basketball | form 5-15pp above | 11,775 | 770 | +0.8pp | +0.7 | -5.9% |
| basketball | form 5-15pp below | 11,753 | 769 | -0.9pp | -0.8 | -9.0% |
| basketball | form within 5pp | 15,853 | 726 | -0.0pp | -0.4 | -6.8% |
| football | form 15pp+ above price | 9,377 | 1,679 | +0.8pp | +1.0 | -8.0% |
| football | form 15pp+ below price | 8,301 | 1,588 | -1.5pp | -1.4 | -9.0% |
| football | form 5-15pp above | 13,884 | 1,755 | +0.2pp | +0.4 | -7.9% |
| football | form 5-15pp below | 13,706 | 1,760 | +0.2pp | +0.3 | -7.5% |
| football | form within 5pp | 19,183 | 1,727 | +0.0pp | +0.2 | -8.1% |
| ice hockey | form 15pp+ above price | 798 | 296 | +6.1pp | +2.0 | +5.4% |
| ice hockey | form 15pp+ below price | 835 | 300 | -6.3pp | -2.1 | -17.3% |
| ice hockey | form 5-15pp above | 2,613 | 433 | +1.8pp | +1.1 | -3.9% |
| ice hockey | form 5-15pp below | 2,567 | 433 | -1.6pp | -1.0 | -10.2% |
| ice hockey | form within 5pp | 3,950 | 408 | +0.0pp | +0.2 | -8.2% |
| volleyball | form 15pp+ above price | 41 | 41 | -5.5pp | -0.8 | -26.4% |
| volleyball | form 15pp+ below price | 62 | 62 | +6.5pp | +1.3 | +4.0% |
| volleyball | form 5-15pp above | 63 | 63 | -1.0pp | -0.2 | -12.4% |
| volleyball | form 5-15pp below | 71 | 71 | +2.1pp | +0.4 | -2.4% |
| volleyball | form within 5pp | 127 | 66 | +0.7pp | +2.3 | -7.7% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 5,404 | 338 | +0.0pp | +0.1 | -6.9% |
| researched, not vetoed: same markets | 75,969 | 3,669 | -0.1pp | -0.6 | -6.3% |
| research picks | 1,689 | 1,354 | -0.4pp | -0.3 | -4.8% |
