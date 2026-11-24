# What the engine has learned (auto, 2026-11-24 05:42 UTC)

Rebuilt every night by `engine/learn.py` from **4,282,223 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-24). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (15 of 1197 slices; chance alone would give about 3.2)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,666 | -0.6pp | -4.5 | -0.6pp / -0.7pp | -23.4% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,394 | +1.7pp | +4.4 | +1.6pp / +1.8pp | -9.1% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 931 | -4.2pp | -4.1 | -3.2pp / -5.4pp | -44.8% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,722 | +2.7pp | +3.7 | +2.7pp / +2.7pp | -3.5% | +1.9pp |
| football | Winning Margin | other | 2.20-3.99 | 3,128 | +2.5pp | +3.6 | +2.7pp / +2.2pp | -3.9% | +1.7pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,461 | +1.6pp | +3.5 | +1.2pp / +2.2pp | -1.6% | +1.3pp |
| football | Goal Range | other | 2.20-3.99 | 3,630 | -1.8pp | -3.4 | -1.9pp / -1.8pp | -17.3% | -1.3pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,022 | +3.5pp | +3.3 | +3.0pp / +4.3pp | +0.3% | +2.0pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,605 | +3.6pp | +3.2 | +3.9pp / +3.2pp | -0.4% | +1.8pp |
| football | Goal Range | other | 1.60-2.19 | 3,300 | +2.7pp | +3.2 | +2.9pp / +2.5pp | -4.2% | +1.9pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 937 | -3.5pp | -3.1 | -4.3pp / -2.4pp | -30.2% | -1.3pp |
| football | GG/NG | Yes | 2.20-3.99 | 644 | +6.1pp | +3.1 | +3.9pp / +8.7pp | +3.3% | +1.8pp |
| football | GG/NG | No | 2.20-3.99 | 2,670 | +2.9pp | +3.1 | +1.7pp / +4.3pp | -3.6% | +1.9pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 901 | -4.8pp | -3.0 | -4.2pp / -5.5pp | -11.4% | -1.8pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,712 | -3.5pp | -3.0 | -2.8pp / -4.4pp | -9.7% | -1.9pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 48,712 | 1,403 | +0.054 | 0.036 | +1.5 | 0.000 |
| basketball | 37,051 | 540 | +0.139 | 0.076 | +1.8 | 0.000 |
| ice hockey | 5,776 | 248 | +0.248 | 0.182 | +1.4 | 0.000 |
| american football | 1,816 | 76 | +0.126 | 0.291 | +0.4 | 0.000 |
| volleyball | 237 | 130 | -0.292 | 0.273 | -1.1 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 12,310 | 2,056 | +2.3pp | +2.4 | -4.4% |
| all sports | form 15pp+ below price | 11,595 | 1,989 | -2.8pp | -2.7 | -12.1% |
| all sports | form 5-15pp above | 20,664 | 2,286 | +0.9pp | +1.4 | -6.4% |
| all sports | form 5-15pp below | 20,539 | 2,299 | -0.7pp | -1.1 | -9.1% |
| all sports | form within 5pp | 29,123 | 2,198 | +0.0pp | +0.1 | -7.6% |
| american football | form 15pp+ above price | 228 | 59 | +5.1pp | +0.8 | +1.6% |
| american football | form 15pp+ below price | 229 | 60 | -5.4pp | -0.8 | -17.1% |
| american football | form 5-15pp above | 398 | 74 | -2.1pp | -0.4 | -11.0% |
| american football | form 5-15pp below | 400 | 74 | +2.3pp | +0.5 | -2.5% |
| american football | form within 5pp | 561 | 71 | -0.1pp | -1.0 | -7.5% |
| basketball | form 15pp+ above price | 4,687 | 478 | +3.7pp | +1.9 | -1.0% |
| basketball | form 15pp+ below price | 4,791 | 480 | -3.6pp | -1.8 | -14.4% |
| basketball | form 5-15pp above | 8,074 | 527 | +1.6pp | +1.1 | -4.7% |
| basketball | form 5-15pp below | 8,058 | 526 | -1.5pp | -1.1 | -10.2% |
| basketball | form within 5pp | 11,441 | 497 | -0.0pp | -0.2 | -6.7% |
| football | form 15pp+ above price | 6,785 | 1,312 | +1.3pp | +1.4 | -7.1% |
| football | form 15pp+ below price | 5,965 | 1,228 | -2.2pp | -1.8 | -10.3% |
| football | form 5-15pp above | 10,612 | 1,368 | +0.5pp | +0.6 | -7.8% |
| football | form 5-15pp below | 10,517 | 1,371 | -0.1pp | -0.1 | -8.3% |
| football | form within 5pp | 14,833 | 1,345 | +0.0pp | +0.1 | -8.3% |
| ice hockey | form 15pp+ above price | 425 | 164 | +4.4pp | +1.1 | +2.0% |
| ice hockey | form 15pp+ below price | 444 | 166 | -4.7pp | -1.1 | -14.7% |
| ice hockey | form 5-15pp above | 1,419 | 240 | +2.5pp | +1.2 | -2.4% |
| ice hockey | form 5-15pp below | 1,398 | 240 | -2.4pp | -1.1 | -12.7% |
| ice hockey | form within 5pp | 2,090 | 221 | +0.1pp | +0.7 | -7.8% |
| volleyball | form 15pp+ below price | 35 | 35 | +6.1pp | +0.9 | +4.7% |
| volleyball | form 5-15pp above | 48 | 48 | -0.1pp | -0.0 | -8.7% |
| volleyball | form 5-15pp below | 56 | 56 | +1.6pp | +0.3 | -3.1% |
| volleyball | form within 5pp | 75 | 38 | +0.3pp | +1.0 | -11.3% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 4,371 | 286 | +0.5pp | +0.8 | -6.3% |
| researched, not vetoed: same markets | 65,012 | 3,122 | -0.1pp | -0.8 | -6.4% |
| research picks | 1,421 | 1,132 | -0.8pp | -0.6 | -5.4% |
