# What the engine has learned (auto, 2026-11-26 04:01 UTC)

Rebuilt every night by `engine/learn.py` from **4,429,752 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-26). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (19 of 1230 slices; chance alone would give about 3.3)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,857 | -0.7pp | -4.7 | -0.6pp / -0.7pp | -23.6% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,577 | +1.7pp | +4.6 | +1.8pp / +1.7pp | -8.9% | +1.4pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,642 | +1.8pp | +4.0 | +1.1pp / +2.6pp | -1.4% | +1.4pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 971 | -4.0pp | -3.9 | -3.3pp / -4.9pp | -44.2% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,819 | +2.7pp | +3.8 | +2.8pp / +2.7pp | -3.4% | +2.0pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,089 | +3.8pp | +3.6 | +3.4pp / +4.3pp | +1.0% | +2.2pp |
| football | Winning Margin | other | 2.20-3.99 | 3,229 | +2.3pp | +3.5 | +2.5pp / +2.1pp | -4.3% | +1.6pp |
| football | 1st Half - Over/Under | Over | 4.00+ | 5,346 | -1.5pp | -3.4 | -0.8pp / -2.5pp | -34.3% | -1.2pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,767 | -3.8pp | -3.4 | -3.2pp / -4.6pp | -10.3% | -2.1pp |
| football | GG/NG | Yes | 2.20-3.99 | 658 | +6.4pp | +3.3 | +4.2pp / +8.9pp | +4.0% | +1.9pp |
| football | Goal Range | other | 2.20-3.99 | 3,767 | -1.7pp | -3.3 | -1.7pp / -1.8pp | -17.0% | -1.2pp |
| football | Goal Range | other | 1.60-2.19 | 3,432 | +2.7pp | +3.2 | +2.8pp / +2.6pp | -4.2% | +1.9pp |
| football | 1X2 & Over/Under 4.5 | other | 4.00+ | 5,845 | -0.5pp | -3.1 | -0.3pp / -0.7pp | -29.3% | -0.4pp |
| football | 1st Half - Multigoals | other | 4.00+ | 5,685 | -0.8pp | -3.1 | -0.5pp / -1.3pp | -40.8% | -0.6pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,639 | +3.4pp | +3.1 | +3.6pp / +3.2pp | -1.1% | +1.8pp |
| football | Teams to Score | Both teams | 2.20-3.99 | 647 | +6.0pp | +3.1 | +4.8pp / +7.5pp | +3.5% | +1.8pp |
| football | Half Time/Full Time Correct Score | other | 4.00+ | 5,694 | +0.1pp | +3.1 | +0.0pp / +0.1pp | -35.6% | +0.0pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 969 | -3.3pp | -3.1 | -4.1pp / -2.4pp | -29.7% | -1.3pp |
| football | GG/NG | No | 2.20-3.99 | 2,761 | +2.8pp | +3.0 | +2.0pp / +3.7pp | -3.8% | +1.8pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 60,476 | 1,701 | +0.031 | 0.033 | +1.0 | 0.000 |
| basketball | 49,408 | 724 | +0.038 | 0.066 | +0.6 | 0.000 |
| ice hockey | 9,313 | 391 | +0.253 | 0.140 | +1.8 | 0.000 |
| american football | 1,878 | 78 | +0.186 | 0.289 | +0.6 | 0.000 |
| volleyball | 324 | 177 | -0.192 | 0.211 | -0.9 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 16,334 | 2,625 | +1.2pp | +1.4 | -6.6% |
| all sports | form 15pp+ below price | 15,486 | 2,558 | -1.5pp | -1.6 | -9.6% |
| all sports | form 5-15pp above | 26,758 | 2,915 | +0.4pp | +0.6 | -7.2% |
| all sports | form 5-15pp below | 26,522 | 2,929 | -0.2pp | -0.4 | -8.0% |
| all sports | form within 5pp | 36,983 | 2,812 | +0.0pp | +0.3 | -7.6% |
| american football | form 15pp+ above price | 237 | 61 | +6.2pp | +0.9 | +3.7% |
| american football | form 15pp+ below price | 238 | 62 | -6.5pp | -1.0 | -18.9% |
| american football | form 5-15pp above | 415 | 76 | -1.0pp | -0.2 | -8.8% |
| american football | form 5-15pp below | 417 | 76 | +1.1pp | +0.2 | -4.7% |
| american football | form within 5pp | 571 | 73 | -0.1pp | -1.0 | -7.4% |
| basketball | form 15pp+ above price | 6,534 | 648 | +0.8pp | +0.4 | -6.6% |
| basketball | form 15pp+ below price | 6,668 | 650 | -0.7pp | -0.4 | -8.9% |
| basketball | form 5-15pp above | 10,819 | 707 | +0.6pp | +0.5 | -6.4% |
| basketball | form 5-15pp below | 10,796 | 706 | -0.6pp | -0.5 | -8.4% |
| basketball | form within 5pp | 14,591 | 666 | +0.0pp | +0.0 | -6.6% |
| football | form 15pp+ above price | 8,655 | 1,595 | +1.1pp | +1.3 | -7.6% |
| football | form 15pp+ below price | 7,646 | 1,500 | -1.7pp | -1.6 | -9.7% |
| football | form 5-15pp above | 13,093 | 1,658 | +0.1pp | +0.2 | -8.2% |
| football | form 5-15pp below | 12,919 | 1,663 | +0.2pp | +0.3 | -7.6% |
| football | form within 5pp | 18,163 | 1,632 | +0.0pp | +0.3 | -8.2% |
| ice hockey | form 15pp+ above price | 705 | 261 | +6.0pp | +1.9 | +4.9% |
| ice hockey | form 15pp+ below price | 740 | 265 | -6.2pp | -2.0 | -17.3% |
| ice hockey | form 5-15pp above | 2,250 | 377 | +1.7pp | +1.0 | -3.7% |
| ice hockey | form 5-15pp below | 2,205 | 377 | -1.5pp | -0.8 | -9.9% |
| ice hockey | form within 5pp | 3,413 | 353 | +0.0pp | +0.1 | -8.3% |
| volleyball | form 15pp+ above price | 35 | 35 | -2.4pp | -0.3 | -20.5% |
| volleyball | form 15pp+ below price | 54 | 54 | +4.3pp | +0.8 | -0.0% |
| volleyball | form 5-15pp above | 60 | 60 | +0.8pp | +0.1 | -8.0% |
| volleyball | form 5-15pp below | 68 | 68 | +0.5pp | +0.1 | -5.0% |
| volleyball | form within 5pp | 107 | 54 | +0.2pp | +1.0 | -8.1% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 5,184 | 326 | +0.1pp | +0.2 | -6.8% |
| researched, not vetoed: same markets | 72,115 | 3,470 | -0.1pp | -0.8 | -6.3% |
| research picks | 1,589 | 1,275 | -0.6pp | -0.5 | -5.1% |
