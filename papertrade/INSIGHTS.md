# Tape insights — every market on every fixture

Built by `engine/tape_insights.py` from `tape_graded.jsonl`. 3,731,251 settled outcomes on 13,848 fixtures, kick-offs 2026-10-12 → 2026-11-20. Halves split at 2026-10-31 15:00.

Read: *actual − house* is the calibration error of SportyBet's own probability; *flat ROI* is what 1 unit on every outcome in the slice returned at first-seen odds. ± is one SE clustered by fixture. A slice is only worth anything if |z| is large (≥3 here, many slices are tested) AND the sign holds in both halves.

## 1. Calibration and margin by sport and odds band
| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| football <1.30 | 432838 (9199 fx) | 1.16 | 82.5% | 82.8% | +0.2pp ±0.1 (z +1.7) | -4.5% ±0.1 | +0.1/+0.3 both |
| football 1.30-1.59 | 342168 (9189 fx) | 1.44 | 64.8% | 65.0% | +0.1pp ±0.1 (z +1.4) | -7.0% ±0.1 | +0.1/+0.2 both |
| football 1.60-2.19 | 401878 (9257 fx) | 1.85 | 49.5% | 49.6% | +0.1pp ±0.1 (z +1.5) | -8.9% ±0.1 | +0.1/+0.1 both |
| football 2.20-3.99 | 616738 (9286 fx) | 3.00 | 30.1% | 30.1% | +0.0pp ±0.1 (z +0.1) | -12.9% ±0.2 | +0.0/-0.0 FLIPS |
| football 4.00+ | 1656747 (9202 fx) | 31.67 | 7.4% | 7.3% | -0.1pp ±0.0 (z -2.2) | -28.0% ±0.7 | -0.1/-0.1 both |
| basketball <1.30 | 13668 (2051 fx) | 1.22 | 80.0% | 78.9% | -1.1pp ±0.6 (z -2.0) | -4.4% ±0.7 | -2.3/-0.4 both |
| basketball 1.30-1.59 | 43565 (2924 fx) | 1.47 | 65.0% | 64.8% | -0.2pp ±0.3 (z -0.6) | -5.4% ±0.5 | -0.6/+0.0 FLIPS |
| basketball 1.60-2.19 | 111385 (3021 fx) | 1.85 | 50.4% | 50.4% | +0.0pp ±0.0 (z +1.0) | -7.2% ±0.1 | +0.0/+0.0 both |
| basketball 2.20-3.99 | 54694 (2828 fx) | 2.72 | 34.5% | 34.6% | +0.1pp ±0.3 (z +0.4) | -8.6% ±0.9 | +0.5/-0.1 FLIPS |
| basketball 4.00+ | 8072 (1917 fx) | 5.45 | 17.0% | 18.6% | +1.6pp ±0.7 (z +2.2) | -7.8% ±3.8 | +3.3/+0.6 both |
| ice hockey <1.30 | 4724 (770 fx) | 1.17 | 82.3% | 81.9% | -0.4pp ±0.7 (z -0.6) | -4.6% ±0.8 | +nan/-0.4 both |
| ice hockey 1.30-1.59 | 6182 (824 fx) | 1.44 | 65.8% | 66.5% | +0.6pp ±0.6 (z +1.0) | -4.4% ±0.9 | +nan/+0.6 FLIPS |
| ice hockey 1.60-2.19 | 12385 (848 fx) | 1.85 | 50.6% | 50.4% | -0.2pp ±0.2 (z -1.3) | -7.4% ±0.3 | +nan/-0.2 both |
| ice hockey 2.20-3.99 | 9756 (850 fx) | 2.85 | 32.7% | 32.6% | -0.1pp ±0.5 (z -0.2) | -10.3% ±1.4 | +nan/-0.1 both |
| ice hockey 4.00+ | 8699 (854 fx) | 7.04 | 14.0% | 14.2% | +0.2pp ±0.4 (z +0.4) | -16.9% ±2.4 | +nan/+0.2 FLIPS |
| volleyball 1.60-2.19 | 2356 (277 fx) | 1.86 | 50.0% | 50.0% | +0.0pp ±0.2 (z +0.1) | -7.6% ±0.4 | +nan/+0.0 FLIPS |
| volleyball 2.20-3.99 | 609 (212 fx) | 2.99 | 29.8% | 28.4% | -1.4pp ±1.5 (z -1.0) | -18.3% ±4.3 | +nan/-1.4 both |
| volleyball 4.00+ | 1479 (307 fx) | 9.64 | 12.4% | 11.4% | -1.0pp ±0.6 (z -1.8) | -31.3% ±4.9 | +nan/-1.0 both |
| american football 1.60-2.19 | 978 (44 fx) | 1.86 | 50.2% | 50.5% | +0.3pp ±0.2 (z +1.6) | -6.2% ±0.4 | +nan/+0.3 FLIPS |

## 2. Strongest slices on the whole board (market × side × odds band, n ≥ 400, |z| ≥ 2.5)
| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| football / Home Team or Over 2.5 / No / 4.00+ | 818 (818 fx) | 5.12 | 15.8% | 11.0% | -4.8pp ±1.1 (z -4.4) | -48.2% ±5.2 | -3.7/-5.9 both |
| football / Goal Range / 2-3 / 1.60-2.19 | 2628 (2628 fx) | 2.00 | 45.1% | 48.9% | +3.8pp ±1.0 (z +3.9) | -2.1% ±2.0 | +3.0/+4.7 both |
| football / Handicap 0:1 / Draw (0:1) / 2.20-3.99 | 3225 (3225 fx) | 3.68 | 23.6% | 26.3% | +2.7pp ±0.8 (z +3.5) | -3.4% ±2.9 | +2.6/+2.8 both |
| football / Halftime/Fulltime & 1st Half Over/Under 2.5 / Away/Draw & Over 2.5 / 4.00+ | 4852 (4852 fx) | 95.13 | 0.9% | 0.5% | -0.3pp ±0.1 (z -3.3) | -53.5% ±9.7 | -0.2/-0.5 both |
| football / 2nd Half - Asian Handicap / Away (0) / 2.20-3.99 | 433 (433 fx) | 2.79 | 34.4% | 27.7% | -6.7pp ±2.1 (z -3.1) | -24.7% ±6.0 | -7.2/-6.2 both |
| football / Away Team Total Corners / Under / 2.20-3.99 | 2135 (1757 fx) | 2.90 | 32.1% | 35.6% | +3.6pp ±1.2 (z +3.1) | +0.5% ±3.3 | +3.2/+4.0 both |
| football / 1X2 & Over/Under 3.5 / Home & Under 3.5 / 2.20-3.99 | 3211 (3211 fx) | 2.94 | 30.2% | 32.8% | +2.5pp ±0.8 (z +3.1) | -6.5% ±2.4 | +0.9/+4.3 both |
| football / Asian Handicap 0 / Home (0) / 1.30-1.59 | 786 (786 fx) | 1.44 | 66.5% | 71.4% | +4.9pp ±1.6 (z +3.0) | +2.4% ±2.3 | +6.4/+3.3 both |
| football / 1X2 & Over/Under 3.5 / Away & Under 3.5 / 4.00+ | 2735 (2735 fx) | 6.82 | 14.6% | 12.7% | -1.9pp ±0.6 (z -3.0) | -29.6% ±3.7 | -2.3/-1.5 both |
| football / 2nd Half - Asian Handicap / Away (+1.0) / <1.30 | 483 (483 fx) | 1.19 | 82.2% | 76.6% | -5.6pp ±1.9 (z -2.9) | -9.3% ±2.3 | -6.6/-4.5 both |
| football / Away Team Total Corners / Over / 1.30-1.59 | 1494 (1487 fx) | 1.43 | 66.9% | 63.3% | -3.6pp ±1.2 (z -2.9) | -9.8% ±1.8 | -2.0/-5.2 both |
| football / 1X2 & Over/Under 2.5 / Draw & Under 2.5 / 2.20-3.99 | 917 (917 fx) | 3.55 | 24.2% | 28.5% | +4.3pp ±1.5 (z +2.9) | +0.1% ±5.3 | +4.4/+4.1 both |
| football / Draw No Bet / Away / 2.20-3.99 | 2427 (2427 fx) | 2.84 | 31.8% | 29.2% | -2.6pp ±0.9 (z -2.8) | -19.9% ±2.6 | -3.4/-1.9 both |
| football / 2nd Half - Home Team Clean Sheet / No / 2.20-3.99 | 1325 (1325 fx) | 2.51 | 35.4% | 39.2% | +3.8pp ±1.3 (z +2.8) | -2.3% ±3.4 | +1.9/+5.5 both |
| football / 2nd Half - Asian Handicap / Home (-1.0) / 4.00+ | 435 (435 fx) | 5.21 | 17.1% | 22.8% | +5.6pp ±2.0 (z +2.8) | +15.0% ±10.3 | +8.0/+2.9 both |
| football / Winning Margin / Home by 1 / 4.00+ | 3372 (3372 fx) | 6.11 | 17.4% | 19.3% | +1.9pp ±0.7 (z +2.8) | -5.5% ±3.6 | +1.0/+2.9 both |
| football / Winning Margin / Home by 1 / 2.20-3.99 | 1660 (1660 fx) | 3.67 | 23.6% | 26.6% | +3.0pp ±1.1 (z +2.8) | -2.3% ±4.0 | +2.4/+3.7 both |
| basketball / Over/Under (incl. overtime) 157.5 / Over / 1.60-2.19 | 461 (461 fx) | 1.84 | 50.7% | 44.3% | -6.4pp ±2.3 (z -2.8) | -19.0% ±4.3 | -5.5/-6.7 both |
| football / 1st Half - Over/Under / Under / <1.30 | 8252 (4805 fx) | 1.13 | 85.6% | 87.0% | +1.4pp ±0.5 (z +2.8) | -1.9% ±0.6 | +1.5/+1.2 both |
| football / Asian Handicap 0 / Away (0) / 2.20-3.99 | 1107 (1107 fx) | 2.85 | 32.7% | 29.0% | -3.7pp ±1.4 (z -2.8) | -19.4% ±3.9 | -4.0/-3.4 both |
| football / 2nd Half - 1X2 / Home / 4.00+ | 816 (816 fx) | 6.28 | 16.6% | 13.4% | -3.2pp ±1.2 (z -2.7) | -28.5% ±6.8 | -4.1/-2.3 both |
| football / Home Team Total Corners / Over / <1.30 | 904 (904 fx) | 1.22 | 78.7% | 74.8% | -3.9pp ±1.4 (z -2.7) | -8.7% ±1.8 | -3.1/-4.9 both |
| football / Exact Goals / 4 / 4.00+ | 3217 (3217 fx) | 5.18 | 16.3% | 14.6% | -1.7pp ±0.6 (z -2.7) | -26.2% ±3.2 | -1.1/-2.3 both |
| basketball / Over/Under (incl. overtime) 169.5 / Under / 1.60-2.19 | 607 (607 fx) | 1.85 | 51.0% | 56.3% | +5.4pp ±2.0 (z +2.7) | +3.3% ±3.7 | +7.1/+4.2 both |
| football / Both Halves Over 1.5 / No / 1.30-1.59 | 788 (788 fx) | 1.37 | 69.6% | 65.1% | -4.5pp ±1.7 (z -2.6) | -10.9% ±2.3 | -6.1/-2.9 both |
| football / 2nd Half - Away Team Clean Sheet / No / <1.30 | 460 (460 fx) | 1.23 | 77.3% | 82.0% | +4.7pp ±1.8 (z +2.6) | +0.3% ±2.2 | +9.2/+1.5 both |
| football / 2nd Half - GG/NG / No / <1.30 | 2925 (2925 fx) | 1.23 | 77.5% | 75.5% | -2.1pp ±0.8 (z -2.6) | -7.3% ±1.0 | -1.8/-2.4 both |
| basketball / Over/Under (incl. overtime) 169.5 / Over / 1.60-2.19 | 591 (591 fx) | 1.86 | 50.5% | 45.2% | -5.3pp ±2.0 (z -2.6) | -16.9% ±3.8 | -6.9/-4.2 both |
| football / Asian Handicap 1 / Home (+1.0) / <1.30 | 1218 (1218 fx) | 1.17 | 82.7% | 85.3% | +2.6pp ±1.0 (z +2.6) | -0.5% ±1.2 | +1.1/+4.2 both |
| football / Draw No Bet / Home / 1.30-1.59 | 1791 (1791 fx) | 1.44 | 65.7% | 68.5% | +2.8pp ±1.1 (z +2.6) | -2.0% ±1.6 | +3.7/+2.1 both |
| football / Goal Bounds - Away / 0 / 1.60-2.19 | 1147 (1147 fx) | 1.97 | 47.2% | 43.4% | -3.8pp ±1.5 (z -2.6) | -15.3% ±2.9 | -3.3/-4.1 both |
| football / 1X2 & Over/Under 4.5 / Away & Under 4.5 / 4.00+ | 1940 (1940 fx) | 6.86 | 14.3% | 12.4% | -1.9pp ±0.7 (z -2.6) | -31.5% ±4.4 | -3.5/-0.2 both |
| football / Winning Margin / Away by 1 / 2.20-3.99 | 703 (703 fx) | 3.71 | 23.4% | 27.7% | +4.3pp ±1.7 (z +2.6) | +2.5% ±6.3 | +3.7/+5.0 both |
| football / 1X2 & Over/Under 3.5 / Draw & Under 3.5 / 2.20-3.99 | 958 (958 fx) | 3.54 | 24.1% | 27.8% | +3.7pp ±1.4 (z +2.6) | -3.0% ±5.1 | +4.0/+3.3 both |
| football / Away Team Clean Sheet / Yes / 4.00+ | 3397 (3397 fx) | 5.41 | 13.8% | 12.4% | -1.4pp ±0.6 (z -2.5) | -39.0% ±2.8 | -1.8/-1.1 both |
| football / 1X2 & GG/NG / Home & yes / 2.20-3.99 | 2192 (2192 fx) | 3.18 | 27.7% | 30.2% | +2.5pp ±1.0 (z +2.5) | -6.3% ±3.1 | +2.1/+2.9 both |
| football / 2nd Half - Multigoals / 1-3 / <1.30 | 3730 (3730 fx) | 1.27 | 72.1% | 73.9% | +1.8pp ±0.7 (z +2.5) | -5.9% ±0.9 | +2.1/+1.5 both |
| basketball / Over/Under (incl. overtime) 167.5 / Over / 1.60-2.19 | 638 (638 fx) | 1.87 | 50.4% | 45.5% | -5.0pp ±2.0 (z -2.5) | -16.0% ±3.7 | -8.2/-2.8 both |
| football / Asian Handicap 1 / Away (-1.0) / 4.00+ | 985 (985 fx) | 5.36 | 15.8% | 13.1% | -2.7pp ±1.1 (z -2.5) | -34.6% ±5.5 | -1.4/-4.1 both |
| football / 2nd Half - Over/Under / Over / 1.30-1.59 | 2179 (2153 fx) | 1.42 | 67.2% | 69.7% | +2.5pp ±1.0 (z +2.5) | -1.3% ±1.4 | +3.8/+1.0 both |
| football / Asian Handicap -0.5 / Home (-0.5) / 1.60-2.19 | 2974 (2974 fx) | 1.89 | 49.4% | 51.7% | +2.3pp ±0.9 (z +2.5) | -3.3% ±1.7 | +2.2/+2.3 both |

1071 slices tested; by chance alone ~13 would show |z| ≥ 2.5 and ~2.9 |z| ≥ 3.

## 3. Rule audit — each binding rule tested on the whole board, not just our legs
| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| Unders p<0.82 (all lines) | 20949 (9005 fx) | 1.54 | 63.4% | 63.6% | +0.2pp ±0.5 (z +0.4) | -5.0% ±0.8 | -1.1/+1.4 FLIPS |
| Unders p≥0.82 | 8329 (4196 fx) | 1.10 | 89.1% | 89.2% | +0.2pp ±0.5 (z +0.4) | -2.4% ±0.5 | -0.4/+0.8 FLIPS |
| Unders 1.18-2.2 when favourite p≥0.65 | 3902 (1539 fx) | 1.54 | 63.6% | 62.4% | -1.2pp ±1.2 (z -1.0) | -6.7% ±1.9 | -1.2/-1.2 both |
| Overs 1.18-2.2 (.5 lines) | 15240 (8998 fx) | 1.58 | 62.0% | 62.0% | +0.0pp ±0.5 (z +0.0) | -5.8% ±0.7 | +1.1/-1.0 FLIPS |
| Overs integer line (Over 2/3) 1.18-2.2 | 3496 (2755 fx) | 1.55 | 63.6% | 63.5% | -0.1pp ±0.9 (z -0.1) | -4.9% ±1.5 | -0.1/-0.2 both |
| Over 1.5 all | 7447 (7447 fx) | 1.27 | 76.2% | 75.9% | -0.3pp ±0.5 (z -0.6) | -4.8% ±0.6 | +0.7/-1.3 FLIPS |
| Away 1X2 p<0.75 (odds<2.2) | 1875 (1875 fx) | 1.78 | 53.9% | 56.3% | +2.3pp ±1.1 (z +2.0) | -1.4% ±2.1 | +2.4/+2.3 both |
| Away 1X2 p≥0.75 | 203 (203 fx) | 1.16 | 83.3% | 82.8% | -0.5pp ±2.6 (z -0.2) | -4.0% ±3.1 | +2.2/-3.5 FLIPS |
| Home 1X2 odds<2.2 | 4678 (4678 fx) | 1.69 | 57.7% | 58.7% | +1.0pp ±0.7 (z +1.4) | -4.0% ±1.2 | +0.9/+1.1 both |
| Draw (all) | 9331 (9331 fx) | 3.97 | 24.1% | 24.4% | +0.3pp ±0.4 (z +0.7) | -9.9% ±1.7 | +1.0/-0.3 FLIPS |
| AH +1.5 receiver when fav p≥0.55 | 2475 (2474 fx) | 1.72 | 56.0% | 58.4% | +2.4pp ±1.0 (z +2.4) | -1.8% ±1.7 | +1.8/+2.9 both |
| AH +2.5 receiver when fav p≥0.60 | 1151 (1151 fx) | 1.37 | 70.8% | 71.2% | +0.4pp ±1.3 (z +0.3) | -4.0% ±1.8 | -2.3/+3.0 FLIPS |
| DC 12 (Home or Away) | 9121 (9121 fx) | 1.25 | 75.6% | 75.6% | -0.0pp ±0.4 (z -0.1) | -6.2% ±0.6 | -0.7/+0.6 FLIPS |
| DC 1X / X2 | 18238 (9122 fx) | 1.60 | 62.2% | 62.2% | +0.0pp ±0.2 (z +0.1) | -10.3% ±0.4 | +0.4/-0.3 FLIPS |
| DNB 1.18-2.2 | 7232 (5543 fx) | 1.60 | 60.0% | 61.1% | +1.1pp ±0.4 (z +2.8) | -5.5% ±0.6 | +1.5/+0.7 both |
| BTTS Yes | 8159 (8159 fx) | 1.75 | 53.7% | 54.2% | +0.4pp ±0.5 (z +0.8) | -6.8% ±1.0 | +1.9/-1.0 FLIPS |
| BTTS No | 8159 (8159 fx) | 2.02 | 46.3% | 45.8% | -0.4pp ±0.5 (z -0.8) | -9.5% ±1.1 | -1.9/+1.0 FLIPS |
| Both halves U1.5 (m59) No | 6562 (6562 fx) | 1.44 | 66.7% | 66.6% | -0.1pp ±0.6 (z -0.1) | -5.6% ±0.8 | +0.5/-0.6 FLIPS |
| Corners 166 Over | 6025 (1426 fx) | 2.01 | 50.2% | 49.2% | -1.0pp ±1.1 (z -0.9) | -9.8% ±2.3 | +0.3/-2.4 FLIPS |
| Corners 166 Under | 6025 (1426 fx) | 2.04 | 49.8% | 50.8% | +1.0pp ±1.1 (z +0.9) | -5.8% ±2.3 | -0.3/+2.4 FLIPS |
| Team corners home 900300 Over | 8031 (1769 fx) | 2.29 | 48.0% | 46.4% | -1.6pp ±0.9 (z -1.8) | -10.2% ±2.1 | -0.9/-2.4 both |
| Team corners home 900300 Under | 8031 (1769 fx) | 2.11 | 52.0% | 53.6% | +1.6pp ±0.9 (z +1.8) | -2.5% ±2.0 | +0.9/+2.4 both |
| Team corners away 900301 Over | 8022 (1770 fx) | 2.43 | 47.2% | 45.2% | -2.0pp ±0.9 (z -2.2) | -11.5% ±2.1 | -1.5/-2.5 both |
| Team corners away 900301 Under | 8022 (1770 fx) | 2.14 | 52.8% | 54.8% | +2.0pp ±0.9 (z +2.2) | -2.1% ±1.9 | +1.5/+2.5 both |
| Bookings 139 Over | 2594 (579 fx) | 2.30 | 51.1% | 49.4% | -1.7pp ±1.4 (z -1.2) | -12.4% ±3.5 | -3.3/-0.0 both |
| Bookings 139 Under | 2594 (579 fx) | 2.55 | 48.9% | 50.6% | +1.7pp ±1.4 (z +1.2) | -7.9% ±3.4 | +3.3/+0.0 both |
| Women — Over (1.18-2.2) | 320 (198 fx) | 1.61 | 60.0% | 64.7% | +4.7pp ±3.0 (z +1.5) | +0.5% ±5.0 | +nan/+4.7 FLIPS |
| Women — Under (1.18-2.2) | 351 (198 fx) | 1.55 | 62.2% | 57.5% | -4.6pp ±3.3 (z -1.4) | -13.2% ±5.2 | +nan/-4.6 both |
| Youth/reserves — Over (1.18-2.2) | 332 (204 fx) | 1.58 | 61.3% | 58.4% | -2.8pp ±3.2 (z -0.9) | -11.3% ±5.1 | -0.9/-3.0 both |
| Friendlies — 1X2 favourite | 26 (26 fx) | 1.45 | 68.4% | 76.9% | +8.5pp ±7.8 (z +1.1) | +7.7% ±12.3 | -16.8/+10.6 FLIPS |
| Cup — fav 1X2 p≥0.65 | 266 (266 fx) | 1.26 | 77.1% | 74.4% | -2.7pp ±2.6 (z -1.0) | -7.7% ±3.4 | -3.9/-0.8 both |
| League — fav 1X2 p≥0.65 | 1220 (1220 fx) | 1.30 | 73.9% | 75.2% | +1.3pp ±1.2 (z +1.0) | -2.7% ±1.6 | +1.0/+1.5 both |
| BB handicap receiving ≥15 pts | 5658 (1159 fx) | 1.56 | 64.1% | 63.2% | -0.9pp ±1.5 (z -0.6) | -5.9% ±2.4 | -2.9/-0.2 both |
| BB handicap receiving 8.5-14.5 | 9032 (1790 fx) | 1.60 | 62.7% | 61.7% | -1.1pp ±1.0 (z -1.0) | -6.3% ±1.8 | -2.5/-0.2 both |
| BB handicap giving | 29760 (3013 fx) | 2.70 | 41.2% | 41.8% | +0.6pp ±0.7 (z +0.9) | -4.7% ±1.8 | +1.8/+0.0 both |
| BB ML p≥0.75 | 1203 (1203 fx) | 1.12 | 87.3% | 86.0% | -1.3pp ±1.0 (z -1.3) | -4.7% ±1.1 | -2.7/-0.8 both |
| BB totals Over 1.18-2.2 | 36299 (2963 fx) | 1.65 | 58.6% | 57.5% | -1.1pp ±0.8 (z -1.3) | -7.6% ±1.4 | -1.1/-1.1 both |
| BB totals Under 1.18-2.2 | 36290 (2963 fx) | 1.66 | 58.4% | 59.6% | +1.2pp ±0.8 (z +1.4) | -3.9% ±1.4 | +0.4/+1.5 both |

## 4. Does form, league scoring or history add anything the price lacks? (football, prior matches only)


**Over 2.5 by league scoring so far (avg goals of earlier games in the same competition, ≥8 games)**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| league avg <2.3 | 838 (838 fx) | 2.14 | 44.4% | 43.7% | -0.7pp ±1.7 (z -0.4) | -9.8% ±3.7 | +3.3/-2.4 FLIPS |
| 2.3-2.6 | 933 (933 fx) | 1.90 | 50.4% | 51.0% | +0.6pp ±1.6 (z +0.4) | -5.8% ±3.1 | +1.6/+0.2 both |
| 2.6-2.9 | 1301 (1301 fx) | 1.82 | 52.5% | 52.1% | -0.3pp ±1.4 (z -0.3) | -8.0% ±2.5 | -0.5/-0.3 both |
| 2.9-3.2 | 1095 (1095 fx) | 1.74 | 55.3% | 53.5% | -1.8pp ±1.5 (z -1.2) | -9.6% ±2.6 | +0.7/-3.0 FLIPS |
| ≥3.2 | 1459 (1459 fx) | 1.59 | 60.3% | 59.6% | -0.8pp ±1.3 (z -0.6) | -6.5% ±2.1 | +0.9/-1.6 FLIPS |

**Over 1.5 by league scoring so far**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| league avg <2.3 | 740 (740 fx) | 1.39 | 69.0% | 65.9% | -3.1pp ±1.7 (z -1.8) | -9.7% ±2.4 | -3.9/-2.7 both |
| 2.3-2.6 | 879 (879 fx) | 1.29 | 74.4% | 76.0% | +1.5pp ±1.4 (z +1.1) | -2.5% ±1.9 | +5.9/-0.6 FLIPS |
| 2.6-2.9 | 1088 (1088 fx) | 1.26 | 76.2% | 75.9% | -0.2pp ±1.3 (z -0.2) | -4.5% ±1.6 | +0.4/-0.5 FLIPS |
| 2.9-3.2 | 1011 (1011 fx) | 1.24 | 77.8% | 76.8% | -1.1pp ±1.3 (z -0.8) | -5.3% ±1.7 | +2.1/-2.7 FLIPS |
| ≥3.2 | 1179 (1179 fx) | 1.20 | 80.8% | 80.6% | -0.3pp ±1.1 (z -0.2) | -3.9% ±1.4 | +1.1/-1.1 FLIPS |

**Over 2.5 by both teams' recent match goals (last ≤5 each, avg of GF+GA per game)**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| 2.0-2.5 | 342 (342 fx) | 1.88 | 50.8% | 49.4% | -1.4pp ±2.7 (z -0.5) | -8.9% ±5.1 | -0.2/-1.4 both |
| 2.5-3.0 | 460 (460 fx) | 1.78 | 53.8% | 51.7% | -2.0pp ±2.3 (z -0.9) | -10.7% ±4.1 | -5.4/-1.8 both |
| 3.0-3.5 | 367 (367 fx) | 1.67 | 57.7% | 59.7% | +2.0pp ±2.5 (z +0.8) | -2.0% ±4.3 | +8.0/+1.5 both |
| ≥3.5 | 357 (357 fx) | 1.59 | 60.7% | 56.3% | -4.4pp ±2.5 (z -1.7) | -13.0% ±4.1 | -0.2/-4.7 both |

**Under 2.5 by both teams' recent match goals**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| 2.0-2.5 | 342 (342 fx) | 1.96 | 49.2% | 50.6% | +1.4pp ±2.7 (z +0.5) | -3.7% ±5.3 | +0.2/+1.4 both |
| 2.5-3.0 | 460 (460 fx) | 2.08 | 46.2% | 48.3% | +2.0pp ±2.3 (z +0.9) | -4.8% ±4.7 | +5.4/+1.8 both |
| 3.0-3.5 | 367 (367 fx) | 2.29 | 42.3% | 40.3% | -2.0pp ±2.5 (z -0.8) | -12.2% ±5.7 | -8.0/-1.5 both |
| ≥3.5 | 357 (357 fx) | 2.48 | 39.3% | 43.7% | +4.4pp ±2.5 (z +1.7) | +0.7% ±6.3 | +0.2/+4.7 both |

**Home win by form gap (home last-5 pts/game − away last-5 pts/game)**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| away in much better form (≤-1.0 pts/g) | 254 (254 fx) | 3.43 | 33.9% | 37.0% | +3.1pp ±2.9 (z +1.1) | +2.9% ±9.9 | -5.6/+3.6 FLIPS |
| -1.0 to -0.4 | 339 (339 fx) | 2.87 | 38.6% | 33.9% | -4.7pp ±2.4 (z -1.9) | -21.6% ±6.5 | -4.7/-4.7 both |
| similar (-0.4 to 0.4) | 529 (529 fx) | 2.53 | 44.8% | 46.9% | +2.1pp ±2.0 (z +1.1) | -4.6% ±5.0 | +4.8/+1.9 both |
| 0.4 to 1.0 | 245 (245 fx) | 2.24 | 48.7% | 47.3% | -1.3pp ±3.0 (z -0.4) | -8.5% ±6.9 | -2.5/-1.3 both |
| home much better (≥1.0) | 321 (321 fx) | 2.10 | 52.9% | 55.8% | +2.9pp ±2.7 (z +1.1) | +0.9% ±5.6 | +6.0/+2.7 both |

**Away win by form gap**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| away in much better form (≤-1.0 pts/g) | 254 (254 fx) | 2.75 | 41.5% | 41.7% | +0.2pp ±2.9 (z +0.1) | -7.1% ±7.7 | +6.9/-0.1 FLIPS |
| -1.0 to -0.4 | 339 (339 fx) | 3.16 | 36.2% | 40.4% | +4.2pp ±2.5 (z +1.7) | +10.7% ±10.7 | +6.4/+4.1 both |
| similar (-0.4 to 0.4) | 529 (529 fx) | 3.95 | 30.8% | 31.8% | +1.0pp ±1.9 (z +0.5) | -6.9% ±7.0 | +5.5/+0.7 both |
| 0.4 to 1.0 | 245 (245 fx) | 4.26 | 27.5% | 26.5% | -0.9pp ±2.7 (z -0.3) | -15.5% ±9.9 | +3.9/-1.2 FLIPS |
| home much better (≥1.0) | 321 (321 fx) | 5.32 | 24.3% | 24.6% | +0.3pp ±2.3 (z +0.1) | -4.2% ±11.1 | +11.9/-0.4 FLIPS |

**Draw by form gap**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| away in much better form (≤-1.0 pts/g) | 254 (254 fx) | 3.87 | 24.6% | 21.3% | -3.3pp ±2.6 (z -1.3) | -21.7% ±9.5 | -1.3/-3.4 both |
| -1.0 to -0.4 | 339 (339 fx) | 3.75 | 25.2% | 25.7% | +0.4pp ±2.4 (z +0.2) | -7.5% ±8.8 | -1.6/+0.6 FLIPS |
| similar (-0.4 to 0.4) | 529 (529 fx) | 3.91 | 24.4% | 21.4% | -3.1pp ±1.8 (z -1.7) | -22.8% ±6.6 | -10.3/-2.6 both |
| 0.4 to 1.0 | 245 (245 fx) | 3.99 | 23.9% | 26.1% | +2.2pp ±2.8 (z +0.8) | +0.7% ±11.1 | -1.4/+2.4 FLIPS |
| home much better (≥1.0) | 321 (321 fx) | 4.28 | 22.8% | 19.6% | -3.2pp ±2.2 (z -1.4) | -24.8% ±8.7 | -17.9/-2.3 both |

**Home win when FORM disagrees with PRICE (form gap/3 minus price gap; + = form likes home more than the price does)**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| form much less keen (≤-0.4) | 382 (382 fx) | 1.87 | 55.5% | 57.6% | +2.0pp ±2.4 (z +0.9) | -1.5% ±4.7 | +1.7/+2.1 both |
| -0.4 to -0.15 | 440 (440 fx) | 2.31 | 46.5% | 48.4% | +2.0pp ±2.3 (z +0.9) | -0.1% ±5.7 | +12.3/+1.5 both |
| agree (±0.15) | 505 (505 fx) | 2.62 | 41.4% | 39.0% | -2.4pp ±2.1 (z -1.2) | -10.6% ±5.6 | -5.4/-2.2 both |
| 0.15 to 0.4 | 247 (247 fx) | 3.23 | 34.9% | 35.6% | +0.7pp ±2.8 (z +0.3) | -15.2% ±7.8 | -5.0/+1.1 FLIPS |

**Home win by home side's last-3 HOME pts/game**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| 0-0.67 | 1242 (1242 fx) | 2.88 | 40.8% | 40.8% | +0.0pp ±1.3 (z +0.0) | -5.4% ±4.0 | +0.0/+0.1 both |
| 0.67-1.34 | 941 (941 fx) | 2.63 | 43.9% | 44.0% | +0.1pp ±1.5 (z +0.1) | -6.4% ±4.0 | -2.9/+1.3 FLIPS |
| 1.34-2.0 | 704 (704 fx) | 2.45 | 47.0% | 47.7% | +0.7pp ±1.7 (z +0.4) | -7.9% ±4.1 | -1.7/+1.0 FLIPS |
| 3.0 | 1590 (1590 fx) | 2.39 | 47.6% | 48.3% | +0.7pp ±1.2 (z +0.6) | -6.9% ±2.8 | +2.2/+0.1 both |

## 5. By competition type (football, odds 1.18–2.2 only)
| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| top5+UEFA — Over | 950 (322 fx) | 1.56 | 63.3% | 64.0% | +0.7pp ±2.4 (z +0.3) | -4.0% ±3.9 | +3.9/-3.3 FLIPS |
| top5+UEFA — Under | 1154 (322 fx) | 1.52 | 66.4% | 66.3% | -0.1pp ±2.5 (z -0.1) | -2.0% ±3.8 | -5.2/+5.9 FLIPS |
| top5+UEFA — BTTS Yes | 315 (315 fx) | 1.66 | 58.0% | 55.9% | -2.1pp ±2.8 (z -0.8) | -7.4% ±4.7 | -2.5/-1.7 both |
| other league — Over | 15529 (7570 fx) | 1.57 | 62.3% | 62.2% | -0.1pp ±0.5 (z -0.2) | -5.7% ±0.9 | +0.8/-1.0 FLIPS |
| other league — Under | 17396 (7577 fx) | 1.54 | 63.5% | 63.8% | +0.3pp ±0.5 (z +0.6) | -5.0% ±0.8 | -0.9/+1.5 FLIPS |
| other league — Home 1X2 | 3811 (3811 fx) | 1.73 | 55.8% | 56.5% | +0.7pp ±0.8 (z +0.9) | -4.5% ±1.4 | +0.5/+1.0 both |
| other league — Away 1X2 | 1557 (1557 fx) | 1.78 | 54.3% | 56.8% | +2.6pp ±1.2 (z +2.1) | -1.3% ±2.2 | +2.4/+2.8 both |
| other league — BTTS Yes | 6379 (6379 fx) | 1.70 | 55.0% | 55.5% | +0.5pp ±0.6 (z +0.9) | -6.8% ±1.1 | +2.1/-1.0 FLIPS |
| cup — Over | 1508 (665 fx) | 1.57 | 62.7% | 62.1% | -0.6pp ±1.8 (z -0.3) | -6.4% ±2.9 | -0.4/-0.9 both |
| cup — Under | 1761 (665 fx) | 1.53 | 64.2% | 64.5% | +0.3pp ±1.8 (z +0.1) | -4.5% ±2.8 | -0.7/+1.4 FLIPS |
| cup — Home 1X2 | 290 (290 fx) | 1.60 | 61.3% | 60.7% | -0.6pp ±2.7 (z -0.2) | -7.7% ±4.5 | +3.6/-5.0 FLIPS |
| cup — Away 1X2 | 235 (235 fx) | 1.65 | 59.5% | 58.7% | -0.7pp ±3.2 (z -0.2) | -5.4% ±5.4 | +1.2/-4.1 FLIPS |
| cup — BTTS Yes | 537 (537 fx) | 1.75 | 53.4% | 51.6% | -1.8pp ±2.2 (z -0.9) | -10.5% ±3.8 | +0.0/-4.9 FLIPS |
| youth/res — Over | 332 (204 fx) | 1.58 | 61.3% | 58.4% | -2.8pp ±3.2 (z -0.9) | -11.3% ±5.1 | -0.9/-3.0 both |
| youth/res — Under | 361 (204 fx) | 1.60 | 60.5% | 61.5% | +1.0pp ±3.2 (z +0.3) | -4.8% ±5.3 | +6.8/+0.5 both |
| women — Over | 320 (198 fx) | 1.61 | 60.0% | 64.7% | +4.7pp ±3.0 (z +1.5) | +0.5% ±5.0 | +nan/+4.7 FLIPS |
| women — Under | 351 (198 fx) | 1.55 | 62.2% | 57.5% | -4.6pp ±3.3 (z -1.4) | -13.2% ±5.2 | +nan/-4.6 both |

## 6. Competitions with the biggest goal-total miscalibration (O/U 1.18–2.2, n ≥ 120)
| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| Colombia / Liga DIMAYOR — Under | 189 (62 fx) | 1.52 | 64.6% | 79.9% | +15.3pp ±4.5 (z +3.4) | +18.6% ±7.2 | +18.8/+11.4 both |
| Sweden / Allsvenskan — Under | 125 (36 fx) | 1.51 | 65.3% | 81.6% | +16.3pp ±5.9 (z +2.8) | +21.1% ±9.2 | +14.5/+18.5 both |
| England / Premier League — Under | 132 (36 fx) | 1.52 | 66.8% | 81.1% | +14.3pp ±5.7 (z +2.5) | +21.1% ±9.2 | +19.2/+9.7 both |
| Turkiye / 1. Lig — Over | 121 (43 fx) | 1.53 | 64.4% | 77.7% | +13.2pp ±5.5 (z +2.4) | +15.8% ±8.7 | +11.5/+16.1 both |
| England / Championship — Under | 210 (62 fx) | 1.55 | 64.9% | 51.9% | -13.0pp ±5.9 (z -2.2) | -23.0% ±9.2 | -14.7/-11.3 both |
| International Clubs / UEFA Champions League — Under | 210 (54 fx) | 1.53 | 66.5% | 53.3% | -13.2pp ±6.3 (z -2.1) | -21.7% ±9.7 | -15.6/-8.7 both |
| Colombia / Liga DIMAYOR — Over | 166 (63 fx) | 1.58 | 62.2% | 50.6% | -11.6pp ±5.8 (z -2.0) | -24.4% ±9.3 | -10.5/-12.9 both |
| Netherlands / Eredivisie — Under | 120 (32 fx) | 1.55 | 64.8% | 48.3% | -16.4pp ±8.5 (z -1.9) | -27.9% ±13.1 | -9.7/-21.9 both |
| International Clubs / UEFA Conference League — Under | 129 (36 fx) | 1.52 | 66.6% | 78.3% | +11.7pp ±6.3 (z +1.8) | +17.4% ±9.9 | -0.3/+23.2 FLIPS |
| International Clubs / UEFA Champions League — Over | 172 (54 fx) | 1.58 | 62.6% | 72.7% | +10.0pp ±5.6 (z +1.8) | +11.9% ±9.2 | +13.6/+2.3 both |
| Italy / Serie B — Under | 136 (44 fx) | 1.54 | 63.9% | 74.3% | +10.3pp ±5.9 (z +1.8) | +11.5% ±9.4 | +10.1/+10.6 both |
| Italy / Serie A — Over | 135 (46 fx) | 1.56 | 63.3% | 73.3% | +10.1pp ±6.0 (z +1.7) | +11.9% ±9.7 | +16.9/+0.2 both |
| International / UEFA Nations League — Over | 140 (52 fx) | 1.57 | 62.8% | 72.1% | +9.4pp ±5.9 (z +1.6) | +10.4% ±9.6 | +nan/+9.4 FLIPS |
| England / League One — Under | 168 (48 fx) | 1.52 | 65.2% | 74.4% | +9.2pp ±5.8 (z +1.6) | +9.5% ±9.1 | +9.6/+8.5 both |
| Brazil / Brasileiro Serie B — Over | 122 (47 fx) | 1.59 | 61.8% | 51.6% | -10.1pp ±6.7 (z -1.5) | -21.9% ±10.7 | -27.5/+0.0 FLIPS |
| Portugal / Campeonato de Portugal — Over | 149 (79 fx) | 1.61 | 60.1% | 67.1% | +7.0pp ±4.6 (z +1.5) | +4.4% ±7.8 | +9.5/+5.7 both |
| Italy / Serie A — Under | 163 (46 fx) | 1.52 | 66.9% | 57.1% | -9.9pp ±6.7 (z -1.5) | -17.1% ±10.2 | -21.0/+5.6 FLIPS |
| International / CONCACAF Nations League — Under | 121 (32 fx) | 1.54 | 64.1% | 52.1% | -12.1pp ±8.5 (z -1.4) | -21.7% ±13.1 | +nan/-12.1 both |
| Portugal / Campeonato de Portugal — Under | 157 (79 fx) | 1.50 | 64.2% | 58.0% | -6.3pp ±4.9 (z -1.3) | -16.0% ±7.4 | -7.9/-5.4 both |
| Spain / LaLiga — Under | 127 (37 fx) | 1.52 | 66.5% | 75.6% | +9.1pp ±7.0 (z +1.3) | +13.5% ±10.9 | +4.7/+13.8 both |
| USA / MLS — Under | 310 (89 fx) | 1.52 | 65.9% | 71.0% | +5.1pp ±4.1 (z +1.2) | +3.6% ±6.5 | +5.6/+4.1 both |
| Japan / J1 League — Under | 176 (52 fx) | 1.52 | 65.8% | 58.0% | -7.9pp ±6.4 (z -1.2) | -15.0% ±9.9 | -17.2/+9.7 FLIPS |
| Brazil / Brasileiro Serie A — Under | 153 (47 fx) | 1.53 | 64.2% | 71.9% | +7.7pp ±6.2 (z +1.2) | +7.5% ±9.6 | +7.9/+7.3 both |
| Japan / J1 League — Over | 149 (52 fx) | 1.54 | 65.2% | 71.8% | +6.6pp ±5.7 (z +1.2) | +7.1% ±8.9 | +14.6/-12.0 FLIPS |
| Turkiye / 1. Lig — Under | 136 (43 fx) | 1.56 | 63.3% | 55.1% | -8.2pp ±7.0 (z -1.2) | -18.1% ±11.0 | -11.9/-2.6 both |

64 competition×side slices tested (chance: ~1 at |z|≥2.5).

## 7. Weekend vs midweek, kick-off hour (football O/U and 1X2 favourites, odds 1.18–2.2)
| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| Over Sat-Sun | 10893 (5318 fx) | 1.58 | 62.1% | 61.9% | -0.2pp ±0.6 (z -0.3) | -6.2% ±1.0 | +0.6/-0.8 FLIPS |
| Over Mon-Fri | 7843 (3680 fx) | 1.57 | 62.5% | 62.8% | +0.3pp ±0.8 (z +0.3) | -4.9% ±1.2 | +1.1/-0.9 FLIPS |
| Under Sat-Sun | 12206 (5333 fx) | 1.54 | 63.4% | 64.1% | +0.7pp ±0.6 (z +1.1) | -4.3% ±1.0 | -1.0/+1.9 FLIPS |
| Under Mon-Fri | 8938 (3672 fx) | 1.54 | 63.9% | 63.4% | -0.5pp ±0.8 (z -0.6) | -5.8% ±1.2 | -1.1/+0.4 FLIPS |
| fav 1X2 Sat-Sun | 2379 (2379 fx) | 1.58 | 60.7% | 61.4% | +0.7pp ±1.0 (z +0.7) | -4.1% ±1.6 | -0.4/+1.4 FLIPS |
| fav 1X2 Mon-Fri | 1779 (1779 fx) | 1.55 | 62.3% | 64.2% | +2.0pp ±1.1 (z +1.8) | -1.9% ±1.8 | +3.4/+0.2 both |

## 8. Corners and cards: do the teams' own averages beat the house line?


**Corners OVER by (teams' last-10 expected corners − line)**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| -2 to -1 | 192 (192 fx) | 2.61 | 36.3% | 35.9% | -0.4pp ±3.5 (z -0.1) | -7.5% ±9.2 | -5.9/+3.2 FLIPS |
| -1 to 0 | 232 (232 fx) | 2.16 | 44.8% | 44.0% | -0.8pp ±3.2 (z -0.3) | -9.3% ±6.9 | -8.1/+4.2 FLIPS |
| 0 to +1 | 243 (243 fx) | 1.76 | 55.0% | 55.6% | +0.5pp ±3.1 (z +0.2) | -4.8% ±5.6 | -6.2/+5.3 FLIPS |
| +1 to +2 | 199 (199 fx) | 1.51 | 63.9% | 64.3% | +0.5pp ±3.3 (z +0.1) | -4.4% ±5.2 | -5.7/+4.8 FLIPS |

**Corners UNDER by the same gap**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| -2 to -1 | 192 (192 fx) | 1.52 | 63.7% | 64.1% | +0.4pp ±3.5 (z +0.1) | -3.5% ±5.3 | +5.9/-3.2 FLIPS |
| -1 to 0 | 232 (232 fx) | 1.76 | 55.2% | 56.0% | +0.8pp ±3.2 (z +0.3) | -4.5% ±5.7 | +8.1/-4.2 FLIPS |
| 0 to +1 | 243 (243 fx) | 2.16 | 45.0% | 44.4% | -0.5pp ±3.1 (z -0.2) | -8.3% ±6.8 | +6.2/-5.3 FLIPS |
| +1 to +2 | 199 (199 fx) | 2.64 | 36.1% | 35.7% | -0.5pp ±3.3 (z -0.1) | -11.1% ±8.7 | +5.7/-4.8 FLIPS |

**Bookings OVER by (teams' last-10 cards − line)**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| ≤-1.5 | 169 (131 fx) | 4.20 | 20.8% | 17.8% | -3.1pp ±3.3 (z -0.9) | -27.1% ±13.7 | -5.1/-1.0 both |
| -1.5 to -0.5 | 151 (151 fx) | 2.79 | 34.2% | 29.8% | -4.4pp ±3.6 (z -1.2) | -23.7% ±9.9 | -4.1/-4.7 both |
| -0.5 to +0.5 | 152 (152 fx) | 1.85 | 52.2% | 48.7% | -3.5pp ±3.9 (z -0.9) | -14.9% ±7.4 | -1.6/-5.2 both |
| +0.5 to +1.5 | 151 (151 fx) | 1.37 | 70.8% | 66.2% | -4.5pp ±3.8 (z -1.2) | -11.2% ±5.3 | -4.7/-4.4 both |

**Bookings UNDER by the same gap**

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| ≤-1.5 | 169 (131 fx) | 1.21 | 79.2% | 82.2% | +3.1pp ±3.3 (z +0.9) | -0.4% ±4.1 | +5.1/+1.0 both |
| -1.5 to -0.5 | 151 (151 fx) | 1.47 | 65.8% | 70.2% | +4.4pp ±3.6 (z +1.2) | +0.7% ±5.5 | +4.1/+4.7 both |
| -0.5 to +0.5 | 152 (152 fx) | 2.03 | 47.8% | 51.3% | +3.5pp ±3.9 (z +0.9) | -3.6% ±7.9 | +1.6/+5.2 both |
| +0.5 to +1.5 | 151 (151 fx) | 3.29 | 29.2% | 33.8% | +4.5pp ±3.8 (z +1.2) | +1.1% ±12.3 | +4.7/+4.4 both |

## 9. Does our research (team news, absences, form) add to the house price?

1542 researched fixtures in papertrade/research, 102 vetoed; 501 research picks found on the graded tape.

| slice | n | avg odds | house p | actual | actual − house | flat ROI | halves (resid) |
|---|---|---|---|---|---|---|---|
| all research picks | 501 (377 fx) | 1.37 | 70.6% | 69.5% | -1.1pp ±2.3 (z -0.5) | -6.2% ±3.2 | +nan/-1.1 both |
| research p ≤ house p | 339 (276 fx) | 1.35 | 71.3% | 68.7% | -2.6pp ±2.7 (z -0.9) | -8.2% ±3.7 | +nan/-2.6 both |
| research 0–5pp above house | 146 (118 fx) | 1.37 | 70.2% | 69.9% | -0.4pp ±4.2 (z -0.1) | -5.5% ±6.0 | +nan/-0.4 both |
| 5–10pp above | 11 (10 fx) | 1.52 | 62.6% | 81.8% | +19.2pp ±11.4 (z +1.7) | +22.3% ±18.8 | +nan/+19.2 FLIPS |
| 10–15pp above | 4 (3 fx) | 1.89 | 48.9% | 75.0% | +26.1pp ±22.6 (z +1.2) | +38.5% ±43.2 | +nan/+26.1 FLIPS |
| >15pp above (R5 says skip) | 1 (1 fx) | 1.81 | 51.8% | 100.0% | +48.2pp ±0.0 (z +481826000.0) | +81.0% ±0.0 | +nan/+48.2 FLIPS |
| VETOED fixtures — all short-priced main markets | 807 (63 fx) | 1.57 | 61.7% | 59.9% | -1.8pp ±1.2 (z -1.5) | -8.7% ±1.7 | +nan/-1.8 both |
| researched, not vetoed — same markets | 8921 (653 fx) | 1.57 | 61.8% | 62.2% | +0.4pp ±0.4 (z +1.1) | -5.9% ±0.5 | +nan/+0.4 FLIPS |
| VETOED fixtures — the 1X2 favourite | 34 (34 fx) | 1.37 | 70.9% | 64.7% | -6.2pp ±8.1 (z -0.8) | -13.2% ±11.3 | +nan/-6.2 both |
| not vetoed — the 1X2 favourite | 255 (255 fx) | 1.45 | 67.0% | 67.5% | +0.4pp ±2.8 (z +0.1) | -4.8% ±4.3 | +nan/+0.4 FLIPS |
