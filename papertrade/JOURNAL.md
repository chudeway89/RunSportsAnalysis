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

## Day 5 — 2026-10-14 15:46 UTC
Run: OK | snapshot 5446 outcomes / 101 events | failed steps: none
Graded outcomes to date: 5653

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 2348 | 0.6542 | 0.6524 | +0.0018 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 1178 | 0.6451 | 0.6479 | -0.0027 | 15 | +0.324 | **PASS** |
| basketball | 227 | 580 | 0.6882 | 0.6885 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 490 | 0.6882 | 0.6883 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 354 | 0.6637 | 0.6224 | +0.0412 | 69 | -0.057 | FAIL (house better) |
| football | 166 | 298 | 0.6484 | 0.6321 | +0.0163 | 27 | -0.346 | collecting |
| football | 139 | 122 | 0.6202 | 0.6551 | -0.0349 | 17 | +0.399 | collecting |
| football | 900301 | 112 | 0.6663 | 0.5677 | +0.0986 | 27 | -0.053 | collecting |
| basketball | 219 | 102 | 0.7279 | 0.7434 | -0.0154 | 0 | +0.000 | collecting |
| baseball | 258 | 26 | 0.6803 | 0.6999 | -0.0196 | 1 | +1.330 | collecting |
| baseball | 256 | 25 | 0.5977 | 0.5648 | +0.0329 | 0 | +0.000 | collecting |
| baseball | 251 | 18 | 0.6860 | 0.6838 | +0.0022 | 0 | +0.000 | collecting |

## Day 6 — 2026-10-15 00:09 UTC
Run: OK | snapshot 3094 outcomes / 72 events | failed steps: none
Graded outcomes to date: 8776

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 3738 | 0.6461 | 0.6450 | +0.0011 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 1988 | 0.6390 | 0.6395 | -0.0005 | 39 | +0.149 | **PASS** |
| basketball | 227 | 892 | 0.6857 | 0.6857 | +0.0000 | 0 | +0.000 | FAIL (house better) |
| basketball | 228 | 738 | 0.6880 | 0.6880 | -0.0000 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 468 | 0.6574 | 0.5982 | +0.0591 | 91 | -0.184 | FAIL (house better) |
| football | 166 | 394 | 0.6688 | 0.6516 | +0.0172 | 32 | -0.448 | FAIL (house better) |
| football | 139 | 197 | 0.6258 | 0.6306 | -0.0049 | 26 | +0.088 | collecting |
| basketball | 219 | 150 | 0.6979 | 0.7080 | -0.0101 | 0 | +0.000 | collecting |
| football | 900301 | 142 | 0.8186 | 0.6633 | +0.1554 | 34 | -0.171 | collecting |
| baseball | 258 | 26 | 0.6803 | 0.6999 | -0.0196 | 1 | +1.330 | collecting |
| baseball | 256 | 25 | 0.5977 | 0.5648 | +0.0329 | 0 | +0.000 | collecting |
| baseball | 251 | 18 | 0.6860 | 0.6838 | +0.0022 | 0 | +0.000 | collecting |

## Day 7 — 2026-10-15 15:33 UTC
Run: OK | snapshot 3094 outcomes / 72 events | failed steps: none
Graded outcomes to date: 9523

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 3856 | 0.6488 | 0.6475 | +0.0012 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 2038 | 0.6407 | 0.6406 | +0.0001 | 39 | +0.149 | FAIL (house better) |
| basketball | 227 | 938 | 0.6866 | 0.6867 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 770 | 0.6898 | 0.6900 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 652 | 0.6384 | 0.6011 | +0.0373 | 112 | -0.124 | FAIL (house better) |
| football | 166 | 568 | 0.6574 | 0.6510 | +0.0063 | 32 | -0.448 | FAIL (house better) |
| football | 139 | 245 | 0.6263 | 0.6196 | +0.0067 | 38 | -0.105 | collecting |
| football | 900301 | 194 | 0.7430 | 0.6315 | +0.1116 | 40 | -0.116 | collecting |
| basketball | 219 | 160 | 0.7154 | 0.7256 | -0.0102 | 0 | +0.000 | collecting |
| baseball | 258 | 40 | 0.6428 | 0.6563 | -0.0135 | 2 | +0.165 | collecting |
| baseball | 256 | 38 | 0.6141 | 0.5875 | +0.0266 | 0 | +0.000 | collecting |
| baseball | 251 | 24 | 0.7219 | 0.7223 | -0.0004 | 0 | +0.000 | collecting |

## Day 8 — 2026-10-15 23:56 UTC
Run: OK | snapshot 9088 outcomes / 199 events | failed steps: none
Graded outcomes to date: 11292

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 4308 | 0.6529 | 0.6518 | +0.0011 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 2262 | 0.6344 | 0.6344 | -0.0000 | 39 | +0.149 | **PASS** |
| basketball | 227 | 1078 | 0.6864 | 0.6865 | -0.0000 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 900 | 0.6453 | 0.5870 | +0.0582 | 162 | -0.196 | FAIL (house better) |
| basketball | 228 | 890 | 0.6902 | 0.6904 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 848 | 0.6602 | 0.6498 | +0.0103 | 50 | -0.450 | FAIL (house better) |
| football | 139 | 425 | 0.5931 | 0.5901 | +0.0030 | 78 | -0.032 | FAIL (house better) |
| football | 900301 | 285 | 0.7937 | 0.6594 | +0.1343 | 67 | -0.256 | collecting |
| basketball | 219 | 174 | 0.7238 | 0.7327 | -0.0089 | 0 | +0.000 | collecting |
| baseball | 258 | 50 | 0.6361 | 0.6455 | -0.0094 | 3 | -0.223 | collecting |
| baseball | 256 | 46 | 0.5715 | 0.5434 | +0.0282 | 0 | +0.000 | collecting |
| baseball | 251 | 26 | 0.7129 | 0.7130 | -0.0001 | 0 | +0.000 | collecting |

## Day 9 — 2026-10-16 15:19 UTC
Run: OK | snapshot 9088 outcomes / 199 events | failed steps: none
Graded outcomes to date: 12347

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 4832 | 0.6446 | 0.6436 | +0.0011 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 2474 | 0.6418 | 0.6416 | +0.0002 | 42 | +0.198 | FAIL (house better) |
| basketball | 227 | 1192 | 0.6867 | 0.6868 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 956 | 0.6914 | 0.6917 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 954 | 0.6419 | 0.5900 | +0.0519 | 176 | -0.171 | FAIL (house better) |
| football | 166 | 878 | 0.6567 | 0.6473 | +0.0095 | 51 | -0.425 | FAIL (house better) |
| football | 139 | 431 | 0.5908 | 0.5888 | +0.0020 | 81 | -0.028 | FAIL (house better) |
| football | 900301 | 299 | 0.7849 | 0.6565 | +0.1284 | 70 | -0.268 | collecting |
| basketball | 219 | 197 | 0.7221 | 0.7299 | -0.0078 | 0 | +0.000 | collecting |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 10 — 2026-10-17 00:03 UTC
Run: OK | snapshot 2224 outcomes / 103 events | failed steps: none
Graded outcomes to date: 15940

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 6514 | 0.6519 | 0.6509 | +0.0010 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 3223 | 0.6413 | 0.6414 | -0.0000 | 43 | +0.206 | **PASS** |
| basketball | 227 | 1690 | 0.6885 | 0.6884 | +0.0000 | 0 | +0.000 | FAIL (house better) |
| basketball | 228 | 1340 | 0.6911 | 0.6914 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 1046 | 0.6301 | 0.5895 | +0.0406 | 184 | -0.124 | FAIL (house better) |
| football | 166 | 942 | 0.6550 | 0.6477 | +0.0074 | 53 | -0.406 | FAIL (house better) |
| football | 139 | 431 | 0.5908 | 0.5888 | +0.0020 | 81 | -0.028 | FAIL (house better) |
| football | 900301 | 337 | 0.7757 | 0.6550 | +0.1208 | 73 | -0.279 | FAIL (house better) |
| basketball | 219 | 283 | 0.7043 | 0.7098 | -0.0055 | 0 | +0.000 | collecting |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 11 — 2026-10-17 14:08 UTC
Run: OK | snapshot 2224 outcomes / 103 events | failed steps: none
Graded outcomes to date: 16502

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 6524 | 0.6520 | 0.6510 | +0.0010 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 3229 | 0.6414 | 0.6414 | -0.0000 | 43 | +0.206 | **PASS** |
| basketball | 227 | 1700 | 0.6885 | 0.6885 | +0.0000 | 0 | +0.000 | FAIL (house better) |
| basketball | 228 | 1350 | 0.6914 | 0.6918 | -0.0004 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 1263 | 0.6459 | 0.6093 | +0.0365 | 224 | -0.152 | FAIL (house better) |
| football | 166 | 1152 | 0.6551 | 0.6506 | +0.0046 | 53 | -0.406 | FAIL (house better) |
| football | 139 | 463 | 0.5897 | 0.5881 | +0.0016 | 87 | -0.013 | FAIL (house better) |
| football | 900301 | 402 | 0.7751 | 0.6637 | +0.1114 | 84 | -0.297 | FAIL (house better) |
| basketball | 219 | 285 | 0.7063 | 0.7123 | -0.0060 | 0 | +0.000 | collecting |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 12 — 2026-10-17 23:30 UTC
Run: OK | snapshot 6344 outcomes / 135 events | failed steps: none
Graded outcomes to date: 17040

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 6524 | 0.6520 | 0.6510 | +0.0010 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 3229 | 0.6414 | 0.6414 | -0.0000 | 43 | +0.206 | **PASS** |
| basketball | 227 | 1700 | 0.6885 | 0.6885 | +0.0000 | 0 | +0.000 | FAIL (house better) |
| football | 900300 | 1545 | 0.6226 | 0.6035 | +0.0191 | 272 | -0.043 | FAIL (house better) |
| basketball | 228 | 1350 | 0.6914 | 0.6918 | -0.0004 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 1308 | 0.6563 | 0.6554 | +0.0009 | 60 | -0.297 | FAIL (house better) |
| football | 900301 | 494 | 0.7644 | 0.6761 | +0.0882 | 89 | -0.259 | FAIL (house better) |
| football | 139 | 471 | 0.5885 | 0.5892 | -0.0007 | 89 | +0.020 | **PASS** |
| basketball | 219 | 285 | 0.7063 | 0.7123 | -0.0060 | 0 | +0.000 | collecting |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 13 — 2026-10-18 14:25 UTC
Run: OK | snapshot 6344 outcomes / 135 events | failed steps: none
Graded outcomes to date: 19051

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 7040 | 0.6547 | 0.6538 | +0.0010 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 3537 | 0.6427 | 0.6426 | +0.0001 | 45 | +0.219 | FAIL (house better) |
| football | 900300 | 1978 | 0.6244 | 0.6137 | +0.0107 | 325 | +0.026 | FAIL (house better) |
| basketball | 227 | 1792 | 0.6892 | 0.6893 | -0.0000 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 1611 | 0.6582 | 0.6554 | +0.0028 | 66 | -0.332 | FAIL (house better) |
| basketball | 228 | 1420 | 0.6904 | 0.6907 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900301 | 621 | 0.7222 | 0.6549 | +0.0673 | 106 | -0.202 | FAIL (house better) |
| football | 139 | 618 | 0.5818 | 0.5864 | -0.0046 | 119 | +0.090 | **PASS** |
| basketball | 219 | 300 | 0.7022 | 0.7089 | -0.0067 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 14 — 2026-10-18 23:49 UTC
Run: OK | snapshot 3068 outcomes / 57 events | failed steps: none
Graded outcomes to date: 22724

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 8556 | 0.6491 | 0.6486 | +0.0005 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 4377 | 0.6458 | 0.6463 | -0.0005 | 49 | +0.156 | **PASS** |
| football | 900300 | 2312 | 0.6229 | 0.6117 | +0.0113 | 366 | -0.013 | FAIL (house better) |
| basketball | 227 | 2112 | 0.6878 | 0.6877 | +0.0001 | 0 | +0.000 | FAIL (house better) |
| football | 166 | 1863 | 0.6593 | 0.6552 | +0.0042 | 71 | -0.379 | FAIL (house better) |
| basketball | 228 | 1656 | 0.6899 | 0.6902 | -0.0004 | 0 | +0.000 | FAIL (picks lose) |
| football | 900301 | 738 | 0.7162 | 0.6549 | +0.0613 | 120 | -0.222 | FAIL (house better) |
| football | 139 | 622 | 0.5830 | 0.5880 | -0.0050 | 120 | +0.097 | **PASS** |
| basketball | 219 | 354 | 0.7002 | 0.7069 | -0.0066 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 15 — 2026-10-19 17:24 UTC
Run: OK | snapshot 3068 outcomes / 57 events | failed steps: none
Graded outcomes to date: 24258

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 9278 | 0.6447 | 0.6442 | +0.0005 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 4675 | 0.6464 | 0.6467 | -0.0002 | 52 | +0.146 | **PASS** |
| football | 900300 | 2426 | 0.6254 | 0.6152 | +0.0102 | 383 | -0.014 | FAIL (house better) |
| basketball | 227 | 2262 | 0.6885 | 0.6885 | +0.0000 | 0 | +0.000 | FAIL (house better) |
| football | 166 | 1925 | 0.6608 | 0.6560 | +0.0048 | 71 | -0.379 | FAIL (house better) |
| basketball | 228 | 1770 | 0.6903 | 0.6908 | -0.0005 | 0 | +0.000 | FAIL (picks lose) |
| football | 900301 | 766 | 0.7251 | 0.6626 | +0.0625 | 122 | -0.235 | FAIL (house better) |
| football | 139 | 642 | 0.5851 | 0.5852 | -0.0001 | 127 | +0.075 | **PASS** |
| basketball | 219 | 380 | 0.6898 | 0.6950 | -0.0052 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 16 — 2026-10-20 00:43 UTC
Run: OK | snapshot 4601 outcomes / 92 events | failed steps: none
Graded outcomes to date: 25221

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 9712 | 0.6472 | 0.6471 | +0.0002 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 4860 | 0.6450 | 0.6448 | +0.0002 | 52 | +0.146 | FAIL (house better) |
| football | 900300 | 2494 | 0.6237 | 0.6160 | +0.0077 | 398 | +0.010 | FAIL (house better) |
| basketball | 227 | 2372 | 0.6883 | 0.6883 | -0.0000 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 1993 | 0.6599 | 0.6562 | +0.0037 | 72 | -0.387 | FAIL (house better) |
| basketball | 228 | 1828 | 0.6893 | 0.6897 | -0.0004 | 0 | +0.000 | FAIL (picks lose) |
| football | 900301 | 786 | 0.7224 | 0.6577 | +0.0647 | 127 | -0.221 | FAIL (house better) |
| football | 139 | 642 | 0.5851 | 0.5852 | -0.0001 | 127 | +0.075 | **PASS** |
| basketball | 219 | 400 | 0.6886 | 0.6921 | -0.0035 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 54 | 0.6418 | 0.6462 | -0.0044 | 3 | -0.223 | collecting |
| baseball | 256 | 50 | 0.5787 | 0.5489 | +0.0298 | 0 | +0.000 | collecting |
| baseball | 251 | 30 | 0.7099 | 0.7107 | -0.0009 | 0 | +0.000 | collecting |

## Day 17 — 2026-10-20 15:37 UTC
Run: OK | snapshot 4601 outcomes / 92 events | failed steps: none
Graded outcomes to date: 26525

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 10342 | 0.6460 | 0.6458 | +0.0002 | 0 | +0.000 | FAIL (house better) |
| basketball | 223 | 5133 | 0.6473 | 0.6469 | +0.0004 | 53 | +0.124 | FAIL (house better) |
| football | 900300 | 2554 | 0.6248 | 0.6175 | +0.0073 | 402 | +0.019 | FAIL (house better) |
| basketball | 227 | 2526 | 0.6881 | 0.6882 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 2013 | 0.6593 | 0.6552 | +0.0041 | 72 | -0.387 | FAIL (house better) |
| basketball | 228 | 1934 | 0.6900 | 0.6905 | -0.0004 | 0 | +0.000 | FAIL (picks lose) |
| football | 900301 | 808 | 0.7209 | 0.6584 | +0.0625 | 129 | -0.205 | FAIL (house better) |
| football | 139 | 644 | 0.5849 | 0.5857 | -0.0007 | 128 | +0.082 | **PASS** |
| basketball | 219 | 425 | 0.6797 | 0.6826 | -0.0029 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 58 | 0.6465 | 0.6475 | -0.0009 | 3 | -0.223 | collecting |
| baseball | 256 | 54 | 0.5932 | 0.5666 | +0.0266 | 0 | +0.000 | collecting |
| baseball | 251 | 34 | 0.7159 | 0.7173 | -0.0014 | 0 | +0.000 | collecting |

## Day 18 — 2026-10-21 00:11 UTC
Run: OK | snapshot 7278 outcomes / 127 events | failed steps: none
Graded outcomes to date: 29016

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 11416 | 0.6505 | 0.6500 | +0.0005 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 5663 | 0.6475 | 0.6470 | +0.0005 | 68 | -0.005 | FAIL (house better) |
| basketball | 227 | 2816 | 0.6883 | 0.6884 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 2650 | 0.6221 | 0.6166 | +0.0055 | 428 | +0.022 | FAIL (house better) |
| basketball | 228 | 2144 | 0.6898 | 0.6901 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 2143 | 0.6577 | 0.6537 | +0.0039 | 72 | -0.387 | FAIL (house better) |
| football | 900301 | 846 | 0.7308 | 0.6626 | +0.0682 | 139 | -0.209 | FAIL (house better) |
| football | 139 | 719 | 0.5804 | 0.5889 | -0.0085 | 144 | +0.109 | **PASS** |
| basketball | 219 | 473 | 0.6697 | 0.6714 | -0.0017 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 58 | 0.6465 | 0.6475 | -0.0009 | 3 | -0.223 | collecting |
| baseball | 256 | 54 | 0.5932 | 0.5666 | +0.0266 | 0 | +0.000 | collecting |
| baseball | 251 | 34 | 0.7159 | 0.7173 | -0.0014 | 0 | +0.000 | collecting |

## Day 19 — 2026-10-21 15:55 UTC
Run: OK | snapshot 7278 outcomes / 127 events | failed steps: none
Graded outcomes to date: 30940

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 12206 | 0.6484 | 0.6480 | +0.0004 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 6032 | 0.6491 | 0.6485 | +0.0006 | 69 | -0.020 | FAIL (house better) |
| basketball | 227 | 2996 | 0.6886 | 0.6888 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 2829 | 0.6202 | 0.6148 | +0.0054 | 453 | +0.026 | FAIL (house better) |
| football | 166 | 2311 | 0.6552 | 0.6520 | +0.0031 | 72 | -0.387 | FAIL (house better) |
| basketball | 228 | 2286 | 0.6886 | 0.6888 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900301 | 902 | 0.7319 | 0.6699 | +0.0620 | 144 | -0.185 | FAIL (house better) |
| football | 139 | 719 | 0.5804 | 0.5889 | -0.0085 | 144 | +0.109 | **PASS** |
| basketball | 219 | 507 | 0.6614 | 0.6614 | +0.0000 | 0 | +0.000 | FAIL (house better) |
| baseball | 258 | 60 | 0.6474 | 0.6464 | +0.0011 | 3 | -0.223 | collecting |
| baseball | 256 | 56 | 0.5872 | 0.5613 | +0.0259 | 0 | +0.000 | collecting |
| baseball | 251 | 36 | 0.7123 | 0.7134 | -0.0011 | 0 | +0.000 | collecting |

## Day 20 — 2026-10-22 00:16 UTC
Run: OK | snapshot 5475 outcomes / 105 events | failed steps: none
Graded outcomes to date: 34221

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 13566 | 0.6468 | 0.6466 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 6767 | 0.6476 | 0.6470 | +0.0005 | 85 | +0.089 | FAIL (house better) |
| basketball | 227 | 3460 | 0.6887 | 0.6889 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 2917 | 0.6185 | 0.6135 | +0.0050 | 471 | +0.028 | FAIL (house better) |
| basketball | 228 | 2650 | 0.6889 | 0.6890 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 2401 | 0.6547 | 0.6517 | +0.0030 | 75 | -0.412 | FAIL (house better) |
| football | 900301 | 938 | 0.7269 | 0.6683 | +0.0586 | 155 | -0.141 | FAIL (house better) |
| football | 139 | 792 | 0.5815 | 0.5920 | -0.0105 | 155 | +0.103 | **PASS** |
| basketball | 219 | 578 | 0.6684 | 0.6708 | -0.0024 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 60 | 0.6474 | 0.6464 | +0.0011 | 3 | -0.223 | collecting |
| baseball | 256 | 56 | 0.5872 | 0.5613 | +0.0259 | 0 | +0.000 | collecting |
| baseball | 251 | 36 | 0.7123 | 0.7134 | -0.0011 | 0 | +0.000 | collecting |

## Day 21 — 2026-10-22 15:51 UTC
Run: OK | snapshot 5475 outcomes / 105 events | failed steps: none
Graded outcomes to date: 36926

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 14794 | 0.6415 | 0.6414 | +0.0001 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 7543 | 0.6516 | 0.6519 | -0.0004 | 87 | +0.096 | **PASS** |
| basketball | 227 | 3680 | 0.6884 | 0.6886 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 3029 | 0.6215 | 0.6151 | +0.0065 | 486 | +0.020 | FAIL (house better) |
| basketball | 228 | 2822 | 0.6890 | 0.6892 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 2481 | 0.6524 | 0.6503 | +0.0022 | 79 | -0.333 | FAIL (house better) |
| football | 900301 | 972 | 0.7220 | 0.6663 | +0.0557 | 157 | -0.127 | FAIL (house better) |
| football | 139 | 826 | 0.5871 | 0.5983 | -0.0112 | 170 | +0.109 | **PASS** |
| basketball | 219 | 627 | 0.6655 | 0.6676 | -0.0021 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 60 | 0.6474 | 0.6464 | +0.0011 | 3 | -0.223 | collecting |
| baseball | 256 | 56 | 0.5872 | 0.5613 | +0.0259 | 0 | +0.000 | collecting |
| baseball | 251 | 36 | 0.7123 | 0.7134 | -0.0011 | 0 | +0.000 | collecting |

## Day 22 — 2026-10-23 00:14 UTC
Run: OK | snapshot 8164 outcomes / 181 events | failed steps: none
Graded outcomes to date: 39671

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 15626 | 0.6393 | 0.6391 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 8002 | 0.6528 | 0.6536 | -0.0008 | 94 | +0.121 | **PASS** |
| basketball | 227 | 3910 | 0.6886 | 0.6888 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 3370 | 0.6244 | 0.6129 | +0.0115 | 555 | -0.020 | FAIL (house better) |
| basketball | 228 | 2986 | 0.6891 | 0.6893 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 2861 | 0.6485 | 0.6487 | -0.0002 | 119 | -0.178 | FAIL (picks lose) |
| football | 900301 | 1085 | 0.7076 | 0.6532 | +0.0544 | 190 | -0.116 | FAIL (house better) |
| football | 139 | 1014 | 0.5874 | 0.5896 | -0.0021 | 188 | +0.041 | **PASS** |
| basketball | 219 | 665 | 0.6705 | 0.6748 | -0.0043 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 60 | 0.6474 | 0.6464 | +0.0011 | 3 | -0.223 | collecting |
| baseball | 256 | 56 | 0.5872 | 0.5613 | +0.0259 | 0 | +0.000 | collecting |
| baseball | 251 | 36 | 0.7123 | 0.7134 | -0.0011 | 0 | +0.000 | collecting |

## Day 23 — 2026-10-23 15:42 UTC
Run: OK | snapshot 8164 outcomes / 181 events | failed steps: none
Graded outcomes to date: 41652

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 16656 | 0.6387 | 0.6383 | +0.0004 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 8469 | 0.6511 | 0.6518 | -0.0008 | 95 | +0.109 | **PASS** |
| basketball | 227 | 4124 | 0.6883 | 0.6884 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 3404 | 0.6230 | 0.6119 | +0.0111 | 567 | -0.021 | FAIL (house better) |
| basketball | 228 | 3144 | 0.6894 | 0.6896 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 2879 | 0.6488 | 0.6487 | +0.0001 | 119 | -0.178 | FAIL (house better) |
| football | 900301 | 1099 | 0.7069 | 0.6534 | +0.0535 | 195 | -0.118 | FAIL (house better) |
| football | 139 | 1022 | 0.5869 | 0.5893 | -0.0024 | 192 | +0.036 | **PASS** |
| basketball | 219 | 703 | 0.6663 | 0.6704 | -0.0042 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 60 | 0.6474 | 0.6464 | +0.0011 | 3 | -0.223 | collecting |
| baseball | 256 | 56 | 0.5872 | 0.5613 | +0.0259 | 0 | +0.000 | collecting |
| baseball | 251 | 36 | 0.7123 | 0.7134 | -0.0011 | 0 | +0.000 | collecting |

## Day 24 — 2026-10-24 00:07 UTC
Run: OK | snapshot 8164 outcomes / 181 events | failed steps: none
Graded outcomes to date: 45000

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 18144 | 0.6423 | 0.6418 | +0.0005 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 9137 | 0.6500 | 0.6507 | -0.0007 | 97 | +0.114 | **PASS** |
| basketball | 227 | 4606 | 0.6889 | 0.6891 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 3544 | 0.6187 | 0.6138 | +0.0049 | 600 | +0.019 | FAIL (house better) |
| basketball | 228 | 3476 | 0.6890 | 0.6892 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 2985 | 0.6466 | 0.6465 | +0.0000 | 119 | -0.178 | FAIL (house better) |
| football | 900301 | 1147 | 0.7074 | 0.6608 | +0.0466 | 200 | -0.095 | FAIL (house better) |
| football | 139 | 1022 | 0.5869 | 0.5893 | -0.0024 | 192 | +0.036 | **PASS** |
| basketball | 219 | 787 | 0.6584 | 0.6616 | -0.0032 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 60 | 0.6474 | 0.6464 | +0.0011 | 3 | -0.223 | collecting |
| baseball | 256 | 56 | 0.5872 | 0.5613 | +0.0259 | 0 | +0.000 | collecting |
| baseball | 251 | 36 | 0.7123 | 0.7134 | -0.0011 | 0 | +0.000 | collecting |

## Day 25 — 2026-10-24 14:25 UTC
Run: OK | snapshot 8164 outcomes / 181 events | failed steps: none
Graded outcomes to date: 46769

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 18802 | 0.6439 | 0.6436 | +0.0004 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 9635 | 0.6504 | 0.6512 | -0.0008 | 98 | +0.103 | **PASS** |
| basketball | 227 | 4716 | 0.6888 | 0.6891 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 3776 | 0.6182 | 0.6141 | +0.0041 | 644 | +0.032 | FAIL (house better) |
| basketball | 228 | 3570 | 0.6893 | 0.6895 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3051 | 0.6484 | 0.6482 | +0.0002 | 126 | -0.148 | FAIL (house better) |
| football | 900301 | 1201 | 0.7001 | 0.6574 | +0.0427 | 207 | -0.072 | FAIL (house better) |
| football | 139 | 1026 | 0.5867 | 0.5899 | -0.0032 | 194 | +0.045 | **PASS** |
| basketball | 219 | 819 | 0.6556 | 0.6584 | -0.0029 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 70 | 0.6420 | 0.6323 | +0.0097 | 4 | -0.417 | collecting |
| baseball | 256 | 65 | 0.5609 | 0.5324 | +0.0285 | 0 | +0.000 | collecting |
| baseball | 251 | 38 | 0.6990 | 0.6997 | -0.0006 | 0 | +0.000 | collecting |

## Day 26 — 2026-10-24 23:48 UTC
Run: OK | snapshot 1803 outcomes / 82 events | failed steps: none
Graded outcomes to date: 46769

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 18802 | 0.6439 | 0.6436 | +0.0004 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 9635 | 0.6504 | 0.6512 | -0.0008 | 98 | +0.103 | **PASS** |
| basketball | 227 | 4716 | 0.6888 | 0.6891 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 3776 | 0.6182 | 0.6141 | +0.0041 | 644 | +0.032 | FAIL (house better) |
| basketball | 228 | 3570 | 0.6893 | 0.6895 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3051 | 0.6484 | 0.6482 | +0.0002 | 126 | -0.148 | FAIL (house better) |
| football | 900301 | 1201 | 0.7001 | 0.6574 | +0.0427 | 207 | -0.072 | FAIL (house better) |
| football | 139 | 1026 | 0.5867 | 0.5899 | -0.0032 | 194 | +0.045 | **PASS** |
| basketball | 219 | 819 | 0.6556 | 0.6584 | -0.0029 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 70 | 0.6420 | 0.6323 | +0.0097 | 4 | -0.417 | collecting |
| baseball | 256 | 65 | 0.5609 | 0.5324 | +0.0285 | 0 | +0.000 | collecting |
| baseball | 251 | 38 | 0.6990 | 0.6997 | -0.0006 | 0 | +0.000 | collecting |

## Day 27 — 2026-10-25 14:57 UTC
Run: OK | snapshot 1803 outcomes / 82 events | failed steps: none
Graded outcomes to date: 47303

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 18802 | 0.6439 | 0.6436 | +0.0004 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 9635 | 0.6504 | 0.6512 | -0.0008 | 98 | +0.103 | **PASS** |
| basketball | 227 | 4716 | 0.6888 | 0.6891 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 3988 | 0.6171 | 0.6135 | +0.0036 | 680 | +0.037 | FAIL (house better) |
| basketball | 228 | 3570 | 0.6893 | 0.6895 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3235 | 0.6466 | 0.6456 | +0.0010 | 129 | -0.156 | FAIL (house better) |
| football | 900301 | 1261 | 0.6977 | 0.6569 | +0.0408 | 214 | -0.055 | FAIL (house better) |
| football | 139 | 1104 | 0.5933 | 0.5934 | -0.0001 | 203 | +0.024 | **PASS** |
| basketball | 219 | 819 | 0.6556 | 0.6584 | -0.0029 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 70 | 0.6420 | 0.6323 | +0.0097 | 4 | -0.417 | collecting |
| baseball | 256 | 65 | 0.5609 | 0.5324 | +0.0285 | 0 | +0.000 | collecting |
| baseball | 251 | 38 | 0.6990 | 0.6997 | -0.0006 | 0 | +0.000 | collecting |

## Day 28 — 2026-10-25 23:36 UTC
Run: OK | snapshot 4082 outcomes / 68 events | failed steps: none
Graded outcomes to date: 47911

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 18802 | 0.6439 | 0.6436 | +0.0004 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 9635 | 0.6504 | 0.6512 | -0.0008 | 98 | +0.103 | **PASS** |
| basketball | 227 | 4716 | 0.6888 | 0.6891 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4310 | 0.6142 | 0.6141 | +0.0001 | 744 | +0.056 | FAIL (house better) |
| basketball | 228 | 3570 | 0.6893 | 0.6895 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3421 | 0.6477 | 0.6466 | +0.0011 | 138 | -0.127 | FAIL (house better) |
| football | 900301 | 1361 | 0.6927 | 0.6555 | +0.0372 | 223 | -0.039 | FAIL (house better) |
| football | 139 | 1104 | 0.5933 | 0.5934 | -0.0001 | 203 | +0.024 | **PASS** |
| basketball | 219 | 819 | 0.6556 | 0.6584 | -0.0029 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 70 | 0.6420 | 0.6323 | +0.0097 | 4 | -0.417 | collecting |
| baseball | 256 | 65 | 0.5609 | 0.5324 | +0.0285 | 0 | +0.000 | collecting |
| baseball | 251 | 38 | 0.6990 | 0.6997 | -0.0006 | 0 | +0.000 | collecting |

## Day 29 — 2026-10-26 17:14 UTC
Run: OK | snapshot 4082 outcomes / 68 events | failed steps: none
Graded outcomes to date: 49488

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 19504 | 0.6444 | 0.6439 | +0.0005 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 9926 | 0.6503 | 0.6512 | -0.0009 | 99 | +0.120 | **PASS** |
| basketball | 227 | 4846 | 0.6890 | 0.6892 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4462 | 0.6158 | 0.6154 | +0.0004 | 763 | +0.056 | FAIL (house better) |
| basketball | 228 | 3674 | 0.6880 | 0.6880 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3497 | 0.6487 | 0.6469 | +0.0017 | 139 | -0.133 | FAIL (house better) |
| football | 900301 | 1429 | 0.6933 | 0.6565 | +0.0369 | 234 | -0.061 | FAIL (house better) |
| football | 139 | 1134 | 0.5922 | 0.5978 | -0.0057 | 217 | +0.044 | **PASS** |
| basketball | 219 | 837 | 0.6568 | 0.6601 | -0.0033 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 72 | 0.6425 | 0.6337 | +0.0089 | 4 | -0.417 | collecting |
| baseball | 256 | 67 | 0.5712 | 0.5393 | +0.0319 | 0 | +0.000 | collecting |
| baseball | 251 | 40 | 0.6924 | 0.6924 | +0.0000 | 0 | +0.000 | collecting |

## Day 30 — 2026-10-27 00:52 UTC
Run: OK | snapshot 4886 outcomes / 68 events | failed steps: none
Graded outcomes to date: 50796

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 20156 | 0.6451 | 0.6446 | +0.0005 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 10192 | 0.6500 | 0.6507 | -0.0008 | 105 | +0.186 | **PASS** |
| basketball | 227 | 5006 | 0.6894 | 0.6897 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4502 | 0.6163 | 0.6164 | -0.0001 | 767 | +0.058 | **PASS** |
| basketball | 228 | 3802 | 0.6876 | 0.6876 | -0.0000 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3513 | 0.6493 | 0.6473 | +0.0020 | 139 | -0.133 | FAIL (house better) |
| football | 900301 | 1445 | 0.6924 | 0.6557 | +0.0368 | 235 | -0.065 | FAIL (house better) |
| football | 139 | 1134 | 0.5922 | 0.5978 | -0.0057 | 217 | +0.044 | **PASS** |
| basketball | 219 | 867 | 0.6531 | 0.6558 | -0.0027 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 72 | 0.6425 | 0.6337 | +0.0089 | 4 | -0.417 | collecting |
| baseball | 256 | 67 | 0.5712 | 0.5393 | +0.0319 | 0 | +0.000 | collecting |
| baseball | 251 | 40 | 0.6924 | 0.6924 | +0.0000 | 0 | +0.000 | collecting |

## Day 31 — 2026-10-27 16:20 UTC
Run: OK | snapshot 4886 outcomes / 68 events | failed steps: none
Graded outcomes to date: 52597

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 21006 | 0.6450 | 0.6446 | +0.0004 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 10650 | 0.6501 | 0.6507 | -0.0006 | 105 | +0.186 | **PASS** |
| basketball | 227 | 5176 | 0.6894 | 0.6897 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4560 | 0.6166 | 0.6171 | -0.0005 | 774 | +0.064 | **PASS** |
| basketball | 228 | 3938 | 0.6881 | 0.6881 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3559 | 0.6502 | 0.6485 | +0.0018 | 139 | -0.133 | FAIL (house better) |
| football | 900301 | 1467 | 0.6930 | 0.6559 | +0.0371 | 238 | -0.077 | FAIL (house better) |
| football | 139 | 1138 | 0.5912 | 0.5981 | -0.0069 | 219 | +0.051 | **PASS** |
| basketball | 219 | 898 | 0.6540 | 0.6568 | -0.0028 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 84 | 0.6476 | 0.6529 | -0.0052 | 6 | +0.157 | collecting |
| baseball | 256 | 77 | 0.5958 | 0.5688 | +0.0269 | 0 | +0.000 | collecting |
| baseball | 251 | 44 | 0.7067 | 0.7081 | -0.0014 | 0 | +0.000 | collecting |

## Day 32 — 2026-10-28 00:49 UTC
Run: OK | snapshot 7273 outcomes / 115 events | failed steps: none
Graded outcomes to date: 55544

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 22460 | 0.6452 | 0.6449 | +0.0003 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 11478 | 0.6486 | 0.6488 | -0.0002 | 137 | +0.100 | **PASS** |
| basketball | 227 | 5502 | 0.6890 | 0.6893 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4586 | 0.6167 | 0.6177 | -0.0010 | 781 | +0.064 | **PASS** |
| basketball | 228 | 4182 | 0.6881 | 0.6881 | -0.0000 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3571 | 0.6504 | 0.6485 | +0.0019 | 139 | -0.133 | FAIL (house better) |
| football | 900301 | 1471 | 0.6947 | 0.6578 | +0.0369 | 239 | -0.070 | FAIL (house better) |
| football | 139 | 1138 | 0.5912 | 0.5981 | -0.0069 | 219 | +0.051 | **PASS** |
| basketball | 219 | 951 | 0.6590 | 0.6633 | -0.0043 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 84 | 0.6476 | 0.6529 | -0.0052 | 6 | +0.157 | collecting |
| baseball | 256 | 77 | 0.5958 | 0.5688 | +0.0269 | 0 | +0.000 | collecting |
| baseball | 251 | 44 | 0.7067 | 0.7081 | -0.0014 | 0 | +0.000 | collecting |

## Day 33 — 2026-10-28 17:05 UTC
Run: OK | snapshot 7273 outcomes / 115 events | failed steps: none
Graded outcomes to date: 56841

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 23132 | 0.6460 | 0.6457 | +0.0003 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 11773 | 0.6484 | 0.6487 | -0.0004 | 140 | +0.077 | **PASS** |
| basketball | 227 | 5652 | 0.6891 | 0.6894 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4610 | 0.6172 | 0.6190 | -0.0017 | 791 | +0.068 | **PASS** |
| basketball | 228 | 4286 | 0.6882 | 0.6883 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3593 | 0.6506 | 0.6486 | +0.0021 | 139 | -0.133 | FAIL (house better) |
| football | 900301 | 1473 | 0.6947 | 0.6575 | +0.0372 | 240 | -0.074 | FAIL (house better) |
| football | 139 | 1138 | 0.5912 | 0.5981 | -0.0069 | 219 | +0.051 | **PASS** |
| basketball | 219 | 973 | 0.6575 | 0.6621 | -0.0045 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 86 | 0.6478 | 0.6539 | -0.0061 | 6 | +0.157 | collecting |
| baseball | 256 | 79 | 0.5997 | 0.5746 | +0.0251 | 0 | +0.000 | collecting |
| baseball | 251 | 46 | 0.6949 | 0.6953 | -0.0004 | 0 | +0.000 | collecting |

## Day 34 — 2026-10-29 01:17 UTC
Run: OK | snapshot 3763 outcomes / 76 events | failed steps: none
Graded outcomes to date: 60008

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 24604 | 0.6454 | 0.6452 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 12640 | 0.6486 | 0.6488 | -0.0002 | 173 | +0.100 | **PASS** |
| basketball | 227 | 5958 | 0.6889 | 0.6892 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4713 | 0.6171 | 0.6189 | -0.0018 | 804 | +0.067 | **PASS** |
| basketball | 228 | 4484 | 0.6881 | 0.6882 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3691 | 0.6499 | 0.6475 | +0.0024 | 144 | -0.117 | FAIL (house better) |
| football | 900301 | 1503 | 0.6951 | 0.6577 | +0.0375 | 245 | -0.074 | FAIL (house better) |
| football | 139 | 1176 | 0.5914 | 0.5949 | -0.0034 | 233 | +0.041 | **PASS** |
| basketball | 219 | 1028 | 0.6598 | 0.6653 | -0.0055 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 86 | 0.6478 | 0.6539 | -0.0061 | 6 | +0.157 | collecting |
| baseball | 256 | 79 | 0.5997 | 0.5746 | +0.0251 | 0 | +0.000 | collecting |
| baseball | 251 | 46 | 0.6949 | 0.6953 | -0.0004 | 0 | +0.000 | collecting |

## Day 35 — 2026-10-29 17:23 UTC
Run: OK | snapshot 3763 outcomes / 76 events | failed steps: none
Graded outcomes to date: 62602

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 25580 | 0.6454 | 0.6452 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 13271 | 0.6483 | 0.6485 | -0.0002 | 173 | +0.100 | **PASS** |
| basketball | 227 | 6170 | 0.6887 | 0.6890 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 4945 | 0.6212 | 0.6203 | +0.0009 | 834 | +0.046 | FAIL (house better) |
| basketball | 228 | 4668 | 0.6882 | 0.6883 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3893 | 0.6485 | 0.6459 | +0.0026 | 149 | -0.108 | FAIL (house better) |
| football | 900301 | 1575 | 0.6882 | 0.6524 | +0.0359 | 251 | -0.072 | FAIL (house better) |
| football | 139 | 1211 | 0.5963 | 0.5973 | -0.0010 | 241 | +0.037 | **PASS** |
| basketball | 219 | 1072 | 0.6528 | 0.6577 | -0.0050 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 88 | 0.6492 | 0.6529 | -0.0037 | 6 | +0.157 | collecting |
| baseball | 256 | 81 | 0.5965 | 0.5716 | +0.0248 | 0 | +0.000 | collecting |
| baseball | 251 | 48 | 0.6971 | 0.6978 | -0.0007 | 0 | +0.000 | collecting |

## Day 36 — 2026-10-30 01:26 UTC
Run: OK | snapshot 9082 outcomes / 170 events | failed steps: none
Graded outcomes to date: 63894

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 26144 | 0.6448 | 0.6446 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 13563 | 0.6493 | 0.6494 | -0.0001 | 177 | +0.123 | **PASS** |
| basketball | 227 | 6310 | 0.6886 | 0.6889 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 5001 | 0.6205 | 0.6197 | +0.0007 | 837 | +0.050 | FAIL (house better) |
| basketball | 228 | 4786 | 0.6882 | 0.6884 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 3971 | 0.6482 | 0.6461 | +0.0021 | 149 | -0.108 | FAIL (house better) |
| football | 900301 | 1591 | 0.6859 | 0.6501 | +0.0358 | 251 | -0.072 | FAIL (house better) |
| football | 139 | 1219 | 0.6012 | 0.5986 | +0.0026 | 244 | +0.024 | FAIL (house better) |
| basketball | 219 | 1092 | 0.6514 | 0.6566 | -0.0053 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 88 | 0.6492 | 0.6529 | -0.0037 | 6 | +0.157 | collecting |
| baseball | 256 | 81 | 0.5965 | 0.5716 | +0.0248 | 0 | +0.000 | collecting |
| baseball | 251 | 48 | 0.6971 | 0.6978 | -0.0007 | 0 | +0.000 | collecting |

## Day 37 — 2026-10-30 17:01 UTC
Run: OK | snapshot 9082 outcomes / 170 events | failed steps: none
Graded outcomes to date: 66061

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 27230 | 0.6451 | 0.6448 | +0.0003 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 14059 | 0.6488 | 0.6488 | +0.0000 | 179 | +0.111 | FAIL (house better) |
| basketball | 227 | 6524 | 0.6885 | 0.6888 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 5075 | 0.6194 | 0.6199 | -0.0005 | 847 | +0.060 | **PASS** |
| basketball | 228 | 4950 | 0.6878 | 0.6879 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 166 | 4025 | 0.6473 | 0.6454 | +0.0020 | 149 | -0.108 | FAIL (house better) |
| football | 900301 | 1618 | 0.6839 | 0.6486 | +0.0353 | 252 | -0.070 | FAIL (house better) |
| football | 139 | 1231 | 0.6027 | 0.5990 | +0.0037 | 247 | +0.020 | FAIL (house better) |
| basketball | 219 | 1126 | 0.6516 | 0.6568 | -0.0052 | 0 | +0.000 | FAIL (picks lose) |
| baseball | 258 | 90 | 0.6502 | 0.6537 | -0.0034 | 6 | +0.157 | collecting |
| baseball | 256 | 83 | 0.6049 | 0.5816 | +0.0234 | 0 | +0.000 | collecting |
| baseball | 251 | 50 | 0.6935 | 0.6938 | -0.0003 | 0 | +0.000 | collecting |

## Day 38 — 2026-10-31 01:09 UTC
Run: OK | snapshot 12985 outcomes / 237 events | failed steps: none
Graded outcomes to date: 69702

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 28864 | 0.6443 | 0.6441 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 14851 | 0.6487 | 0.6487 | -0.0000 | 187 | +0.094 | **PASS** |
| basketball | 227 | 7030 | 0.6885 | 0.6887 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 5336 | 0.6878 | 0.6880 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 5193 | 0.6211 | 0.6215 | -0.0004 | 864 | +0.059 | **PASS** |
| football | 166 | 4095 | 0.6484 | 0.6467 | +0.0017 | 150 | -0.101 | FAIL (house better) |
| football | 900301 | 1670 | 0.6774 | 0.6459 | +0.0315 | 259 | -0.057 | FAIL (house better) |
| football | 139 | 1231 | 0.6027 | 0.5990 | +0.0037 | 247 | +0.020 | FAIL (house better) |
| basketball | 219 | 1209 | 0.6514 | 0.6563 | -0.0049 | 1 | -1.000 | FAIL (picks lose) |
| baseball | 258 | 90 | 0.6502 | 0.6537 | -0.0034 | 6 | +0.157 | collecting |
| baseball | 256 | 83 | 0.6049 | 0.5816 | +0.0234 | 0 | +0.000 | collecting |
| baseball | 251 | 50 | 0.6935 | 0.6938 | -0.0003 | 0 | +0.000 | collecting |

## Day 39 — 2026-10-31 16:02 UTC
Run: OK | snapshot 12985 outcomes / 237 events | failed steps: none
Graded outcomes to date: 73778

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 30756 | 0.6441 | 0.6439 | +0.0001 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 15913 | 0.6476 | 0.6473 | +0.0004 | 190 | +0.099 | FAIL (house better) |
| basketball | 227 | 7366 | 0.6881 | 0.6884 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 5588 | 0.6877 | 0.6879 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 5421 | 0.6256 | 0.6251 | +0.0005 | 894 | +0.053 | FAIL (house better) |
| football | 166 | 4243 | 0.6482 | 0.6466 | +0.0016 | 153 | -0.118 | FAIL (house better) |
| football | 900301 | 1737 | 0.6734 | 0.6427 | +0.0307 | 265 | -0.054 | FAIL (house better) |
| basketball | 219 | 1274 | 0.6530 | 0.6576 | -0.0047 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1257 | 0.6033 | 0.6008 | +0.0025 | 250 | +0.033 | FAIL (house better) |
| baseball | 258 | 90 | 0.6502 | 0.6537 | -0.0034 | 6 | +0.157 | collecting |
| baseball | 256 | 83 | 0.6049 | 0.5816 | +0.0234 | 0 | +0.000 | collecting |
| baseball | 251 | 50 | 0.6935 | 0.6938 | -0.0003 | 0 | +0.000 | collecting |

## Day 40 — 2026-11-01 00:32 UTC
Run: OK | snapshot 12275 outcomes / 233 events | failed steps: none
Graded outcomes to date: 80577

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 33880 | 0.6449 | 0.6448 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 17426 | 0.6500 | 0.6500 | -0.0000 | 212 | +0.130 | **PASS** |
| basketball | 227 | 8158 | 0.6886 | 0.6889 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 6202 | 0.6876 | 0.6877 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 5740 | 0.6268 | 0.6278 | -0.0011 | 934 | +0.053 | **PASS** |
| football | 166 | 4459 | 0.6498 | 0.6491 | +0.0007 | 160 | -0.105 | FAIL (house better) |
| football | 900301 | 1830 | 0.6675 | 0.6404 | +0.0271 | 277 | -0.045 | FAIL (house better) |
| basketball | 219 | 1400 | 0.6564 | 0.6603 | -0.0039 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1259 | 0.6033 | 0.6011 | +0.0022 | 251 | +0.037 | FAIL (house better) |
| baseball | 258 | 90 | 0.6502 | 0.6537 | -0.0034 | 6 | +0.157 | collecting |
| baseball | 256 | 83 | 0.6049 | 0.5816 | +0.0234 | 0 | +0.000 | collecting |
| baseball | 251 | 50 | 0.6935 | 0.6938 | -0.0003 | 0 | +0.000 | collecting |

## Day 41 — 2026-11-01 17:07 UTC
Run: OK | snapshot 12275 outcomes / 233 events | failed steps: none
Graded outcomes to date: 85835

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 36276 | 0.6441 | 0.6440 | +0.0001 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 18629 | 0.6520 | 0.6515 | +0.0005 | 215 | +0.128 | FAIL (house better) |
| basketball | 227 | 8686 | 0.6887 | 0.6890 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 6604 | 0.6872 | 0.6873 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6064 | 0.6236 | 0.6273 | -0.0037 | 991 | +0.063 | **PASS** |
| football | 166 | 4657 | 0.6488 | 0.6483 | +0.0005 | 165 | -0.121 | FAIL (house better) |
| football | 900301 | 1917 | 0.6661 | 0.6403 | +0.0257 | 294 | -0.025 | FAIL (house better) |
| basketball | 219 | 1478 | 0.6632 | 0.6672 | -0.0040 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1295 | 0.6061 | 0.6025 | +0.0036 | 263 | +0.025 | FAIL (house better) |
| baseball | 258 | 92 | 0.6512 | 0.6555 | -0.0043 | 6 | +0.157 | collecting |
| baseball | 256 | 85 | 0.6014 | 0.5794 | +0.0220 | 0 | +0.000 | collecting |
| baseball | 251 | 52 | 0.6947 | 0.6951 | -0.0004 | 0 | +0.000 | collecting |

## Day 42 — 2026-11-02 01:07 UTC
Run: OK | snapshot 9803 outcomes / 191 events | failed steps: none
Graded outcomes to date: 90972

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 38592 | 0.6461 | 0.6458 | +0.0003 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 19664 | 0.6524 | 0.6521 | +0.0002 | 225 | +0.129 | FAIL (house better) |
| basketball | 227 | 9348 | 0.6885 | 0.6888 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 7030 | 0.6874 | 0.6875 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6330 | 0.6247 | 0.6274 | -0.0027 | 1034 | +0.056 | **PASS** |
| football | 166 | 4855 | 0.6491 | 0.6487 | +0.0004 | 172 | -0.135 | FAIL (house better) |
| football | 900301 | 2004 | 0.6635 | 0.6403 | +0.0232 | 306 | -0.009 | FAIL (house better) |
| basketball | 219 | 1599 | 0.6622 | 0.6655 | -0.0034 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1321 | 0.6076 | 0.6051 | +0.0025 | 265 | +0.025 | FAIL (house better) |
| baseball | 258 | 92 | 0.6512 | 0.6555 | -0.0043 | 6 | +0.157 | collecting |
| baseball | 256 | 85 | 0.6014 | 0.5794 | +0.0220 | 0 | +0.000 | collecting |
| baseball | 251 | 52 | 0.6947 | 0.6951 | -0.0004 | 0 | +0.000 | collecting |

## Day 43 — 2026-11-02 20:44 UTC
Run: OK | snapshot 9803 outcomes / 191 events | failed steps: none
Graded outcomes to date: 93185

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 39628 | 0.6460 | 0.6457 | +0.0003 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 20134 | 0.6513 | 0.6511 | +0.0001 | 225 | +0.129 | FAIL (house better) |
| basketball | 227 | 9588 | 0.6886 | 0.6890 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 7212 | 0.6873 | 0.6874 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6446 | 0.6252 | 0.6278 | -0.0026 | 1040 | +0.054 | **PASS** |
| football | 166 | 4919 | 0.6497 | 0.6490 | +0.0007 | 172 | -0.135 | FAIL (house better) |
| football | 900301 | 2042 | 0.6616 | 0.6374 | +0.0241 | 310 | -0.018 | FAIL (house better) |
| basketball | 219 | 1637 | 0.6613 | 0.6649 | -0.0036 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1350 | 0.6058 | 0.6033 | +0.0026 | 271 | +0.027 | FAIL (house better) |
| baseball | 258 | 92 | 0.6512 | 0.6555 | -0.0043 | 6 | +0.157 | collecting |
| baseball | 256 | 85 | 0.6014 | 0.5794 | +0.0220 | 0 | +0.000 | collecting |
| baseball | 251 | 52 | 0.6947 | 0.6951 | -0.0004 | 0 | +0.000 | collecting |

## Day 44 — 2026-11-03 03:09 UTC
Run: OK | snapshot 5431 outcomes / 83 events | failed steps: none
Graded outcomes to date: 96617

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 41452 | 0.6471 | 0.6469 | +0.0003 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 20847 | 0.6513 | 0.6512 | +0.0001 | 225 | +0.129 | FAIL (house better) |
| basketball | 227 | 9902 | 0.6885 | 0.6888 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 7474 | 0.6877 | 0.6878 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6588 | 0.6264 | 0.6274 | -0.0010 | 1065 | +0.055 | **PASS** |
| football | 166 | 4999 | 0.6501 | 0.6489 | +0.0012 | 181 | -0.159 | FAIL (house better) |
| football | 900301 | 2082 | 0.6566 | 0.6327 | +0.0240 | 316 | -0.012 | FAIL (house better) |
| basketball | 219 | 1692 | 0.6633 | 0.6671 | -0.0038 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1352 | 0.6056 | 0.6033 | +0.0023 | 272 | +0.029 | FAIL (house better) |
| baseball | 258 | 92 | 0.6512 | 0.6555 | -0.0043 | 6 | +0.157 | collecting |
| baseball | 256 | 85 | 0.6014 | 0.5794 | +0.0220 | 0 | +0.000 | collecting |
| baseball | 251 | 52 | 0.6947 | 0.6951 | -0.0004 | 0 | +0.000 | collecting |

## Day 45 — 2026-11-03 18:22 UTC
Run: OK | snapshot 5431 outcomes / 83 events | failed steps: none
Graded outcomes to date: 101201

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 43698 | 0.6487 | 0.6485 | +0.0002 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 21925 | 0.6505 | 0.6503 | +0.0002 | 226 | +0.124 | FAIL (house better) |
| basketball | 227 | 10516 | 0.6884 | 0.6887 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 8006 | 0.6874 | 0.6876 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6612 | 0.6264 | 0.6275 | -0.0010 | 1065 | +0.055 | **PASS** |
| football | 166 | 5003 | 0.6500 | 0.6489 | +0.0011 | 181 | -0.159 | FAIL (house better) |
| football | 900301 | 2090 | 0.6552 | 0.6314 | +0.0238 | 316 | -0.012 | FAIL (house better) |
| basketball | 219 | 1764 | 0.6608 | 0.6642 | -0.0034 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1352 | 0.6056 | 0.6033 | +0.0023 | 272 | +0.029 | FAIL (house better) |
| baseball | 258 | 94 | 0.6528 | 0.6581 | -0.0052 | 6 | +0.157 | collecting |
| baseball | 256 | 87 | 0.6025 | 0.5822 | +0.0203 | 0 | +0.000 | collecting |
| baseball | 251 | 54 | 0.6846 | 0.6843 | +0.0004 | 0 | +0.000 | collecting |

## Day 46 — 2026-11-04 01:44 UTC
Run: OK | snapshot 6499 outcomes / 110 events | failed steps: none
Graded outcomes to date: 103966

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 44944 | 0.6472 | 0.6471 | +0.0001 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 22568 | 0.6499 | 0.6497 | +0.0003 | 248 | +0.126 | FAIL (house better) |
| basketball | 227 | 10782 | 0.6884 | 0.6887 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 8236 | 0.6871 | 0.6872 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6735 | 0.6257 | 0.6274 | -0.0017 | 1090 | +0.058 | **PASS** |
| football | 166 | 5115 | 0.6489 | 0.6479 | +0.0010 | 184 | -0.164 | FAIL (house better) |
| football | 900301 | 2122 | 0.6538 | 0.6298 | +0.0240 | 322 | -0.020 | FAIL (house better) |
| basketball | 219 | 1805 | 0.6606 | 0.6642 | -0.0036 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1424 | 0.6078 | 0.6035 | +0.0043 | 287 | +0.032 | FAIL (house better) |
| baseball | 258 | 94 | 0.6528 | 0.6581 | -0.0052 | 6 | +0.157 | collecting |
| baseball | 256 | 87 | 0.6025 | 0.5822 | +0.0203 | 0 | +0.000 | collecting |
| baseball | 251 | 54 | 0.6846 | 0.6843 | +0.0004 | 0 | +0.000 | collecting |

## Day 47 — 2026-11-04 18:34 UTC
Run: OK | snapshot 6499 outcomes / 110 events | failed steps: none
Graded outcomes to date: 105370

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 45630 | 0.6472 | 0.6471 | +0.0001 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 22828 | 0.6502 | 0.6498 | +0.0003 | 248 | +0.126 | FAIL (house better) |
| basketball | 227 | 10964 | 0.6884 | 0.6887 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 8398 | 0.6872 | 0.6874 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6771 | 0.6260 | 0.6279 | -0.0019 | 1095 | +0.062 | **PASS** |
| football | 166 | 5139 | 0.6496 | 0.6483 | +0.0013 | 188 | -0.172 | FAIL (house better) |
| football | 900301 | 2140 | 0.6544 | 0.6312 | +0.0232 | 324 | -0.012 | FAIL (house better) |
| basketball | 219 | 1825 | 0.6616 | 0.6652 | -0.0036 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1434 | 0.6092 | 0.6050 | +0.0042 | 288 | +0.028 | FAIL (house better) |
| baseball | 258 | 96 | 0.6537 | 0.6599 | -0.0061 | 6 | +0.157 | collecting |
| baseball | 256 | 89 | 0.5997 | 0.5793 | +0.0203 | 0 | +0.000 | collecting |
| baseball | 251 | 56 | 0.6874 | 0.6874 | -0.0000 | 0 | +0.000 | collecting |

## Day 48 — 2026-11-05 01:54 UTC
Run: OK | snapshot 5638 outcomes / 104 events | failed steps: none
Graded outcomes to date: 108095

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 46832 | 0.6474 | 0.6474 | -0.0000 | 1 | +1.950 | **PASS** |
| basketball | 223 | 23493 | 0.6496 | 0.6493 | +0.0003 | 266 | +0.131 | FAIL (house better) |
| basketball | 227 | 11230 | 0.6883 | 0.6886 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 8608 | 0.6871 | 0.6873 | -0.0002 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6889 | 0.6277 | 0.6276 | +0.0002 | 1119 | +0.057 | FAIL (house better) |
| football | 166 | 5249 | 0.6502 | 0.6483 | +0.0019 | 193 | -0.193 | FAIL (house better) |
| football | 900301 | 2184 | 0.6525 | 0.6299 | +0.0226 | 334 | -0.008 | FAIL (house better) |
| basketball | 219 | 1861 | 0.6616 | 0.6654 | -0.0038 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1508 | 0.6106 | 0.6075 | +0.0031 | 293 | +0.038 | FAIL (house better) |
| baseball | 258 | 96 | 0.6537 | 0.6599 | -0.0061 | 6 | +0.157 | collecting |
| baseball | 256 | 89 | 0.5997 | 0.5793 | +0.0203 | 0 | +0.000 | collecting |
| baseball | 251 | 56 | 0.6874 | 0.6874 | -0.0000 | 0 | +0.000 | collecting |

## Day 49 — 2026-11-05 18:40 UTC
Run: OK | snapshot 5638 outcomes / 104 events | failed steps: none
Graded outcomes to date: 110569

| Sport | Market | n | Model LL | House LL | Δ (neg = model better) | EV picks | Picks ROI | Verdict |
|---|---|---|---|---|---|---|---|---|
| basketball | 225 | 48050 | 0.6463 | 0.6463 | +0.0000 | 1 | +1.950 | FAIL (house better) |
| basketball | 223 | 24282 | 0.6489 | 0.6486 | +0.0003 | 266 | +0.131 | FAIL (house better) |
| basketball | 227 | 11402 | 0.6883 | 0.6886 | -0.0003 | 0 | +0.000 | FAIL (picks lose) |
| basketball | 228 | 8762 | 0.6871 | 0.6872 | -0.0001 | 0 | +0.000 | FAIL (picks lose) |
| football | 900300 | 6943 | 0.6277 | 0.6277 | +0.0000 | 1129 | +0.059 | FAIL (house better) |
| football | 166 | 5273 | 0.6502 | 0.6486 | +0.0016 | 197 | -0.168 | FAIL (house better) |
| football | 900301 | 2204 | 0.6521 | 0.6299 | +0.0223 | 335 | -0.002 | FAIL (house better) |
| basketball | 219 | 1900 | 0.6608 | 0.6646 | -0.0038 | 1 | -1.000 | FAIL (picks lose) |
| football | 139 | 1512 | 0.6117 | 0.6078 | +0.0040 | 295 | +0.037 | FAIL (house better) |
| baseball | 258 | 96 | 0.6537 | 0.6599 | -0.0061 | 6 | +0.157 | collecting |
| baseball | 256 | 89 | 0.5997 | 0.5793 | +0.0203 | 0 | +0.000 | collecting |
| baseball | 251 | 56 | 0.6874 | 0.6874 | -0.0000 | 0 | +0.000 | collecting |

