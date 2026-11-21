# What the engine has learned (auto, 2026-11-21 20:49 UTC)

Rebuilt every night by `engine/learn.py` from **4,001,086 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-21). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (13 of 1142 slices; chance alone would give about 3.1)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,354 | -0.6pp | -4.3 | -0.4pp / -0.9pp | -23.0% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,096 | +1.7pp | +4.2 | +1.1pp / +2.3pp | -9.0% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 874 | -4.4pp | -4.1 | -2.5pp / -6.2pp | -45.1% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,442 | +2.6pp | +3.5 | +2.5pp / +2.7pp | -3.8% | +1.8pp |
| football | Goal Range | other | 1.60-2.19 | 3,102 | +3.1pp | +3.4 | +3.0pp / +3.1pp | -3.6% | +2.1pp |
| football | Goal Range | other | 2.20-3.99 | 3,414 | -1.9pp | -3.4 | -2.0pp / -1.8pp | -17.6% | -1.3pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,156 | +1.5pp | +3.2 | +1.5pp / +1.5pp | -1.7% | +1.2pp |
| football | Home Team Total Corners | Over | <1.30 | 960 | -4.5pp | -3.2 | -2.8pp / -6.5pp | -9.4% | -1.8pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 869 | -3.6pp | -3.1 | -3.6pp / -3.5pp | -30.5% | -1.3pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 1,894 | +3.4pp | +3.1 | +3.3pp / +3.6pp | +0.1% | +1.9pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,464 | +3.6pp | +3.1 | +4.5pp / +2.8pp | -0.3% | +1.8pp |
| football | Winning Margin | other | 2.20-3.99 | 2,965 | +2.1pp | +3.0 | +2.0pp / +2.2pp | -5.1% | +1.4pp |
| football | GG/NG | Yes | 2.20-3.99 | 609 | +6.0pp | +3.0 | +4.7pp / +7.3pp | +3.3% | +1.7pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 23,442 | 654 | +0.054 | 0.054 | +1.0 | 0.000 |
| basketball | 12,766 | 196 | +0.083 | 0.129 | +0.6 | 0.000 |
| ice hockey | 1,739 | 76 | +0.749 | 0.330 | +2.3 | 0.000 |
| volleyball | 104 | 56 | -0.354 | 0.377 | -0.9 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 5,089 | 873 | +1.1pp | +0.8 | -6.4% |
| all sports | form 15pp+ below price | 4,802 | 828 | -1.7pp | -1.1 | -9.2% |
| all sports | form 5-15pp above | 8,500 | 952 | +0.9pp | +0.8 | -6.1% |
| all sports | form 5-15pp below | 8,468 | 955 | -0.4pp | -0.4 | -8.1% |
| all sports | form within 5pp | 11,951 | 917 | +0.1pp | +1.2 | -7.8% |
| basketball | form 15pp+ above price | 1,689 | 173 | +1.2pp | +0.3 | -4.6% |
| basketball | form 15pp+ below price | 1,718 | 174 | -0.9pp | -0.3 | -8.3% |
| basketball | form 5-15pp above | 2,783 | 191 | +0.8pp | +0.3 | -5.2% |
| basketball | form 5-15pp below | 2,771 | 191 | -0.7pp | -0.3 | -7.2% |
| basketball | form within 5pp | 3,805 | 181 | -0.1pp | -0.9 | -7.3% |
| football | form 15pp+ above price | 3,099 | 618 | +1.1pp | +0.8 | -7.9% |
| football | form 15pp+ below price | 2,796 | 566 | -2.2pp | -1.3 | -10.0% |
| football | form 5-15pp above | 5,120 | 638 | +0.3pp | +0.3 | -7.7% |
| football | form 5-15pp below | 5,101 | 638 | +0.3pp | +0.3 | -7.4% |
| football | form within 5pp | 7,326 | 632 | +0.3pp | +1.7 | -8.0% |
| ice hockey | form 15pp+ above price | 127 | 50 | +9.0pp | +1.2 | +10.4% |
| ice hockey | form 15pp+ below price | 134 | 52 | -10.2pp | -1.4 | -23.8% |
| ice hockey | form 5-15pp above | 438 | 76 | +11.9pp | +3.3 | +15.0% |
| ice hockey | form 5-15pp below | 440 | 76 | -11.4pp | -3.1 | -30.9% |
| ice hockey | form within 5pp | 600 | 69 | +0.5pp | +1.2 | -8.3% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 2,272 | 152 | -0.6pp | -0.8 | -7.6% |
| researched, not vetoed: same markets | 43,696 | 1,994 | -0.2pp | -0.7 | -6.2% |
| research picks | 973 | 755 | -1.3pp | -0.8 | -6.2% |
