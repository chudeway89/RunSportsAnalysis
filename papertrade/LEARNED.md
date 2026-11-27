# What the engine has learned (auto, 2026-11-27 20:06 UTC)

Rebuilt every night by `engine/learn.py` from **4,526,035 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-27). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (20 of 1238 slices; chance alone would give about 3.3)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,980 | -0.7pp | -4.7 | -0.6pp / -0.7pp | -23.5% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,695 | +1.8pp | +4.6 | +1.8pp / +1.8pp | -8.9% | +1.4pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,762 | +1.9pp | +4.2 | +1.1pp / +2.8pp | -1.3% | +1.5pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 995 | -3.9pp | -3.8 | -3.3pp / -4.5pp | -43.5% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,893 | +2.7pp | +3.8 | +2.8pp / +2.5pp | -3.6% | +1.9pp |
| football | 1st Half - Over/Under | Over | 4.00+ | 5,463 | -1.6pp | -3.7 | -0.8pp / -2.7pp | -34.9% | -1.3pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,140 | +3.7pp | +3.6 | +3.4pp / +4.1pp | +0.7% | +2.2pp |
| football | Winning Margin | other | 2.20-3.99 | 3,292 | +2.3pp | +3.5 | +2.5pp / +2.1pp | -4.2% | +1.6pp |
| football | Handicap 0:5 | Away level | <1.30 | 164 | +4.6pp | +3.4 | +0.5pp / +8.0pp | +2.4% | +0.5pp |
| football | GG/NG | Yes | 2.20-3.99 | 679 | +6.4pp | +3.4 | +4.2pp / +8.9pp | +4.1% | +2.0pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,804 | -3.8pp | -3.3 | -3.2pp / -4.5pp | -10.2% | -2.1pp |
| football | 1st Half - Multigoals | other | 4.00+ | 5,805 | -0.8pp | -3.3 | -0.5pp / -1.3pp | -41.1% | -0.7pp |
| football | Goal Range | other | 1.60-2.19 | 3,512 | +2.8pp | +3.3 | +2.8pp / +2.8pp | -4.1% | +1.9pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,662 | +3.5pp | +3.2 | +3.6pp / +3.4pp | -0.7% | +1.8pp |
| football | Goal Range | other | 2.20-3.99 | 3,854 | -1.7pp | -3.2 | -1.7pp / -1.6pp | -16.8% | -1.2pp |
| football | Teams to Score | Both teams | 2.20-3.99 | 667 | +6.0pp | +3.1 | +4.8pp / +7.4pp | +3.6% | +1.9pp |
| football | GG/NG | No | 1.30-1.59 | 858 | -5.2pp | -3.0 | -2.3pp / -8.2pp | -15.2% | -1.9pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 957 | -4.7pp | -3.0 | -4.1pp / -5.3pp | -11.2% | -1.8pp |
| football | GG/NG | No | 2.20-3.99 | 2,815 | +2.8pp | +3.0 | +2.0pp / +3.6pp | -3.8% | +1.8pp |
| football | Half Time/Full Time Correct Score | other | 4.00+ | 5,814 | +0.1pp | +3.0 | +0.0pp / +0.1pp | -35.4% | +0.0pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 68,518 | 1,910 | +0.021 | 0.031 | +0.7 | 0.000 |
| basketball | 55,524 | 816 | +0.035 | 0.063 | +0.6 | 0.000 |
| ice hockey | 11,853 | 503 | +0.185 | 0.124 | +1.5 | 0.000 |
| american football | 2,035 | 84 | +0.109 | 0.272 | +0.4 | 0.000 |
| volleyball | 389 | 213 | -0.301 | 0.198 | -1.5 | 0.000 |
| cricket | 127 | 64 | -0.388 | 0.459 | -0.8 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 18,743 | 3,004 | +0.8pp | +1.0 | -7.2% |
| all sports | form 15pp+ below price | 17,765 | 2,937 | -1.1pp | -1.3 | -8.8% |
| all sports | form 5-15pp above | 30,500 | 3,355 | +0.5pp | +0.8 | -7.0% |
| all sports | form 5-15pp below | 30,247 | 3,368 | -0.3pp | -0.5 | -8.1% |
| all sports | form within 5pp | 41,997 | 3,235 | +0.0pp | +0.5 | -7.6% |
| american football | form 15pp+ above price | 257 | 66 | +3.4pp | +0.5 | -1.4% |
| american football | form 15pp+ below price | 259 | 67 | -4.0pp | -0.6 | -14.0% |
| american football | form 5-15pp above | 442 | 82 | -0.8pp | -0.2 | -8.4% |
| american football | form 5-15pp below | 444 | 82 | +0.9pp | +0.2 | -5.2% |
| american football | form within 5pp | 633 | 79 | -0.1pp | -1.0 | -7.3% |
| basketball | form 15pp+ above price | 7,382 | 734 | +0.7pp | +0.4 | -6.5% |
| basketball | form 15pp+ below price | 7,544 | 736 | -0.7pp | -0.4 | -8.7% |
| basketball | form 5-15pp above | 12,163 | 799 | +0.6pp | +0.5 | -6.4% |
| basketball | form 5-15pp below | 12,142 | 798 | -0.6pp | -0.6 | -8.5% |
| basketball | form within 5pp | 16,293 | 754 | -0.0pp | -0.4 | -6.8% |
| football | form 15pp+ above price | 9,927 | 1,787 | +0.6pp | +0.8 | -8.5% |
| football | form 15pp+ below price | 8,760 | 1,689 | -1.3pp | -1.3 | -8.6% |
| football | form 5-15pp above | 14,806 | 1,865 | +0.3pp | +0.6 | -7.7% |
| football | form 5-15pp below | 14,623 | 1,869 | +0.1pp | +0.1 | -7.7% |
| football | form within 5pp | 20,402 | 1,833 | +0.1pp | +0.7 | -8.0% |
| ice hockey | form 15pp+ above price | 901 | 334 | +4.5pp | +1.6 | +2.3% |
| ice hockey | form 15pp+ below price | 944 | 339 | -4.5pp | -1.7 | -14.0% |
| ice hockey | form 5-15pp above | 2,851 | 483 | +1.2pp | +0.8 | -4.6% |
| ice hockey | form 5-15pp below | 2,802 | 483 | -1.0pp | -0.6 | -8.8% |
| ice hockey | form within 5pp | 4,355 | 451 | -0.0pp | -0.2 | -8.2% |
| volleyball | form 15pp+ above price | 43 | 43 | -6.6pp | -1.0 | -29.9% |
| volleyball | form 15pp+ below price | 64 | 64 | +7.2pp | +1.5 | +4.9% |
| volleyball | form 5-15pp above | 70 | 70 | +0.5pp | +0.1 | -9.5% |
| volleyball | form 5-15pp below | 77 | 77 | +0.9pp | +0.2 | -4.3% |
| volleyball | form within 5pp | 135 | 70 | +0.7pp | +2.3 | -7.9% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 5,404 | 338 | +0.0pp | +0.1 | -6.9% |
| researched, not vetoed: same markets | 76,205 | 3,678 | -0.1pp | -0.6 | -6.3% |
| research picks | 1,692 | 1,356 | -0.3pp | -0.3 | -4.8% |
