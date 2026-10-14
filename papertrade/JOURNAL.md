# Paper-trade learning journal

Written automatically by `.github/workflows/papertrade.yml` via `engine/journal.py`. A market is stakeable only once it shows **PASS** (n ≥ 300, model log-loss below the house, EV ≥ 1.05 picks with ROI > 0).

## Day 1 — 2026-10-12 22:32 UTC
Run: FAILED | snapshot ? outcomes / ? events | failed steps: none
Graded outcomes to date: 1746

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 688 | 0.6476 | 0.6439 | +0.0037 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 284 | 0.6944 | 0.6934 | +0.0009 | 5 | -0.440 | collecting |
| football | 166 | 170 | 0.6168 | 0.6103 | +0.0066 | 11 | -0.220 | collecting |
| basketball | 227 | 170 | 0.6953 | 0.6966 | -0.0013 | 0 | +0.000 | collecting |
| football | 900300 | 158 | 0.6838 | 0.6577 | +0.0261 | 26 | -0.273 | collecting |
| basketball | 228 | 136 | 0.6720 | 0.6722 | -0.0001 | 0 | +0.000 | collecting |
| football | 139 | 42 | 0.6503 | 0.6908 | -0.0406 | 3 | +1.150 | collecting |
| football | 900301 | 36 | 0.4033 | 0.4216 | -0.0183 | 6 | +0.067 | collecting |
| basketball | 219 | 32 | 0.8024 | 0.8160 | -0.0136 | 0 | +0.000 | collecting |
| baseball | 258 | 10 | 0.6834 | 0.7034 | -0.0200 | 0 | +0.000 | collecting |
| baseball | 256 | 10 | 0.6382 | 0.5919 | +0.0462 | 0 | +0.000 | collecting |
| baseball | 251 | 10 | 0.6575 | 0.6529 | +0.0046 | 0 | +0.000 | collecting |

## Day 2 — 2026-10-12 22:44 UTC
Run: OK | snapshot 3467 outcomes / 60 events | failed steps: ['python3 sr_scores.py cache/board_2026-10-12.json']
Graded outcomes to date: 1746

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 688 | 0.6476 | 0.6439 | +0.0037 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 284 | 0.6944 | 0.6934 | +0.0009 | 5 | -0.440 | collecting |
| football | 166 | 170 | 0.6168 | 0.6103 | +0.0066 | 11 | -0.220 | collecting |
| basketball | 227 | 170 | 0.6953 | 0.6966 | -0.0013 | 0 | +0.000 | collecting |
| football | 900300 | 158 | 0.6838 | 0.6577 | +0.0261 | 26 | -0.273 | collecting |
| basketball | 228 | 136 | 0.6720 | 0.6722 | -0.0001 | 0 | +0.000 | collecting |
| football | 139 | 42 | 0.6503 | 0.6908 | -0.0406 | 3 | +1.150 | collecting |
| football | 900301 | 36 | 0.4033 | 0.4216 | -0.0183 | 6 | +0.067 | collecting |
| basketball | 219 | 32 | 0.8024 | 0.8160 | -0.0136 | 0 | +0.000 | collecting |
| baseball | 258 | 10 | 0.6834 | 0.7034 | -0.0200 | 0 | +0.000 | collecting |
| baseball | 256 | 10 | 0.6382 | 0.5919 | +0.0462 | 0 | +0.000 | collecting |
| baseball | 251 | 10 | 0.6575 | 0.6529 | +0.0046 | 0 | +0.000 | collecting |

## Day 3 — 2026-10-13 18:04 UTC
Run: OK | snapshot 3467 outcomes / 60 events | failed steps: ['python3 sr_scores.py cache/board_2026-10-12.json']
Graded outcomes to date: 2275

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 934 | 0.6370 | 0.6345 | +0.0025 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 404 | 0.6790 | 0.6825 | -0.0034 | 7 | +0.236 | **PASS** |
| basketball | 227 | 222 | 0.6923 | 0.6933 | -0.0010 | 0 | +0.000 | collecting |
| football | 166 | 186 | 0.6292 | 0.6132 | +0.0159 | 14 | -0.387 | collecting |
| basketball | 228 | 178 | 0.6763 | 0.6767 | -0.0004 | 0 | +0.000 | collecting |
| football | 900300 | 168 | 0.6710 | 0.6481 | +0.0228 | 26 | -0.273 | collecting |
| football | 139 | 48 | 0.6204 | 0.6922 | -0.0718 | 6 | +1.038 | collecting |
| basketball | 219 | 44 | 0.7091 | 0.7171 | -0.0079 | 0 | +0.000 | collecting |
| football | 900301 | 40 | 0.4025 | 0.4115 | -0.0090 | 7 | -0.086 | collecting |
| baseball | 258 | 20 | 0.6724 | 0.6927 | -0.0204 | 1 | +1.330 | collecting |
| baseball | 256 | 19 | 0.6153 | 0.5804 | +0.0348 | 0 | +0.000 | collecting |
| baseball | 251 | 12 | 0.7021 | 0.6998 | +0.0022 | 0 | +0.000 | collecting |

## Day 4 — 2026-10-14 00:39 UTC
Run: OK | snapshot 5446 outcomes / 101 events | failed steps: none
Graded outcomes to date: 4712

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 1920 | 0.6395 | 0.6374 | +0.0021 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 998 | 0.6355 | 0.6380 | -0.0025 | 15 | +0.324 | **PASS** |
| basketball | 227 | 448 | 0.6890 | 0.6892 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 364 | 0.6843 | 0.6841 | +0.0002 | 0 | +0.000 | FAIL (house better) |
| football | 900300 | 332 | 0.6551 | 0.6145 | +0.0406 | 62 | -0.072 | FAIL (house better) |
| football | 166 | 290 | 0.6431 | 0.6269 | +0.0163 | 27 | -0.346 | collecting |
| football | 139 | 122 | 0.6202 | 0.6551 | -0.0349 | 17 | +0.399 | collecting |
| football | 900301 | 106 | 0.6736 | 0.5608 | +0.1128 | 26 | -0.078 | collecting |
| basketball | 219 | 81 | 0.7089 | 0.7168 | -0.0079 | 0 | +0.000 | collecting |
| baseball | 258 | 20 | 0.6724 | 0.6927 | -0.0204 | 1 | +1.330 | collecting |
| baseball | 256 | 19 | 0.6153 | 0.5804 | +0.0348 | 0 | +0.000 | collecting |
| baseball | 251 | 12 | 0.7021 | 0.6998 | +0.0022 | 0 | +0.000 | collecting |

