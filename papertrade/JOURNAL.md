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

