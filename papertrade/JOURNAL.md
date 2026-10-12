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

