# What the engine has learned (auto, 2026-11-26 20:14 UTC)

Rebuilt every night by `engine/learn.py` from **4,460,032 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-26). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (22 of 1232 slices; chance alone would give about 3.3)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,894 | -0.7pp | -4.8 | -0.6pp / -0.7pp | -23.6% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,610 | +1.8pp | +4.7 | +1.8pp / +1.8pp | -8.8% | +1.4pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,677 | +1.8pp | +4.0 | +1.1pp / +2.7pp | -1.4% | +1.4pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 980 | -4.0pp | -4.0 | -3.3pp / -4.8pp | -44.3% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,840 | +2.7pp | +3.8 | +2.8pp / +2.6pp | -3.4% | +1.9pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,108 | +3.7pp | +3.5 | +3.4pp / +4.1pp | +0.7% | +2.2pp |
| football | Winning Margin | other | 2.20-3.99 | 3,245 | +2.3pp | +3.5 | +2.5pp / +2.2pp | -4.2% | +1.6pp |
| football | 1st Half - Over/Under | Over | 4.00+ | 5,381 | -1.6pp | -3.5 | -0.8pp / -2.6pp | -34.5% | -1.2pp |
| football | GG/NG | Yes | 2.20-3.99 | 667 | +6.5pp | +3.4 | +4.2pp / +9.1pp | +4.3% | +2.0pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,780 | -3.9pp | -3.4 | -3.2pp / -4.6pp | -10.3% | -2.1pp |
| football | Goal Range | other | 2.20-3.99 | 3,797 | -1.7pp | -3.3 | -1.7pp / -1.8pp | -17.0% | -1.2pp |
| football | Goal Range | other | 1.60-2.19 | 3,458 | +2.7pp | +3.2 | +2.8pp / +2.6pp | -4.3% | +1.9pp |
| football | Teams to Score | Both teams | 2.20-3.99 | 656 | +6.2pp | +3.2 | +4.8pp / +7.8pp | +3.9% | +1.9pp |
| football | Handicap 0:5 | Away level | <1.30 | 157 | +4.4pp | +3.2 | +0.5pp / +7.9pp | +2.2% | +0.4pp |
| football | GG/NG | No | 2.20-3.99 | 2,774 | +2.9pp | +3.1 | +2.0pp / +3.9pp | -3.6% | +1.9pp |
| football | 1st Half - Multigoals | other | 4.00+ | 5,720 | -0.8pp | -3.1 | -0.5pp / -1.3pp | -40.8% | -0.6pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 946 | -4.8pp | -3.1 | -4.1pp / -5.5pp | -11.3% | -1.8pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 975 | -3.3pp | -3.0 | -4.1pp / -2.4pp | -29.6% | -1.3pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,650 | +3.3pp | +3.0 | +3.6pp / +3.1pp | -1.3% | +1.7pp |
| football | 1X2 & Over/Under 4.5 | other | 4.00+ | 5,882 | -0.4pp | -3.0 | -0.3pp / -0.6pp | -29.3% | -0.3pp |
| football | Half Time/Full Time Correct Score | other | 4.00+ | 5,729 | +0.1pp | +3.0 | +0.0pp / +0.1pp | -35.6% | +0.0pp |
| football | GG/NG | No | 1.30-1.59 | 843 | -5.1pp | -3.0 | -2.3pp / -8.3pp | -15.1% | -1.8pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 63,009 | 1,768 | +0.025 | 0.032 | +0.8 | 0.000 |
| basketball | 51,825 | 759 | +0.053 | 0.065 | +0.8 | 0.000 |
| ice hockey | 10,294 | 429 | +0.266 | 0.134 | +2.0 | 0.000 |
| american football | 1,904 | 79 | +0.205 | 0.288 | +0.7 | 0.000 |
| volleyball | 354 | 194 | -0.315 | 0.204 | -1.6 | 0.000 |
| cricket | 119 | 60 | -0.401 | 0.510 | -0.8 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 17,185 | 2,753 | +1.2pp | +1.4 | -6.6% |
| all sports | form 15pp+ below price | 16,317 | 2,690 | -1.5pp | -1.7 | -9.6% |
| all sports | form 5-15pp above | 28,082 | 3,066 | +0.6pp | +1.0 | -6.8% |
| all sports | form 5-15pp below | 27,841 | 3,081 | -0.4pp | -0.7 | -8.3% |
| all sports | form within 5pp | 38,691 | 2,965 | +0.0pp | +0.1 | -7.5% |
| american football | form 15pp+ above price | 237 | 61 | +6.2pp | +0.9 | +3.7% |
| american football | form 15pp+ below price | 238 | 62 | -6.5pp | -1.0 | -18.9% |
| american football | form 5-15pp above | 422 | 77 | -0.5pp | -0.1 | -8.0% |
| american football | form 5-15pp below | 424 | 77 | +0.7pp | +0.1 | -5.5% |
| american football | form within 5pp | 583 | 74 | -0.1pp | -1.0 | -7.3% |
| basketball | form 15pp+ above price | 6,879 | 682 | +1.1pp | +0.6 | -6.0% |
| basketball | form 15pp+ below price | 7,025 | 684 | -1.0pp | -0.6 | -9.4% |
| basketball | form 5-15pp above | 11,352 | 742 | +0.7pp | +0.6 | -6.1% |
| basketball | form 5-15pp below | 11,330 | 741 | -0.8pp | -0.7 | -8.8% |
| basketball | form within 5pp | 15,239 | 700 | -0.0pp | -0.1 | -6.6% |
| football | form 15pp+ above price | 9,093 | 1,655 | +0.9pp | +1.0 | -8.1% |
| football | form 15pp+ below price | 8,051 | 1,563 | -1.6pp | -1.5 | -9.2% |
| football | form 5-15pp above | 13,616 | 1,725 | +0.3pp | +0.4 | -7.8% |
| football | form 5-15pp below | 13,435 | 1,730 | +0.1pp | +0.2 | -7.6% |
| football | form within 5pp | 18,814 | 1,697 | +0.0pp | +0.2 | -8.1% |
| ice hockey | form 15pp+ above price | 763 | 285 | +6.0pp | +2.0 | +5.2% |
| ice hockey | form 15pp+ below price | 797 | 288 | -6.2pp | -2.1 | -17.3% |
| ice hockey | form 5-15pp above | 2,500 | 415 | +2.1pp | +1.3 | -3.3% |
| ice hockey | form 5-15pp below | 2,455 | 415 | -1.9pp | -1.2 | -11.1% |
| ice hockey | form within 5pp | 3,779 | 390 | -0.0pp | -0.1 | -8.1% |
| volleyball | form 15pp+ above price | 40 | 40 | -7.2pp | -1.1 | -30.5% |
| volleyball | form 15pp+ below price | 61 | 61 | +7.6pp | +1.5 | +5.7% |
| volleyball | form 5-15pp above | 62 | 62 | -0.5pp | -0.1 | -11.0% |
| volleyball | form 5-15pp below | 70 | 70 | +1.6pp | +0.3 | -3.1% |
| volleyball | form within 5pp | 121 | 62 | +0.5pp | +1.8 | -8.0% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 5,347 | 334 | +0.0pp | +0.1 | -6.9% |
| researched, not vetoed: same markets | 74,282 | 3,592 | -0.1pp | -0.7 | -6.3% |
| research picks | 1,651 | 1,324 | -0.6pp | -0.5 | -5.1% |
