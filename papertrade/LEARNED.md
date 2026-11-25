# What the engine has learned (auto, 2026-11-25 20:37 UTC)

Rebuilt every night by `engine/learn.py` from **4,400,548 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-25). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (19 of 1225 slices; chance alone would give about 3.3)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,822 | -0.7pp | -4.7 | -0.6pp / -0.8pp | -23.6% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,544 | +1.7pp | +4.5 | +1.6pp / +1.9pp | -8.9% | +1.4pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 961 | -4.1pp | -4.0 | -3.2pp / -5.1pp | -44.6% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,805 | +2.8pp | +3.9 | +2.7pp / +2.9pp | -3.1% | +2.0pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,608 | +1.7pp | +3.8 | +1.2pp / +2.4pp | -1.5% | +1.3pp |
| football | Winning Margin | other | 2.20-3.99 | 3,215 | +2.4pp | +3.6 | +2.7pp / +2.2pp | -3.9% | +1.7pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,070 | +3.7pp | +3.5 | +3.0pp / +4.5pp | +0.7% | +2.1pp |
| football | GG/NG | Yes | 2.20-3.99 | 658 | +6.4pp | +3.3 | +3.9pp / +9.1pp | +4.0% | +1.9pp |
| football | Goal Range | other | 2.20-3.99 | 3,738 | -1.7pp | -3.3 | -1.9pp / -1.6pp | -17.0% | -1.2pp |
| football | 1st Half - Over/Under | Over | 4.00+ | 5,315 | -1.5pp | -3.3 | -0.8pp / -2.3pp | -34.0% | -1.2pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,750 | -3.7pp | -3.2 | -2.8pp / -4.9pp | -10.1% | -2.0pp |
| football | Goal Range | other | 1.60-2.19 | 3,406 | +2.7pp | +3.2 | +2.9pp / +2.4pp | -4.3% | +1.9pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 966 | -3.4pp | -3.1 | -4.3pp / -2.3pp | -30.0% | -1.3pp |
| football | Teams to Score | Both teams | 2.20-3.99 | 647 | +6.0pp | +3.1 | +4.4pp / +7.9pp | +3.5% | +1.8pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,637 | +3.3pp | +3.1 | +3.9pp / +2.8pp | -1.2% | +1.7pp |
| football | 1X2 & Over/Under 4.5 | other | 4.00+ | 5,810 | -0.4pp | -3.1 | -0.2pp / -0.7pp | -29.1% | -0.4pp |
| football | Half Time/Full Time Correct Score | other | 4.00+ | 5,660 | +0.1pp | +3.0 | +0.0pp / +0.1pp | -35.6% | +0.0pp |
| football | 1st Half - Multigoals | other | 4.00+ | 5,651 | -0.8pp | -3.0 | -0.5pp / -1.1pp | -40.5% | -0.6pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 931 | -4.7pp | -3.0 | -4.2pp / -5.2pp | -11.2% | -1.8pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 58,693 | 1,658 | +0.032 | 0.033 | +1.0 | 0.000 |
| basketball | 45,867 | 673 | +0.079 | 0.069 | +1.1 | 0.000 |
| ice hockey | 8,537 | 363 | +0.250 | 0.147 | +1.7 | 0.000 |
| american football | 1,878 | 78 | +0.186 | 0.289 | +0.6 | 0.000 |
| volleyball | 308 | 167 | -0.308 | 0.216 | -1.4 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 15,449 | 2,513 | +1.4pp | +1.6 | -6.1% |
| all sports | form 15pp+ below price | 14,607 | 2,444 | -1.8pp | -1.9 | -10.2% |
| all sports | form 5-15pp above | 25,422 | 2,794 | +0.7pp | +1.1 | -6.7% |
| all sports | form 5-15pp below | 25,206 | 2,809 | -0.5pp | -0.8 | -8.6% |
| all sports | form within 5pp | 35,271 | 2,692 | +0.0pp | +0.3 | -7.7% |
| american football | form 15pp+ above price | 237 | 61 | +6.2pp | +0.9 | +3.7% |
| american football | form 15pp+ below price | 238 | 62 | -6.5pp | -1.0 | -18.9% |
| american football | form 5-15pp above | 415 | 76 | -1.0pp | -0.2 | -8.8% |
| american football | form 5-15pp below | 417 | 76 | +1.1pp | +0.2 | -4.7% |
| american football | form within 5pp | 571 | 73 | -0.1pp | -1.0 | -7.4% |
| basketball | form 15pp+ above price | 6,034 | 602 | +1.7pp | +0.9 | -4.7% |
| basketball | form 15pp+ below price | 6,157 | 604 | -1.6pp | -0.9 | -10.5% |
| basketball | form 5-15pp above | 10,013 | 659 | +1.0pp | +0.8 | -5.6% |
| basketball | form 5-15pp below | 9,994 | 658 | -1.0pp | -0.8 | -9.4% |
| basketball | form within 5pp | 13,669 | 619 | -0.0pp | -0.3 | -6.7% |
| football | form 15pp+ above price | 8,352 | 1,555 | +1.0pp | +1.1 | -7.8% |
| football | form 15pp+ below price | 7,369 | 1,462 | -1.8pp | -1.6 | -9.6% |
| football | form 5-15pp above | 12,733 | 1,616 | +0.3pp | +0.4 | -7.9% |
| football | form 5-15pp below | 12,567 | 1,621 | +0.1pp | +0.1 | -7.7% |
| football | form within 5pp | 17,672 | 1,589 | +0.0pp | +0.4 | -8.4% |
| ice hockey | form 15pp+ above price | 628 | 239 | +5.0pp | +1.5 | +3.6% |
| ice hockey | form 15pp+ below price | 659 | 243 | -5.4pp | -1.7 | -15.2% |
| ice hockey | form 5-15pp above | 2,084 | 350 | +2.3pp | +1.3 | -2.5% |
| ice hockey | form 5-15pp below | 2,046 | 350 | -2.2pp | -1.2 | -11.8% |
| ice hockey | form within 5pp | 3,120 | 326 | +0.1pp | +0.3 | -8.1% |
| volleyball | form 15pp+ above price | 33 | 33 | -5.8pp | -0.8 | -30.8% |
| volleyball | form 15pp+ below price | 48 | 48 | +7.6pp | +1.4 | +5.2% |
| volleyball | form 5-15pp above | 58 | 58 | +0.1pp | +0.0 | -8.9% |
| volleyball | form 5-15pp below | 66 | 66 | +1.2pp | +0.2 | -4.0% |
| volleyball | form within 5pp | 103 | 52 | +0.2pp | +1.0 | -8.2% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 4,908 | 312 | +0.3pp | +0.5 | -6.6% |
| researched, not vetoed: same markets | 70,553 | 3,398 | -0.1pp | -0.8 | -6.4% |
| research picks | 1,552 | 1,243 | -0.5pp | -0.4 | -5.0% |
