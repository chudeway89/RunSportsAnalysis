# What the engine has learned (auto, 2026-11-22 18:33 UTC)

Rebuilt every night by `engine/learn.py` from **4,184,733 settled outcomes** on every market of every fixture (2026-10-12 to 2026-11-22). Read by `build_tickets.py`. A number is only "learned" when it holds in both halves of the period, clears 3 standard errors (clustered by fixture) and survives shrinkage by sample size.

## 1. Where the house probability misses (14 of 1169 slices; chance alone would give about 3.2)

| Sport | Market | Side | Odds | Fixtures | Actual − house | z | Early / late | Flat ROI | Correction applied |
|---|---|---|---|---|---|---|---|---|---|
| football | 1X2 & Over/Under 3.5 | other | 4.00+ | 5,546 | -0.6pp | -4.4 | -0.5pp / -0.8pp | -23.3% | -0.5pp |
| football | 1X2 & Over/Under 3.5 | other | 2.20-3.99 | 5,280 | +1.7pp | +4.3 | +1.4pp / +2.0pp | -9.1% | +1.3pp |
| football | Home Team or Over 2.5 | No | 4.00+ | 909 | -4.2pp | -3.9 | -2.8pp / -5.7pp | -44.5% | -1.6pp |
| football | Handicap 0:1 | Draw level | 2.20-3.99 | 3,646 | +2.7pp | +3.7 | +2.5pp / +2.9pp | -3.5% | +1.9pp |
| football | 1st Half - Over/Under | Under | <1.30 | 5,343 | +1.6pp | +3.5 | +1.3pp / +2.1pp | -1.6% | +1.3pp |
| football | Goal Range | other | 2.20-3.99 | 3,547 | -1.9pp | -3.4 | -2.0pp / -1.7pp | -17.4% | -1.3pp |
| football | Winning Margin | other | 2.20-3.99 | 3,061 | +2.3pp | +3.4 | +2.2pp / +2.4pp | -4.4% | +1.6pp |
| football | 2nd Half - 1X2 | Home | 4.00+ | 921 | -3.7pp | -3.3 | -3.9pp / -3.3pp | -31.3% | -1.4pp |
| football | Goal Range | other | 1.60-2.19 | 3,225 | +2.9pp | +3.3 | +3.2pp / +2.5pp | -3.9% | +2.0pp |
| football | 2nd Half - Away Team Clean Sheet | Yes | 1.60-2.19 | 3,537 | +2.7pp | +3.2 | +2.3pp / +3.1pp | -4.2% | +1.9pp |
| football | Away Team Total Corners | Under | 2.20-3.99 | 1,977 | +3.5pp | +3.2 | +3.3pp / +3.7pp | +0.2% | +2.0pp |
| football | Handicap 1:0 | Draw level | 2.20-3.99 | 1,570 | +3.5pp | +3.1 | +3.6pp / +3.3pp | -0.6% | +1.8pp |
| football | Both Halves Over 1.5 | No | 1.30-1.59 | 882 | -5.0pp | -3.1 | -4.7pp / -5.3pp | -11.6% | -1.8pp |
| football | 1X2 & Over/Under 4.5 | other | 4.00+ | 5,534 | -0.4pp | -3.0 | -0.2pp / -0.8pp | -28.7% | -0.4pp |

## 2. Did the automated form research beat the price?

Each night the last-10 trend of both teams is stored for every market *before* kick-off (`papertrade/form/`). `b` is the weight that best explains results in `p = house + b × (trend − house)`: 0 means the price already contains the form, 1 means form is right and the price is wrong.

| Sport | Outcomes | Fixtures | b | SE | z | Weight used |
|---|---|---|---|---|---|---|
| football | 40,807 | 1,203 | +0.048 | 0.039 | +1.2 | 0.000 |
| basketball | 25,103 | 376 | +0.142 | 0.091 | +1.6 | 0.000 |
| ice hockey | 4,249 | 188 | +0.510 | 0.218 | +2.3 | 0.000 |
| american football | 1,498 | 64 | +0.176 | 0.344 | +0.5 | 0.000 |
| volleyball | 191 | 105 | -0.075 | 0.308 | -0.2 | 0.000 |

| Sport | Form v price | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|---|
| all sports | form 15pp+ above price | 9,490 | 1,664 | +2.4pp | +2.3 | -4.2% |
| all sports | form 15pp+ below price | 8,839 | 1,600 | -3.0pp | -2.5 | -12.2% |
| all sports | form 5-15pp above | 15,886 | 1,847 | +0.7pp | +1.0 | -6.8% |
| all sports | form 5-15pp below | 15,854 | 1,858 | -0.5pp | -0.6 | -8.6% |
| all sports | form within 5pp | 22,378 | 1,770 | +0.0pp | +0.5 | -7.8% |
| american football | form 15pp+ above price | 185 | 50 | +7.5pp | +1.0 | +5.8% |
| american football | form 15pp+ below price | 186 | 51 | -7.9pp | -1.0 | -21.6% |
| american football | form 5-15pp above | 317 | 62 | -3.7pp | -0.7 | -14.7% |
| american football | form 5-15pp below | 319 | 62 | +3.9pp | +0.7 | +0.0% |
| american football | form within 5pp | 491 | 60 | -0.1pp | -1.0 | -7.8% |
| basketball | form 15pp+ above price | 3,180 | 331 | +4.0pp | +1.6 | +0.2% |
| basketball | form 15pp+ below price | 3,246 | 333 | -3.7pp | -1.5 | -14.3% |
| basketball | form 5-15pp above | 5,493 | 369 | +1.1pp | +0.6 | -5.1% |
| basketball | form 5-15pp below | 5,500 | 369 | -1.0pp | -0.6 | -8.7% |
| basketball | form within 5pp | 7,684 | 349 | -0.0pp | -0.5 | -7.1% |
| football | form 15pp+ above price | 5,632 | 1,126 | +1.1pp | +1.1 | -7.8% |
| football | form 15pp+ below price | 4,924 | 1,048 | -2.1pp | -1.6 | -10.0% |
| football | form 5-15pp above | 8,889 | 1,170 | +0.3pp | +0.4 | -8.2% |
| football | form 5-15pp below | 8,856 | 1,173 | +0.1pp | +0.1 | -8.1% |
| football | form within 5pp | 12,506 | 1,150 | +0.1pp | +0.5 | -8.1% |
| ice hockey | form 15pp+ above price | 317 | 123 | +10.5pp | +2.1 | +13.9% |
| ice hockey | form 15pp+ below price | 329 | 125 | -10.9pp | -2.2 | -26.7% |
| ice hockey | form 5-15pp above | 1,041 | 183 | +4.4pp | +1.8 | +1.1% |
| ice hockey | form 5-15pp below | 1,031 | 183 | -4.6pp | -1.8 | -17.2% |
| ice hockey | form within 5pp | 1,531 | 164 | +0.3pp | +1.2 | -8.1% |
| volleyball | form 5-15pp above | 41 | 41 | +1.8pp | +0.2 | -4.2% |
| volleyball | form 5-15pp below | 48 | 48 | -0.2pp | -0.0 | -6.0% |

## 3. Our web research against results

| Slice | Outcomes | Fixtures | Actual − house | z | Flat ROI |
|---|---|---|---|---|---|
| vetoed fixtures: short-priced main markets | 3,770 | 254 | -0.3pp | -0.5 | -7.4% |
| researched, not vetoed: same markets | 56,591 | 2,764 | -0.2pp | -1.0 | -6.4% |
| research picks | 1,283 | 1,017 | -0.6pp | -0.4 | -5.2% |
