# What actually affects what — factor study

Data: 29,636 matches (19 European leagues, 2022-23 to 2026-27; closing odds, shots, corners, cards, fouls; xG for 2026-27 only), plus NBA/WNBA/MLB closing lines. Every factor is measured from matches played **before** kick-off. Train = before July 2025, test = July 2025 onward.

## How to read this

- **Raw effect** = how much the outcome moves per 1 standard deviation of the factor, ignoring the odds. This is the question "does attacking form affect goals?".
- **Beyond the price** = the same, after accounting for what the betting market already expects. This is the question that matters for betting: if the market already knows it, the factor gives no edge.
- **Out-of-sample gain** = how much the factor improves predictions on games the model never saw (×10⁻⁴ nats per match). Anything ≤0.5 is noise.
- For corners and cards there is no market price in this data, so "beyond the price" means beyond a baseline built from the goals market (expected goals for both sides, home/away, league average). SportyBet's own corner/card lines may already contain some of these factors.

## Headline answers

- **Does attacking form (goals scored, last 10) affect a team's goals?** Yes, strongly — but the market already prices it. Raw: +17.9% per SD (t=+49). Beyond the price: +0.2% (t=+0.5), out-of-sample +0.03 → **already in the price** (no extra information).
- **Shots on target form** is a better predictor than goals form, and a little of it is *not* fully priced. Raw: +19.5% per SD (t=+53). Beyond the price: +0.9% (t=+2.9), out-of-sample +1.02 → **adds information beyond the price**.
- **Does expected goals (xG) affect goals scored?** Within the same match, xG and goals correlate 0.59 (n=2,948) — xG explains a lot of what happened, but goals are noisy. As a *predictor*, a team's last-5 xG correlates 0.21 with its next-match goals vs 0.18 for last-5 goals and 0.23 for last-10 shots on target; the market price alone correlates 0.38. Beyond the price, xG adds +1.7% per SD (t=+1.2, n=2,544, one season only) → not significant yet.
- **Does table position affect goals scored?** Yes raw (top sides score more), but it is fully in the price. Raw: -14.7% per SD (t=-40). Beyond the price: -0.2% (t=-0.4), out-of-sample +0.03 → **already in the price** (no extra information).
- **Recent goals conceded:** the market slightly *over-reacts* — a side that has just leaked goals concedes a bit less than priced next time. Raw: +8.8% per SD (t=+23). Beyond the price: -0.9% (t=-2.7), out-of-sample +1.06 → **adds information beyond the price**.
- **Finishing luck** (goals above what shots on target would predict): there is a faint hint that the market over-rates hot finishers (mean reversion), but on its own it does not survive the out-of-sample test. Raw: +8.2% per SD (t=+21). Beyond the price: -0.7% (t=-2.1), out-of-sample +0.32 → **already in the price** (no extra information).
- **Points form (last 5)** has no information beyond the price. Raw: +13.0% per SD (t=+33). Beyond the price: -0.0% (t=-0.0), out-of-sample -0.30 → **already in the price** (no extra information).
- **Head-to-head goals** has no information beyond the price. Raw: +5.0% per SD (t=+10). Beyond the price: +0.1% (t=+0.2), out-of-sample -0.19 → **already in the price** (no extra information).
- **Rest days** don't matter for goals in this data. Raw: +0.2% per SD (t=+0). Beyond the price: +0.1% (t=+0.2), out-of-sample -0.09 → **already in the price** (no extra information).
- **Does table position affect corners conceded?** Yes: lower-placed sides concede more corners, and some of it survives the baseline. Raw: +9.6% per SD (t=+37). Beyond the price: +1.1% (t=+3.9), out-of-sample +3.41 → **adds information beyond the price**.
- **Corners-conceded form** carries the most signal for corners conceded. Raw: +9.6% per SD (t=+39). Beyond the price: +2.2% (t=+9.1), out-of-sample +4.13 → **adds information beyond the price**.
- **Corners-won form** predicts corners won. Raw: +10.0% per SD (t=+41). Beyond the price: +1.7% (t=+6.8), out-of-sample +7.30 → **adds information beyond the price**.
- **Goals form and corners:** once expected goals are known, sides that have been *scoring* more win *fewer* corners — leading teams sit back. Raw: +8.3% per SD (t=+34). Beyond the price: -2.1% (t=-7.7), out-of-sample +3.73 → **adds information beyond the price**.
- **The referee** is the biggest single card factor. Raw: +6.7% per SD (t=+14). Beyond the price: +6.4% (t=+12.9), out-of-sample +33.87 → **adds information beyond the price**.
- **A team's own card history** predicts its cards. Raw: +12.4% per SD (t=+42). Beyond the price: +5.2% (t=+18.1), out-of-sample +17.72 → **adds information beyond the price**.
- **Table position and cards:** lower-placed sides, and sides facing a stronger opponent, collect more cards. Raw: -4.1% per SD (t=-14). Beyond the price: -5.1% (t=-17.3), out-of-sample +15.87 → **adds information beyond the price**.

## Combined models (all factors together), out of sample

| Outcome | Factors | Train / test matches | OOS gain ×10⁻⁴ | Typical move | Does the move come true? (test set: model multiplier → actual/baseline, by quintile) |
|---|---|---|---|---|---|
| Team goals scored | sotf10, o_sota10, o_ga5, fin10, o_rank | 41,810 / 17,462 | +4.24 | ±1.5% | 0.98→0.96 · 0.99→0.98 · 1.00→1.00 · 1.01→0.99 · 1.02→1.04 |
| Team corners won | cf10, o_ca10, gf10, o_rank, rank | 41,792 / 17,462 | +17.58 | ±3.2% | 0.95→0.96 · 0.98→0.97 · 1.00→1.01 · 1.01→0.99 · 1.04→1.03 |
| Team corners conceded | ca10, o_cf10, sa10, rank, ppg | 41,792 / 17,462 | +11.35 | ±3.1% | 0.96→0.96 · 0.98→1.00 · 1.00→0.99 · 1.01→0.99 · 1.04→1.03 |
| Team yellow cards | cards10, fouls10, o_fouls10, ref_y, rank, o_rank, pts5, o_pts5 | 41,794 / 17,462 | +69.89 | ±9.2% | 0.87→0.88 · 0.95→0.94 · 0.99→0.99 · 1.04→1.03 · 1.13→1.09 |

Coefficients (rate multiplier per 1 SD, t-stat, fitted on the training period):

- **Team goals scored**: own shots on target, last 10 +0.9% (t=+2.4); opponent SoT conceded, last 10 +0.9% (t=+1.7); opponent goals conceded, last 5 -1.1% (t=-2.3); finishing luck (goals - 0.3xSoT), last 10 -0.9% (t=-2.2); opponent table position -0.1% (t=-0.1)
- **Team corners won**: own corners won, last 10 +2.2% (t=+7.3); opponent corners conceded, last 10 +2.1% (t=+6.9); own goals scored, last 10 -1.6% (t=-4.4); opponent table position -0.1% (t=-0.2); own table position (0 top, 1 bottom) +1.2% (t=+3.0)
- **Team corners conceded**: corners conceded, last 10 +1.7% (t=+4.7); opponent corners won, last 10 +2.3% (t=+7.3); shots conceded, last 10 +1.4% (t=+3.7); own table position (0 top, 1 bottom) -2.3% (t=-2.8); own season points per game -3.0% (t=-3.6)
- **Team yellow cards**: own yellows, last 10 +4.3% (t=+10.8); own fouls, last 10 +2.3% (t=+5.5); opponent fouls, last 10 -1.3% (t=-3.5); referee avg yellows, last 15 games +6.5% (t=+10.8); own table position (0 top, 1 bottom) +1.4% (t=+3.1); opponent table position -4.1% (t=-9.2); form: points per game, last 5 -2.9% (t=-6.9); opponent points per game, last 5 +1.8% (t=+4.0)

## Quintile tables (all seasons): factor level → average outcome → actual vs baseline expectation

Actual/expected = 1.00 means the price/baseline already accounts for that factor level.

**own goals scored, last 10 → team goals scored**: Q1: 0.68 → 1.11 (1.002) | Q2: 1.01 → 1.19 (0.991) | Q3: 1.25 → 1.27 (0.992) | Q4: 1.49 → 1.39 (1.007) | Q5: 2.05 → 1.71 (1.004)

**own shots on target, last 10 → team goals scored**: Q1: 2.83 → 1.08 (0.985) | Q2: 3.57 → 1.19 (0.986) | Q3: 4.10 → 1.28 (0.992) | Q4: 4.67 → 1.43 (1.014) | Q5: 5.88 → 1.76 (1.013)

**own table position (0 top, 1 bottom) → team goals scored**: Q1: 0.07 → 1.74 (1.001) | Q2: 0.28 → 1.44 (1.001) | Q3: 0.49 → 1.28 (1.002) | Q4: 0.70 → 1.20 (0.994) | Q5: 0.92 → 1.13 (1.001)

**form: points per game, last 5 → team goals scored**: Q1: 0.40 → 1.15 (0.988) | Q2: 0.90 → 1.25 (1.012) | Q3: 1.20 → 1.28 (0.996) | Q4: 1.57 → 1.37 (1.001) | Q5: 2.29 → 1.62 (0.998)

**opponent goals conceded, last 5 → team goals scored**: Q1: 0.48 → 1.15 (0.998) | Q2: 0.91 → 1.28 (1.012) | Q3: 1.20 → 1.34 (1.010) | Q4: 1.49 → 1.38 (0.997) | Q5: 2.13 → 1.51 (0.989)

**finishing luck (goals - 0.3xSoT), last 10 → team goals scored**: Q1: -0.38 → 1.26 (1.011) | Q2: -0.11 → 1.27 (0.999) | Q3: 0.06 → 1.33 (1.005) | Q4: 0.24 → 1.38 (1.000) | Q5: 0.56 → 1.54 (0.987)

**own goals conceded, last 10 → team goals conceded**: Q1: 0.73 → 1.13 (0.995) | Q2: 1.05 → 1.28 (1.017) | Q3: 1.25 → 1.34 (1.010) | Q4: 1.49 → 1.40 (0.997) | Q5: 1.97 → 1.55 (0.990)

**own corners won, last 10 → team corners won**: Q1: 3.36 → 4.31 (0.975) | Q2: 4.17 → 4.60 (0.990) | Q3: 4.75 → 4.83 (1.003) | Q4: 5.38 → 5.06 (1.008) | Q5: 6.55 → 5.60 (1.015)

**opponent table position → team corners won**: Q1: 0.07 → 4.14 (0.985) | Q2: 0.28 → 4.67 (0.994) | Q3: 0.49 → 5.05 (1.011) | Q4: 0.70 → 5.13 (0.995) | Q5: 0.92 → 5.45 (1.010)

**own table position (0 top, 1 bottom) → team corners conceded**: Q1: 0.07 → 4.14 (0.985) | Q2: 0.28 → 4.67 (0.994) | Q3: 0.49 → 5.05 (1.011) | Q4: 0.70 → 5.13 (0.995) | Q5: 0.92 → 5.45 (1.010)

**corners conceded, last 10 → team corners conceded**: Q1: 3.36 → 4.21 (0.965) | Q2: 4.26 → 4.71 (0.998) | Q3: 4.80 → 4.93 (1.003) | Q4: 5.38 → 5.10 (1.005) | Q5: 6.47 → 5.48 (1.021)

**referee avg yellows, last 15 games → team yellow cards**: Q1: 2.86 → 1.72 (0.903) | Q2: 3.38 → 1.85 (0.972) | Q3: 3.74 → 1.89 (0.991) | Q4: 4.12 → 1.96 (1.027) | Q5: 4.78 → 2.09 (1.088)

**own yellows, last 10 → team yellow cards**: Q1: 1.29 → 1.74 (0.930) | Q2: 1.71 → 1.88 (0.960) | Q3: 2.00 → 2.04 (0.998) | Q4: 2.29 → 2.14 (1.015) | Q5: 2.84 → 2.40 (1.064)

**opponent table position → team yellow cards**: Q1: 0.07 → 2.18 (1.084) | Q2: 0.28 → 2.14 (1.036) | Q3: 0.49 → 2.02 (0.977) | Q4: 0.70 → 1.99 (0.961) | Q5: 0.92 → 1.95 (0.949)

## Full table (each factor on its own)

| Outcome | Factor | n | Corr | Raw / SD | t | Beyond price / SD | t | OOS ×10⁻⁴ | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Team goals scored | market goal expectation | 59,272 | +0.373 | +32.0% | +100.7 | +0.9% | +3.0 | +0.26 | **already in the price** (no extra information) |
| Team goals scored | own goals scored, last 5 | 56,947 | +0.166 | +15.0% | +40.0 | +0.0% | +0.0 | -0.11 | **already in the price** (no extra information) |
| Team goals scored | own goals scored, last 10 | 56,947 | +0.199 | +17.9% | +48.6 | +0.2% | +0.5 | +0.03 | **already in the price** (no extra information) |
| Team goals scored | own goals at this venue, last 5 | 54,651 | +0.190 | +17.3% | +45.5 | +0.3% | +0.9 | +0.07 | **already in the price** (no extra information) |
| Team goals scored | own shots, last 10 | 56,947 | +0.201 | +18.6% | +48.6 | +0.9% | +2.9 | +1.16 | **adds information beyond the price** |
| Team goals scored | own shots on target, last 10 | 56,947 | +0.215 | +19.5% | +52.8 | +0.9% | +2.9 | +1.02 | **adds information beyond the price** |
| Team goals scored | own xG, last 5 | 2,544 | +0.209 | +17.9% | +10.3 | +1.7% | +1.2 |  | too few matches to test out of sample |
| Team goals scored | finishing luck (goals - 0.3xSoT), last 10 | 56,947 | +0.090 | +8.2% | +21.0 | -0.7% | -2.1 | +0.32 | **already in the price** (no extra information) |
| Team goals scored | goals minus xG, last 5 | 2,544 | -0.003 | -0.3% | -0.1 | -0.4% | -0.3 |  | too few matches to test out of sample |
| Team goals scored | opponent goals conceded, last 10 | 56,947 | +0.128 | +11.8% | +30.9 | -0.3% | -0.9 | +0.06 | **already in the price** (no extra information) |
| Team goals scored | opponent SoT conceded, last 10 | 56,947 | +0.147 | +13.7% | +35.6 | +0.5% | +1.3 | +0.27 | **already in the price** (no extra information) |
| Team goals scored | opponent xG conceded, last 5 | 2,544 | +0.120 | +10.5% | +6.3 | +1.7% | +1.1 |  | too few matches to test out of sample |
| Team goals scored | form: points per game, last 5 | 56,947 | +0.138 | +13.0% | +33.2 | -0.0% | -0.0 | -0.30 | **already in the price** (no extra information) |
| Team goals scored | own season points per game | 50,102 | +0.195 | +18.3% | +43.9 | +0.1% | +0.2 | -0.03 | **already in the price** (no extra information) |
| Team goals scored | own table position (0 top, 1 bottom) | 50,102 | -0.178 | -14.7% | -39.6 | -0.2% | -0.4 | +0.03 | **already in the price** (no extra information) |
| Team goals scored | opponent table position | 50,102 | +0.126 | +11.9% | +28.6 | -0.5% | -1.4 | +0.34 | **already in the price** (no extra information) |
| Team goals scored | opponent season points per game | 50,102 | -0.133 | -11.4% | -30.0 | +0.4% | +1.0 | +0.15 | **already in the price** (no extra information) |
| Team goals scored | own rest days | 58,807 | +0.002 | +0.2% | +0.5 | +0.1% | +0.2 | -0.09 | **already in the price** (no extra information) |
| Team goals scored | opponent rest days | 58,807 | +0.009 | +0.7% | +2.2 | +0.4% | +1.4 | +0.08 | **already in the price** (no extra information) |
| Team goals scored | avg total goals, last 2-4 H2H | 33,374 | +0.055 | +5.0% | +9.9 | +0.1% | +0.2 | -0.19 | **already in the price** (no extra information) |
| Team goals scored | matches played this season | 59,272 | -0.002 | -0.1% | -0.4 | +0.3% | +0.7 | -0.57 | **already in the price** (no extra information) |
| Team goals conceded | own goals conceded, last 5 | 56,947 | +0.097 | +8.8% | +23.3 | -0.9% | -2.7 | +1.06 | **adds information beyond the price** |
| Team goals conceded | own goals conceded, last 10 | 56,947 | +0.128 | +11.8% | +30.9 | -0.3% | -0.9 | +0.06 | **already in the price** (no extra information) |
| Team goals conceded | shots conceded, last 10 | 56,947 | +0.144 | +13.6% | +34.6 | +0.7% | +1.9 | +0.54 | **already in the price** (no extra information) |
| Team goals conceded | shots on target conceded, last 10 | 56,947 | +0.147 | +13.7% | +35.6 | +0.5% | +1.3 | +0.27 | **already in the price** (no extra information) |
| Team goals conceded | xG conceded, last 5 | 2,544 | +0.120 | +10.5% | +6.3 | +1.7% | +1.1 |  | too few matches to test out of sample |
| Team goals conceded | opponent goals scored, last 10 | 56,947 | +0.199 | +17.9% | +48.6 | +0.2% | +0.5 | +0.03 | **already in the price** (no extra information) |
| Team goals conceded | own table position (0 top, 1 bottom) | 50,102 | +0.126 | +11.9% | +28.6 | -0.5% | -1.4 | +0.34 | **already in the price** (no extra information) |
| Team goals conceded | opponent table position | 50,102 | -0.178 | -14.7% | -39.6 | -0.2% | -0.4 | +0.03 | **already in the price** (no extra information) |
| Team goals conceded | form: points per game, last 5 | 56,947 | -0.094 | -8.2% | -22.7 | +0.3% | +0.7 | +0.08 | **already in the price** (no extra information) |
| Team goals conceded | own rest days | 58,807 | +0.009 | +0.7% | +2.2 | +0.4% | +1.4 | +0.08 | **already in the price** (no extra information) |
| Team goals conceded | avg total goals, last 2-4 H2H | 33,374 | +0.055 | +5.0% | +9.9 | +0.1% | +0.2 | -0.19 | **already in the price** (no extra information) |
| Team corners won | market goal expectation | 59,254 | +0.347 | +19.5% | +90.3 | -5.5% | -5.9 | +3.31 | **adds information beyond the price** |
| Team corners won | own corners won, last 10 | 56,929 | +0.170 | +10.0% | +40.7 | +1.7% | +6.8 | +7.30 | **adds information beyond the price** |
| Team corners won | own shots, last 10 | 56,929 | +0.160 | +9.4% | +37.9 | -0.5% | -1.7 | -0.48 | **already in the price** (no extra information) |
| Team corners won | opponent corners conceded, last 10 | 56,929 | +0.161 | +9.6% | +39.0 | +2.2% | +9.1 | +4.13 | **adds information beyond the price** |
| Team corners won | own goals scored, last 10 | 56,929 | +0.144 | +8.3% | +34.0 | -2.1% | -7.7 | +3.73 | **adds information beyond the price** |
| Team corners won | form: points per game, last 5 | 56,929 | +0.113 | +6.7% | +26.8 | -1.1% | -4.6 | -1.81 | **already in the price** (no extra information) |
| Team corners won | own table position (0 top, 1 bottom) | 50,084 | -0.143 | -7.9% | -31.9 | +1.8% | +6.3 | +0.38 | **already in the price** (no extra information) |
| Team corners won | opponent table position | 50,084 | +0.160 | +9.6% | +36.6 | +1.1% | +3.9 | +3.41 | **adds information beyond the price** |
| Team corners won | opponent season points per game | 50,084 | -0.170 | -9.5% | -38.7 | -1.5% | -5.2 | +3.16 | **adds information beyond the price** |
| Team corners won | own rest days | 58,789 | -0.002 | -0.1% | -0.4 | -0.1% | -0.3 | -0.68 | **already in the price** (no extra information) |
| Team corners conceded | corners conceded, last 10 | 56,929 | +0.161 | +9.6% | +39.0 | +2.2% | +9.1 | +4.13 | **adds information beyond the price** |
| Team corners conceded | shots conceded, last 10 | 56,929 | +0.160 | +9.6% | +39.2 | +1.9% | +7.6 | -2.28 | **already in the price** (no extra information) |
| Team corners conceded | opponent corners won, last 10 | 56,929 | +0.170 | +10.0% | +40.7 | +1.7% | +6.8 | +7.30 | **adds information beyond the price** |
| Team corners conceded | own goals conceded, last 10 | 56,929 | +0.136 | +8.0% | +32.8 | +0.8% | +3.2 | -0.38 | **already in the price** (no extra information) |
| Team corners conceded | own table position (0 top, 1 bottom) | 50,084 | +0.160 | +9.6% | +36.6 | +1.1% | +3.9 | +3.41 | **adds information beyond the price** |
| Team corners conceded | opponent table position | 50,084 | -0.143 | -7.9% | -31.9 | +1.8% | +6.3 | +0.38 | **already in the price** (no extra information) |
| Team corners conceded | form: points per game, last 5 | 56,929 | -0.123 | -6.9% | -29.6 | -1.0% | -3.9 | +0.64 | **adds information beyond the price** |
| Team corners conceded | own season points per game | 50,084 | -0.170 | -9.5% | -38.7 | -1.5% | -5.2 | +3.16 | **adds information beyond the price** |
| Team yellow cards | own yellows, last 10 | 56,931 | +0.175 | +12.4% | +42.1 | +5.2% | +18.1 | +17.72 | **adds information beyond the price** |
| Team yellow cards | opponent yellows, last 10 | 56,931 | +0.109 | +7.6% | +26.2 | +0.4% | +1.3 | -0.12 | **already in the price** (no extra information) |
| Team yellow cards | own fouls, last 10 | 56,931 | +0.156 | +11.0% | +37.8 | +4.2% | +14.2 | +14.95 | **adds information beyond the price** |
| Team yellow cards | referee avg yellows, last 15 games | 19,456 | +0.094 | +6.7% | +13.5 | +6.4% | +12.9 | +33.87 | **adds information beyond the price** |
| Team yellow cards | own table position (0 top, 1 bottom) | 50,086 | +0.064 | +4.5% | +14.3 | +4.1% | +13.3 | +11.51 | **adds information beyond the price** |
| Team yellow cards | opponent table position | 50,086 | -0.061 | -4.1% | -13.7 | -5.1% | -17.3 | +15.87 | **adds information beyond the price** |
| Team yellow cards | form: points per game, last 5 | 56,931 | -0.069 | -4.6% | -16.3 | -4.3% | -15.3 | +18.21 | **adds information beyond the price** |
| Team yellow cards | avg total goals, last 2-4 H2H | 33,366 | -0.040 | -2.7% | -7.3 | -0.6% | -1.4 | +0.38 | **already in the price** (no extra information) |

## US sports: does recent form beat the closing line?

Residual = actual − closing line (total points/runs, or home margin + spread). Slope = points/runs per 1 SD of the factor. A real edge needs |t|>2 **and** the same sign in both halves. MLB "margin" rows use the ±1.5 run line, which is not a margin forecast, so treat them as uninformative. Average residuals ignore the over/under juice, which ESPN does not store.

| Sport | Target | Factor | n | Slope | t | Early half | Late half | Avg residual |
|---|---|---|---|---|---|---|---|---|
| NBA | total | both teams' recent totals vs line | 2,563 | -0.31 | -0.9 | -0.32 | -0.29 | +0.55 |
| NBA | total | either team on a back-to-back | 2,625 | +0.09 | +0.3 | -0.29 | +0.47 | +0.58 |
| NBA | margin | recent results vs spread (home − away) | 2,563 | +0.54 | +2.0 | +0.09 | +0.97 | -0.12 |
| NBA | margin | recent margin (home − away) | 2,563 | +0.67 | +2.4 | +0.39 | +0.95 | -0.12 |
| NBA | margin | rest days (home − away) | 2,625 | +0.16 | +0.6 | +0.55 | -0.23 | -0.13 |
| WNBA | total | both teams' recent totals vs line | 614 | -0.72 | -1.0 | -1.26 | -0.42 | +0.95 |
| WNBA | total | either team on a back-to-back | 649 | +0.39 | +0.6 | +0.73 | -0.06 | +0.94 |
| WNBA | margin | recent results vs spread (home − away) | 614 | +0.41 | +0.8 | +0.65 | +0.04 | +0.56 |
| WNBA | margin | recent margin (home − away) | 614 | -0.32 | -0.6 | -0.64 | +0.06 | +0.56 |
| WNBA | margin | rest days (home − away) | 649 | +0.08 | +0.2 | -0.50 | +0.61 | +0.45 |
| MLB | total | both teams' recent totals vs line | 4,853 | +0.03 | +0.4 | +0.08 | -0.03 | +0.49 |
| MLB | total | either team on a back-to-back | 4,861 | -0.14 | -2.1 | -0.21 | -0.06 | +0.48 |
| MLB | margin | recent results vs spread (home − away) | 4,853 | +0.08 | +1.2 | +0.12 | +0.04 | +0.01 |
| MLB | margin | recent margin (home − away) | 4,853 | -0.09 | -1.4 | -0.02 | -0.18 | +0.01 |
| MLB | margin | rest days (home − away) | 4,861 | +0.16 | +2.4 | +0.12 | +0.19 | +0.02 |
