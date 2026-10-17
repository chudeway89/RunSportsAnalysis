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

