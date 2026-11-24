# What the engine has learned (auto, 2026-11-24 21:14 UTC)

Rebuilt every night by `engine/learn.py` from **4,316,769 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-24). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (15 of 1202 slices; chance alone would give about 3.2)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,709 | -0.6pp | -4.6 | -0.6pp / -0.7pp | -23.4% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,434 | +1.7pp | +4.4 | +1.6pp / +1.9pp | -9.1% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 941 | -4.2pp | -4.1 | -3.2pp / -5.4pp | -44.8% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,751 | +2.8pp | +3.9 | +2.7pp / +2.9pp | -3.2% | +2.0pp |
| football | Winning Margin | other | 2.20-3.99 | 3,155 | +2.5pp | +3.7 | +2.7pp / +2.3pp | -3.8% | +1.7pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,500 | +1.6pp | +3.5 | +1.2pp / +2.1pp | -1.6% | +1.2pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 2,033 | +3.7pp | +3.4 | +3.0pp / +4.6pp | +0.6% | +2.1pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,613 | +3.6pp | +3.3 | +3.9pp / +3.3pp | -0.2% | +1.9pp |
| football | Goal Range | other | 2.20-3.99 | 3,665 | -1.7pp | -3.2 | -1.9pp / -1.6pp | -17.0% | -1.2pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 946 | -3.5pp | -3.2 | -4.3pp / -2.5pp | -30.4% | -1.4pp |
| football | GG/NG | Yes | 2.20-3.99 | 652 | +6.2pp | +3.2 | +3.9pp / +8.7pp | +3.5% | +1.9pp |
| football | Away Team Total Corners | Over | 1.30-1.59 | 1,723 | -3.7pp | -3.2 | -2.8pp / -4.8pp | -10.0% | -2.0pp |
| football | Goal Range | other | 1.60-2.19 | 3,336 | +2.6pp | +3.1 | +2.9pp / +2.3pp | -4.4% | +1.8pp |
| football | GG/NG | No | 2.20-3.99 | 2,691 | +2.8pp | +3.0 | +1.7pp / +4.1pp | -3.7% | +1.8pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 916 | -4.7pp | -3.0 | -4.2pp / -5.3pp | -11.3% | -1.8pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 51,666 | 1,478 | +0.042 | 0.035 | +1.2 | 0.000 |
| basketball | 38,705 | 563 | +0.138 | 0.074 | +1.9 | 0.000 |
| ice hockey | 7,406 | 311 | +0.218 | 0.160 | +1.4 | 0.000 |
| american football | 1,816 | 76 | +0.126 | 0.291 | +0.4 | 0.000 |
| volleyball | 265 | 144 | -0.296 | 0.264 | -1.1 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 13,114 | 2,196 | +2.1pp | +2.2 | -4.9% |
| all sports | form 15pp+ below price | 12,352 | 2,125 | -2.6pp | -2.6 | -11.7% |
| all sports | form 5-15pp above | 22,033 | 2,453 | +0.9pp | +1.4 | -6.3% |
| all sports | form 5-15pp below | 21,878 | 2,466 | -0.7pp | -1.1 | -9.1% |
| all sports | form within 5pp | 31,143 | 2,364 | -0.0pp | -0.2 | -7.7% |
| american football | form 15pp+ above price | 228 | 59 | +5.1pp | +0.8 | +1.6% |
| american football | form 15pp+ below price | 229 | 60 | -5.4pp | -0.8 | -17.1% |
| american football | form 5-15pp above | 398 | 74 | -2.1pp | -0.4 | -11.0% |
| american football | form 5-15pp below | 400 | 74 | +2.3pp | +0.5 | -2.5% |
| american football | form within 5pp | 561 | 71 | -0.1pp | -1.0 | -7.5% |
| basketball | form 15pp+ above price | 4,924 | 497 | +3.5pp | +1.8 | -1.4% |
| basketball | form 15pp+ below price | 5,034 | 499 | -3.4pp | -1.7 | -14.0% |
| basketball | form 5-15pp above | 8,422 | 550 | +1.7pp | +1.3 | -4.1% |
| basketball | form 5-15pp below | 8,410 | 549 | -1.7pp | -1.3 | -10.6% |
| basketball | form within 5pp | 11,915 | 519 | -0.0pp | -0.6 | -6.7% |
| football | form 15pp+ above price | 7,236 | 1,386 | +1.1pp | +1.2 | -7.6% |
| football | form 15pp+ below price | 6,352 | 1,295 | -2.1pp | -1.8 | -10.1% |
| football | form 5-15pp above | 11,225 | 1,442 | +0.2pp | +0.3 | -8.2% |
| football | form 5-15pp below | 11,114 | 1,445 | +0.1pp | +0.2 | -7.8% |
| football | form within 5pp | 15,739 | 1,416 | -0.0pp | -0.1 | -8.4% |
| ice hockey | form 15pp+ above price | 537 | 207 | +3.8pp | +1.1 | +0.3% |
| ice hockey | form 15pp+ below price | 565 | 210 | -4.2pp | -1.2 | -13.2% |
| ice hockey | form 5-15pp above | 1,818 | 301 | +2.4pp | +1.3 | -2.2% |
| ice hockey | form 5-15pp below | 1,779 | 301 | -2.5pp | -1.2 | -12.4% |
| ice hockey | form within 5pp | 2,707 | 282 | +0.1pp | +0.7 | -8.0% |
| volleyball | form 15pp+ below price | 37 | 37 | +7.2pp | +1.1 | +6.1% |
| volleyball | form 5-15pp above | 52 | 52 | +1.4pp | +0.2 | -5.3% |
| volleyball | form 5-15pp below | 60 | 60 | +0.2pp | +0.0 | -5.1% |
| volleyball | form within 5pp | 91 | 46 | +0.2pp | +1.0 | -10.3% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 4,636 | 303 | +0.4pp | +0.7 | -6.4% |
| researched, not vetoed: same markets | 67,068 | 3,252 | -0.2pp | -0.9 | -6.4% |
| research picks | 1,490 | 1,196 | -0.6pp | -0.5 | -5.2% |
