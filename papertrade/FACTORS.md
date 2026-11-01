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

<!-- PART2 -->
## Part 2 — other markets and other sports

Same test: each factor is added on top of the price (football: market expectation; US sports: closing line; tape: SportyBet's own line). "Effect" is per 1 SD for continuous factors, or the effect of the flag being on. A factor counts only if |t|≥2, the sign is the same in both halves of the data, and it improves out-of-sample prediction.

**Multiple-testing warning:** 232 factor×market tests were run. At |t|≥2, about 11 would pass by chance alone, and about half of those also keep their sign across both halves. So treat the |t| 2-3 rows as unconfirmed; only |t|≥3 rows are strong evidence.

### What survives (all markets, all sports)

| Market | Factor | n | Effect | t | Out-of-sample |
|---|---|---|---|---|---|
| Total yellow cards | midweek (Tue-Thu) | 29,628 | -5.4% | -5.9 | +4.4 |
| Total corners | away points form (last 5) | 28,451 | -0.9% | -4.4 | +1.1 |
| Total yellow cards | two top-15% sides | 29,628 | +8.8% | +4.0 | +1.4 |
| Total yellow cards | home side bottom-20% in run-in | 29,628 | -5.0% | -4.0 | +0.5 |
| Total yellow cards | home side played ≤3 days ago | 29,628 | -3.5% | -3.7 | +2.2 |
| Total yellow cards | away side played ≤3 days ago | 29,628 | -3.3% | -3.3 | +3.1 |
| 1st-half goals | both sides' shots on target form | 28,244 | +1.6% | +3.1 | +1.1 |
| Total goals | both sides' shots on target form | 28,252 | +1.0% | +3.0 | +2.5 |
| BTTS (both teams score) | table-position gap | 24,995 | -0.032 log-odds | -2.5 | +1.3 |
| NBA home margin vs closing spread | recent net rating (home − away) | 2,563 | +0.67 pts/runs | +2.5 | +0.59 pts² MSE |
| Home win | home points form (last 5) | 28,487 | +0.031 log-odds | +2.5 | +1.5 |
| Total corners | H2H draw rate (last 3-6) | 12,422 | +0.8% | +2.4 | +3.6 |
| Basketball margin vs SportyBet spread (all leagues) | rest days (home − away) | 1,153 | -0.89 pts/runs | -2.3 | +1.13 pts² MSE |
| NBA home win vs closing moneyline | recent net rating (home − away) | 2,559 | +0.110 log-odds | +2.2 | +11.7 |
| Total yellow cards | table-position gap | 24,987 | -0.8% | -2.2 | +0.8 |
| MLB total vs closing line | away team's road-trip length | 4,934 | -0.14 pts/runs | -2.2 | +0.01 pts² MSE |
| Total yellow cards | referee avg goals (last 20) | 9,397 | +1.2% | +2.1 | +1.4 |
| WNBA home win vs closing moneyline | first 4 rounds of season | 660 | -0.505 log-odds | -2.1 |  |
| Total corners | table-position gap | 24,986 | +0.5% | +2.1 | +1.3 |
| 1st-half goals | home points form (last 5) | 28,479 | +1.0% | +2.0 | +1.2 |

### Total goals

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| both sides' shots on target form | 28,252 | +1.0% | +3.0 | +0.007 | +0.014 | +2.5 | **real, beyond the price** |
| home points form (last 5) | 28,487 | +0.5% | +1.5 | +0.003 | +0.007 | +0.6 | no effect beyond the price |
| last 15% of season (n on=5111) | 29,636 | +1.1% | +1.3 | +0.021 | +0.003 | -1.9 | no effect beyond the price |
| home side played ≤3 days ago (n on=3115) | 29,636 | +1.0% | +0.9 | +0.019 | +0.001 | -0.7 | no effect beyond the price |
| table-position gap | 24,995 | -0.3% | -0.9 | +0.001 | -0.008 | +0.3 | no effect beyond the price |
| away points form (last 5) | 28,460 | -0.3% | -0.8 | -0.007 | +0.002 | -1.3 | no effect beyond the price |
| referee avg goals (last 20) | 9,397 | +0.5% | +0.8 | +0.008 | -0.001 | -0.5 | no effect beyond the price |
| home side newly promoted (n on=4778) | 22,387 | -0.7% | -0.7 | -0.013 | -0.001 | -0.0 | no effect beyond the price |
| home side bottom-20% in run-in (n on=1667) | 29,636 | +1.1% | +0.7 | +0.055 | -0.030 | -4.0 | no effect beyond the price |
| away side newly promoted (n on=4776) | 22,387 | +0.7% | +0.7 | +0.005 | +0.009 | -0.2 | no effect beyond the price |
| midweek (Tue-Thu) (n on=3443) | 29,636 | -0.7% | -0.7 | +0.002 | -0.018 | -0.1 | no effect beyond the price |
| two bottom-20% sides, 2nd half of season (n on=552) | 29,636 | -1.4% | -0.5 | +0.030 | -0.057 | -0.2 | no effect beyond the price |
| H2H draw rate (last 3-6) | 12,425 | +0.3% | +0.5 | +0.004 | +0.001 | +0.1 | no effect beyond the price |
| two top-15% sides (n on=569) | 29,636 | +1.1% | +0.4 | +0.021 | -0.000 | +0.0 | no effect beyond the price |
| away side played ≤3 days ago (n on=3033) | 29,636 | +0.5% | +0.4 | +0.020 | -0.012 | -0.3 | no effect beyond the price |
| rest days (home − away) | 29,361 | -0.1% | -0.4 | +0.001 | -0.003 | -0.1 | no effect beyond the price |
| first 4 rounds of season (n on=4583) | 29,636 | -0.4% | -0.4 | -0.015 | +0.010 | -0.6 | no effect beyond the price |
| referee home-win rate (last 30) | 8,621 | +0.2% | +0.4 | +0.005 | -0.002 | -1.4 | no effect beyond the price |
| December/January (n on=5540) | 29,636 | -0.2% | -0.3 | -0.015 | +0.009 | -0.1 | no effect beyond the price |
| August/September (n on=6414) | 29,636 | -0.1% | -0.1 | -0.009 | +0.008 | -0.1 | no effect beyond the price |

### 1st-half goals

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| both sides' shots on target form | 28,244 | +1.6% | +3.1 | +0.020 | +0.010 | +1.1 | **real, beyond the price** |
| away points form (last 5) | 28,452 | -1.1% | -2.2 | -0.016 | -0.007 | -0.4 | real in-sample, fails out of sample |
| home points form (last 5) | 28,479 | +1.0% | +2.0 | +0.008 | +0.012 | +1.2 | **real, beyond the price** |
| home side played ≤3 days ago (n on=3115) | 29,628 | +2.4% | +1.4 | +0.043 | +0.003 | -1.1 | no effect beyond the price |
| last 15% of season (n on=5110) | 29,628 | +1.7% | +1.2 | +0.024 | +0.011 | -2.4 | no effect beyond the price |
| two top-15% sides (n on=568) | 29,628 | +4.2% | +1.2 | +0.034 | +0.049 | +0.2 | no effect beyond the price |
| two bottom-20% sides, 2nd half of season (n on=552) | 29,628 | -4.3% | -1.1 | +0.017 | -0.106 | +0.3 | no effect beyond the price |
| December/January (n on=5538) | 29,628 | -1.4% | -1.1 | -0.031 | +0.001 | +0.2 | no effect beyond the price |
| H2H draw rate (last 3-6) | 12,422 | +0.8% | +1.0 | +0.013 | +0.002 | -0.2 | no effect beyond the price |
| away side played ≤3 days ago (n on=3032) | 29,628 | +1.6% | +1.0 | +0.029 | +0.002 | +0.2 | no effect beyond the price |
| referee avg goals (last 20) | 9,397 | +0.9% | +1.0 | +0.014 | +0.001 | -2.1 | no effect beyond the price |
| home side bottom-20% in run-in (n on=1667) | 29,628 | +1.5% | +0.7 | +0.067 | -0.035 | -2.5 | no effect beyond the price |
| away side newly promoted (n on=4775) | 22,382 | +1.0% | +0.7 | +0.013 | +0.006 | -0.1 | no effect beyond the price |
| home side newly promoted (n on=4778) | 22,382 | +0.8% | +0.5 | +0.001 | +0.014 | +0.1 | no effect beyond the price |
| referee home-win rate (last 30) | 8,621 | +0.5% | +0.5 | +0.007 | +0.001 | -1.7 | no effect beyond the price |
| first 4 rounds of season (n on=4583) | 29,628 | -0.7% | -0.5 | -0.008 | -0.007 | +0.1 | no effect beyond the price |
| rest days (home − away) | 29,353 | -0.2% | -0.5 | -0.001 | -0.003 | -0.2 | no effect beyond the price |
| August/September (n on=6413) | 29,628 | +0.5% | +0.4 | +0.004 | +0.004 | -0.1 | no effect beyond the price |
| table-position gap | 24,987 | -0.1% | -0.2 | +0.002 | -0.005 | -0.2 | no effect beyond the price |
| midweek (Tue-Thu) (n on=3442) | 29,628 | +0.0% | +0.0 | +0.027 | -0.031 | -1.5 | no effect beyond the price |

### BTTS (both teams score)

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| table-position gap | 24,995 | -0.032 log-odds | -2.5 | -0.028 | -0.037 | +1.3 | **real, beyond the price** |
| first 4 rounds of season (n on=4583) | 29,636 | -0.081 log-odds | -2.5 | -0.110 | -0.033 | -1.2 | real in-sample, fails out of sample |
| August/September (n on=6414) | 29,636 | -0.048 log-odds | -1.7 | -0.087 | +0.008 | -1.5 | no effect beyond the price |
| December/January (n on=5540) | 29,636 | +0.049 log-odds | +1.6 | +0.053 | +0.042 | -0.3 | no effect beyond the price |
| away points form (last 5) | 28,460 | -0.016 log-odds | -1.4 | -0.036 | +0.003 | -1.3 | no effect beyond the price |
| referee avg goals (last 20) | 9,397 | +0.028 log-odds | +1.3 | +0.039 | +0.016 | +0.2 | no effect beyond the price |
| two top-15% sides (n on=569) | 29,636 | +0.106 log-odds | +1.2 | +0.075 | +0.139 | +0.5 | no effect beyond the price |
| home side played ≤3 days ago (n on=3115) | 29,636 | +0.045 log-odds | +1.2 | +0.055 | +0.035 | -0.4 | no effect beyond the price |
| home side newly promoted (n on=4778) | 22,387 | -0.038 log-odds | -1.2 | -0.077 | +0.001 | -1.7 | no effect beyond the price |
| away side played ≤3 days ago (n on=3033) | 29,636 | +0.042 log-odds | +1.1 | +0.055 | +0.031 | -1.1 | no effect beyond the price |
| last 15% of season (n on=5111) | 29,636 | +0.033 log-odds | +1.0 | +0.069 | -0.003 | -0.2 | no effect beyond the price |
| both sides' shots on target form | 28,252 | +0.012 log-odds | +1.0 | -0.012 | +0.039 | +0.3 | no effect beyond the price |
| referee home-win rate (last 30) | 8,621 | +0.021 log-odds | +1.0 | +0.005 | +0.043 | +0.8 | no effect beyond the price |
| home points form (last 5) | 28,487 | +0.012 log-odds | +1.0 | -0.007 | +0.031 | +0.3 | no effect beyond the price |
| home side bottom-20% in run-in (n on=1667) | 29,636 | +0.040 log-odds | +0.8 | +0.116 | -0.031 | -2.0 | no effect beyond the price |
| midweek (Tue-Thu) (n on=3443) | 29,636 | -0.025 log-odds | -0.7 | -0.005 | -0.045 | +0.2 | no effect beyond the price |
| H2H draw rate (last 3-6) | 12,425 | +0.008 log-odds | +0.5 | +0.029 | -0.017 | -0.9 | no effect beyond the price |
| away side newly promoted (n on=4776) | 22,387 | +0.014 log-odds | +0.4 | -0.008 | +0.036 | +0.0 | no effect beyond the price |
| rest days (home − away) | 29,361 | +0.004 log-odds | +0.3 | +0.001 | +0.006 | -0.1 | no effect beyond the price |
| two bottom-20% sides, 2nd half of season (n on=552) | 29,636 | +0.012 log-odds | +0.1 | +0.237 | -0.201 | -2.6 | no effect beyond the price |

### Draw

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| rest days (home − away) | 29,361 | +0.023 log-odds | +1.8 | +0.019 | +0.028 | -0.0 | no effect beyond the price |
| table-position gap | 24,995 | -0.024 log-odds | -1.6 | -0.063 | +0.015 | -3.0 | no effect beyond the price |
| away side played ≤3 days ago (n on=3033) | 29,636 | +0.066 log-odds | +1.5 | +0.021 | +0.114 | -0.2 | no effect beyond the price |
| December/January (n on=5540) | 29,636 | +0.046 log-odds | +1.3 | +0.072 | +0.021 | +0.0 | no effect beyond the price |
| referee home-win rate (last 30) | 8,621 | +0.028 log-odds | +1.1 | +0.011 | +0.049 | +1.1 | no effect beyond the price |
| two top-15% sides (n on=569) | 29,636 | +0.103 log-odds | +1.1 | +0.147 | +0.058 | -0.4 | no effect beyond the price |
| H2H draw rate (last 3-6) | 12,425 | +0.020 log-odds | +1.0 | +0.016 | +0.025 | +0.5 | no effect beyond the price |
| first 4 rounds of season (n on=4583) | 29,636 | +0.026 log-odds | +0.7 | +0.011 | +0.049 | +0.2 | no effect beyond the price |
| midweek (Tue-Thu) (n on=3443) | 29,636 | +0.025 log-odds | +0.6 | -0.003 | +0.055 | -0.2 | no effect beyond the price |
| two bottom-20% sides, 2nd half of season (n on=552) | 29,636 | +0.053 log-odds | +0.6 | +0.150 | -0.042 | -0.1 | no effect beyond the price |
| last 15% of season (n on=5111) | 29,636 | +0.019 log-odds | +0.5 | +0.028 | +0.009 | -0.3 | no effect beyond the price |
| referee avg goals (last 20) | 9,397 | +0.013 log-odds | +0.5 | +0.018 | +0.008 | -0.0 | no effect beyond the price |
| home side bottom-20% in run-in (n on=1667) | 29,636 | +0.027 log-odds | +0.5 | +0.021 | +0.032 | -0.8 | no effect beyond the price |
| both sides' shots on target form | 28,252 | -0.006 log-odds | -0.4 | -0.018 | +0.007 | -0.2 | no effect beyond the price |
| away side newly promoted (n on=4776) | 22,387 | +0.014 log-odds | +0.4 | -0.038 | +0.064 | -2.8 | no effect beyond the price |
| home side played ≤3 days ago (n on=3115) | 29,636 | +0.007 log-odds | +0.2 | -0.056 | +0.073 | -0.1 | no effect beyond the price |
| August/September (n on=6414) | 29,636 | -0.004 log-odds | -0.1 | -0.038 | +0.041 | -0.2 | no effect beyond the price |
| home side newly promoted (n on=4778) | 22,387 | -0.004 log-odds | -0.1 | -0.067 | +0.058 | -0.4 | no effect beyond the price |
| home points form (last 5) | 28,487 | +0.001 log-odds | +0.0 | -0.017 | +0.019 | -0.0 | no effect beyond the price |
| away points form (last 5) | 28,460 | -0.000 log-odds | -0.0 | +0.006 | -0.006 | -0.6 | no effect beyond the price |

### Home win

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| rest days (home − away) | 29,361 | -0.031 log-odds | -2.5 | -0.020 | -0.042 | -0.5 | real in-sample, fails out of sample |
| away side newly promoted (n on=4776) | 22,387 | +0.087 log-odds | +2.5 | +0.109 | +0.064 | -0.4 | real in-sample, fails out of sample |
| home points form (last 5) | 28,487 | +0.031 log-odds | +2.5 | +0.034 | +0.029 | +1.5 | **real, beyond the price** |
| away side played ≤3 days ago (n on=3033) | 29,636 | -0.073 log-odds | -1.8 | +0.008 | -0.160 | +1.0 | no effect beyond the price |
| table-position gap | 24,995 | +0.023 log-odds | +1.7 | +0.037 | +0.009 | +0.2 | no effect beyond the price |
| referee home-win rate (last 30) | 8,621 | +0.031 log-odds | +1.4 | +0.034 | +0.026 | +1.6 | no effect beyond the price |
| home side played ≤3 days ago (n on=3115) | 29,636 | +0.048 log-odds | +1.2 | +0.139 | -0.048 | -2.8 | no effect beyond the price |
| August/September (n on=6414) | 29,636 | -0.035 log-odds | -1.2 | +0.003 | -0.084 | +0.1 | no effect beyond the price |
| December/January (n on=5540) | 29,636 | -0.033 log-odds | -1.1 | -0.043 | -0.024 | +0.4 | no effect beyond the price |
| last 15% of season (n on=5111) | 29,636 | -0.032 log-odds | -1.0 | -0.024 | -0.038 | +0.1 | no effect beyond the price |
| referee avg goals (last 20) | 9,397 | -0.021 log-odds | -1.0 | -0.018 | -0.026 | +0.6 | no effect beyond the price |
| home side bottom-20% in run-in (n on=1667) | 29,636 | -0.049 log-odds | -0.9 | -0.095 | -0.007 | -0.3 | no effect beyond the price |
| home side newly promoted (n on=4778) | 22,387 | +0.030 log-odds | +0.9 | +0.039 | +0.021 | -0.1 | no effect beyond the price |
| first 4 rounds of season (n on=4583) | 29,636 | -0.029 log-odds | -0.8 | +0.005 | -0.076 | -0.0 | no effect beyond the price |
| two bottom-20% sides, 2nd half of season (n on=552) | 29,636 | -0.072 log-odds | -0.8 | +0.044 | -0.186 | +0.2 | no effect beyond the price |
| both sides' shots on target form | 28,252 | +0.010 log-odds | +0.8 | +0.004 | +0.018 | +0.2 | no effect beyond the price |
| away points form (last 5) | 28,460 | +0.006 log-odds | +0.5 | -0.005 | +0.017 | +0.1 | no effect beyond the price |
| two top-15% sides (n on=569) | 29,636 | -0.032 log-odds | -0.4 | -0.039 | -0.025 | -0.1 | no effect beyond the price |
| H2H draw rate (last 3-6) | 12,425 | -0.003 log-odds | -0.2 | +0.020 | -0.032 | -1.2 | no effect beyond the price |
| midweek (Tue-Thu) (n on=3443) | 29,636 | +0.000 log-odds | +0.0 | +0.037 | -0.040 | -1.5 | no effect beyond the price |

### Total corners

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| away points form (last 5) | 28,451 | -0.9% | -4.4 | -0.009 | -0.009 | +1.1 | **real, beyond the price** |
| last 15% of season (n on=5110) | 29,627 | -2.1% | -4.1 | -0.023 | -0.019 | -0.3 | real in-sample, fails out of sample |
| both sides' shots on target form | 28,243 | -1.0% | -4.0 | -0.015 | -0.007 | -3.5 | real in-sample, fails out of sample |
| home points form (last 5) | 28,478 | -0.6% | -2.8 | -0.009 | -0.003 | -2.4 | real in-sample, fails out of sample |
| two top-15% sides (n on=568) | 29,627 | -4.3% | -2.8 | -0.057 | -0.031 | -0.8 | real in-sample, fails out of sample |
| H2H draw rate (last 3-6) | 12,422 | +0.8% | +2.4 | +0.004 | +0.011 | +3.6 | **real, beyond the price** |
| table-position gap | 24,986 | +0.5% | +2.1 | +0.006 | +0.004 | +1.3 | **real, beyond the price** |
| referee avg goals (last 20) | 9,396 | -0.6% | -1.7 | -0.003 | -0.012 | +1.7 | no effect beyond the price |
| August/September (n on=6413) | 29,627 | +0.8% | +1.6 | +0.009 | +0.003 | -5.6 | no effect beyond the price |
| midweek (Tue-Thu) (n on=3442) | 29,627 | -0.9% | -1.5 | -0.013 | -0.005 | +0.1 | no effect beyond the price |
| December/January (n on=5538) | 29,627 | -0.5% | -1.0 | -0.011 | +0.003 | -0.3 | no effect beyond the price |
| home side newly promoted (n on=4778) | 22,382 | +0.5% | +1.0 | +0.008 | +0.003 | -1.3 | no effect beyond the price |
| first 4 rounds of season (n on=4583) | 29,627 | +0.5% | +0.9 | +0.006 | -0.001 | -2.8 | no effect beyond the price |
| away side newly promoted (n on=4775) | 22,382 | +0.3% | +0.5 | -0.003 | +0.009 | -0.4 | no effect beyond the price |
| rest days (home − away) | 29,352 | +0.1% | +0.3 | -0.001 | +0.002 | -0.2 | no effect beyond the price |
| away side played ≤3 days ago (n on=3032) | 29,627 | -0.2% | -0.2 | -0.005 | +0.002 | -0.0 | no effect beyond the price |
| home side played ≤3 days ago (n on=3115) | 29,627 | -0.1% | -0.2 | -0.006 | +0.003 | +0.0 | no effect beyond the price |
| referee home-win rate (last 30) | 8,620 | -0.1% | -0.1 | +0.001 | -0.005 | -1.2 | no effect beyond the price |
| home side bottom-20% in run-in (n on=1667) | 29,627 | -0.1% | -0.1 | -0.005 | +0.004 | -1.8 | no effect beyond the price |
| two bottom-20% sides, 2nd half of season (n on=552) | 29,627 | +0.1% | +0.0 | +0.003 | -0.001 | -0.0 | no effect beyond the price |

### Total yellow cards

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| last 15% of season (n on=5110) | 29,628 | -6.9% | -8.5 | -0.089 | -0.054 | -2.1 | real in-sample, fails out of sample |
| both sides' shots on target form | 28,244 | +2.7% | +7.2 | +0.031 | +0.021 | -0.7 | real in-sample, fails out of sample |
| August/September (n on=6413) | 29,628 | +4.5% | +6.4 | +0.058 | +0.023 | -20.1 | real in-sample, fails out of sample |
| midweek (Tue-Thu) (n on=3442) | 29,628 | -5.4% | -5.9 | -0.054 | -0.059 | +4.4 | **real, beyond the price** |
| two top-15% sides (n on=568) | 29,628 | +8.8% | +4.0 | +0.107 | +0.061 | +1.4 | **real, beyond the price** |
| home side bottom-20% in run-in (n on=1667) | 29,628 | -5.0% | -4.0 | -0.076 | -0.028 | +0.5 | **real, beyond the price** |
| home side played ≤3 days ago (n on=3115) | 29,628 | -3.5% | -3.7 | -0.038 | -0.035 | +2.2 | **real, beyond the price** |
| away side played ≤3 days ago (n on=3032) | 29,628 | -3.3% | -3.3 | -0.037 | -0.031 | +3.1 | **real, beyond the price** |
| table-position gap | 24,987 | -0.8% | -2.2 | -0.011 | -0.004 | +0.8 | **real, beyond the price** |
| referee avg goals (last 20) | 9,397 | +1.2% | +2.1 | +0.014 | +0.006 | +1.4 | **real, beyond the price** |
| first 4 rounds of season (n on=4583) | 29,628 | +1.7% | +2.1 | +0.041 | -0.021 | -20.9 | no effect beyond the price |
| December/January (n on=5538) | 29,628 | +1.0% | +1.4 | +0.004 | +0.019 | -0.5 | no effect beyond the price |
| home side newly promoted (n on=4778) | 22,382 | -1.1% | -1.3 | -0.019 | -0.002 | -0.8 | no effect beyond the price |
| away points form (last 5) | 28,452 | -0.4% | -1.3 | -0.004 | -0.005 | +0.2 | no effect beyond the price |
| rest days (home − away) | 29,353 | -0.3% | -1.1 | +0.000 | -0.007 | -1.4 | no effect beyond the price |
| two bottom-20% sides, 2nd half of season (n on=552) | 29,628 | -1.6% | -0.8 | -0.002 | -0.029 | -0.3 | no effect beyond the price |
| H2H draw rate (last 3-6) | 12,422 | -0.3% | -0.6 | -0.002 | -0.003 | +0.1 | no effect beyond the price |
| home points form (last 5) | 28,479 | +0.2% | +0.5 | +0.007 | -0.005 | -1.4 | no effect beyond the price |
| referee home-win rate (last 30) | 8,621 | +0.1% | +0.2 | -0.000 | +0.000 | -0.6 | no effect beyond the price |
| away side newly promoted (n on=4775) | 22,382 | +0.0% | +0.0 | -0.007 | +0.008 | -1.4 | no effect beyond the price |

### NBA total vs closing line

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| both on back-to-back (n on=141) | 2,645 | -2.70 pts/runs | -1.7 | -3.501 | -1.888 | +0.06 pts² MSE | no effect beyond the price |
| recent net rating (home − away) | 2,565 | -0.53 pts/runs | -1.5 | -0.265 | -0.805 | +0.31 pts² MSE | no effect beyond the price |
| away team's road-trip length | 2,645 | +0.48 pts/runs | +1.4 | +0.267 | +0.707 | +0.30 pts² MSE | no effect beyond the price |
| both teams' recent scoring vs league | 2,565 | -0.38 pts/runs | -1.1 | -0.222 | -0.549 | +0.12 pts² MSE | no effect beyond the price |
| rest days (home − away) | 2,627 | +0.26 pts/runs | +0.7 | -0.266 | +0.772 | -0.47 pts² MSE | no effect beyond the price |
| home team on back-to-back (n on=436) | 2,645 | -0.64 pts/runs | -0.6 | -0.423 | -0.868 | +0.07 pts² MSE | no effect beyond the price |
| first 4 rounds of season (n on=128) | 2,645 | +0.99 pts/runs | +0.6 | +0.859 | +0.000 | +0.04 pts² MSE | no effect beyond the price |
| win streak (home − away) | 2,645 | +0.10 pts/runs | +0.3 | +0.072 | +0.132 | +0.01 pts² MSE | no effect beyond the price |
| playoffs (n on=169) | 2,645 | -0.19 pts/runs | -0.1 | +0.534 | -0.887 | -0.02 pts² MSE | no effect beyond the price |
| away team on back-to-back (n on=455) | 2,645 | -0.09 pts/runs | -0.1 | -1.754 | +1.592 | -1.20 pts² MSE | no effect beyond the price |

### NBA home margin vs closing spread

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| recent net rating (home − away) | 2,563 | +0.67 pts/runs | +2.5 | +0.380 | +0.965 | +0.59 pts² MSE | **real, beyond the price** |
| home team on back-to-back (n on=436) | 2,643 | -0.76 pts/runs | -1.0 | -0.835 | -0.693 | +0.06 pts² MSE | no effect beyond the price |
| rest days (home − away) | 2,625 | +0.18 pts/runs | +0.6 | +0.567 | -0.207 | -0.55 pts² MSE | no effect beyond the price |
| both on back-to-back (n on=141) | 2,643 | +0.68 pts/runs | +0.5 | +1.699 | -0.354 | -0.20 pts² MSE | no effect beyond the price |
| playoffs (n on=169) | 2,643 | +0.51 pts/runs | +0.4 | +2.526 | -1.432 | -0.86 pts² MSE | no effect beyond the price |
| away team's road-trip length | 2,643 | +0.11 pts/runs | +0.4 | +0.217 | -0.008 | -0.04 pts² MSE | no effect beyond the price |
| first 4 rounds of season (n on=127) | 2,643 | +0.33 pts/runs | +0.3 | +0.289 | +0.000 | +0.01 pts² MSE | no effect beyond the price |
| both teams' recent scoring vs league | 2,563 | +0.06 pts/runs | +0.2 | -0.181 | +0.319 | -0.13 pts² MSE | no effect beyond the price |
| win streak (home − away) | 2,643 | -0.04 pts/runs | -0.2 | +0.003 | -0.079 | -0.00 pts² MSE | no effect beyond the price |
| away team on back-to-back (n on=454) | 2,643 | +0.03 pts/runs | +0.0 | +1.174 | -1.128 | -0.56 pts² MSE | no effect beyond the price |

### NBA home win vs closing moneyline

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| recent net rating (home − away) | 2,559 | +0.110 log-odds | +2.2 | +0.051 | +0.177 | +11.7 | **real, beyond the price** |
| home team on back-to-back (n on=435) | 2,639 | -0.128 log-odds | -1.1 | -0.187 | -0.065 | -1.6 | no effect beyond the price |
| both teams' recent scoring vs league | 2,559 | +0.040 log-odds | +0.9 | +0.021 | +0.061 | +1.8 | no effect beyond the price |
| away team on back-to-back (n on=454) | 2,639 | -0.089 log-odds | -0.8 | +0.075 | -0.252 | -5.7 | no effect beyond the price |
| playoffs (n on=169) | 2,639 | -0.136 log-odds | -0.8 | -0.125 | -0.150 | +1.5 | no effect beyond the price |
| first 4 rounds of season (n on=128) | 2,639 | +0.104 log-odds | +0.5 | +0.143 | +0.000 | -1.6 | no effect beyond the price |
| win streak (home − away) | 2,639 | +0.020 log-odds | +0.4 | -0.016 | +0.053 | -2.4 | no effect beyond the price |
| both on back-to-back (n on=141) | 2,639 | -0.070 log-odds | -0.4 | -0.117 | -0.024 | -0.5 | no effect beyond the price |
| rest days (home − away) | 2,621 | +0.012 log-odds | +0.3 | +0.080 | -0.058 | -15.3 | no effect beyond the price |
| away team's road-trip length | 2,639 | +0.004 log-odds | +0.1 | +0.038 | -0.033 | -3.2 | no effect beyond the price |

### WNBA total vs closing line

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| rest days (home − away) | 649 | -0.80 pts/runs | -1.2 | +0.943 | -2.257 |  | no effect beyond the price |
| playoffs (n on=40) | 660 | +3.20 pts/runs | +1.2 | +3.433 | +3.145 |  | too few games with the flag to judge |
| win streak (home − away) | 660 | -0.56 pts/runs | -0.9 | -0.668 | -0.444 |  | no effect beyond the price |
| away team on back-to-back (n on=31) | 660 | +1.35 pts/runs | +0.6 | +2.834 | -0.316 |  | too few games with the flag to judge |
| first 4 rounds of season (n on=119) | 660 | -0.88 pts/runs | -0.5 | -0.522 | -1.073 |  | no effect beyond the price |
| both teams' recent scoring vs league | 598 | -0.37 pts/runs | -0.5 | -1.651 | -0.077 |  | no effect beyond the price |
| home team on back-to-back (n on=24) | 660 | +1.38 pts/runs | +0.4 | +2.200 | +0.399 |  | too few games with the flag to judge |
| away team's road-trip length | 660 | -0.14 pts/runs | -0.2 | +0.710 | -0.863 |  | no effect beyond the price |
| recent net rating (home − away) | 614 | +0.04 pts/runs | +0.1 | +0.050 | +0.030 |  | no effect beyond the price |

### WNBA home margin vs closing spread

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| first 4 rounds of season (n on=119) | 660 | -2.05 pts/runs | -1.5 | -2.009 | -2.155 |  | no effect beyond the price |
| win streak (home − away) | 660 | -0.57 pts/runs | -1.1 | -0.813 | -0.328 |  | no effect beyond the price |
| both teams' recent scoring vs league | 598 | -0.58 pts/runs | -1.1 | -1.657 | -0.300 |  | no effect beyond the price |
| away team's road-trip length | 660 | -0.38 pts/runs | -0.7 | +0.283 | -0.907 |  | no effect beyond the price |
| recent net rating (home − away) | 614 | -0.32 pts/runs | -0.6 | -0.640 | +0.063 |  | no effect beyond the price |
| playoffs (n on=40) | 660 | +0.93 pts/runs | +0.5 | +0.206 | +1.986 |  | too few games with the flag to judge |
| home team on back-to-back (n on=24) | 660 | +1.19 pts/runs | +0.4 | +3.448 | -2.497 |  | too few games with the flag to judge |
| away team on back-to-back (n on=31) | 660 | -0.89 pts/runs | -0.3 | -3.882 | +2.701 |  | too few games with the flag to judge |
| rest days (home − away) | 649 | -0.10 pts/runs | -0.2 | -0.625 | +0.342 |  | no effect beyond the price |

### WNBA home win vs closing moneyline

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| first 4 rounds of season (n on=119) | 660 | -0.505 log-odds | -2.1 | -0.430 | -0.582 |  | **real, beyond the price** |
| playoffs (n on=40) | 660 | +0.402 log-odds | +1.0 | +0.176 | +0.770 |  | too few games with the flag to judge |
| both teams' recent scoring vs league | 598 | -0.071 log-odds | -0.8 | -0.178 | -0.108 |  | no effect beyond the price |
| away team on back-to-back (n on=31) | 660 | -0.305 log-odds | -0.7 | -0.905 | +0.534 |  | too few games with the flag to judge |
| win streak (home − away) | 660 | -0.047 log-odds | -0.5 | -0.154 | +0.060 |  | no effect beyond the price |
| home team on back-to-back (n on=24) | 660 | +0.223 log-odds | +0.4 | +0.680 | -0.444 |  | too few games with the flag to judge |
| recent net rating (home − away) | 614 | +0.024 log-odds | +0.2 | -0.102 | +0.193 |  | no effect beyond the price |
| rest days (home − away) | 649 | -0.009 log-odds | -0.1 | -0.064 | +0.036 |  | no effect beyond the price |
| away team's road-trip length | 660 | -0.006 log-odds | -0.1 | +0.136 | -0.116 |  | no effect beyond the price |

### MLB total vs closing line

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| both on back-to-back (n on=3963) | 4,934 | -0.47 pts/runs | -2.8 | -0.786 | -0.161 | -0.20 pts² MSE | real in-sample, fails out of sample |
| home team on back-to-back (n on=4111) | 4,934 | -0.48 pts/runs | -2.7 | -0.708 | -0.251 | -0.10 pts² MSE | real in-sample, fails out of sample |
| away team on back-to-back (n on=4155) | 4,934 | -0.44 pts/runs | -2.4 | -0.825 | -0.043 | -0.28 pts² MSE | real in-sample, fails out of sample |
| away team's road-trip length | 4,934 | -0.14 pts/runs | -2.2 | -0.195 | -0.079 | +0.01 pts² MSE | **real, beyond the price** |
| win streak (home − away) | 4,934 | +0.08 pts/runs | +1.2 | +0.057 | +0.099 | +0.01 pts² MSE | no effect beyond the price |
| recent net rating (home − away) | 4,853 | +0.06 pts/runs | +1.0 | -0.033 | +0.189 | -0.05 pts² MSE | no effect beyond the price |
| both teams' recent scoring vs league | 4,853 | +0.06 pts/runs | +0.9 | +0.092 | +0.020 | -0.02 pts² MSE | no effect beyond the price |
| first 4 rounds of season (n on=126) | 4,934 | +0.20 pts/runs | +0.5 | +0.302 | -5.047 | -0.02 pts² MSE | no effect beyond the price |
| playoffs (n on=72) | 4,934 | -0.20 pts/runs | -0.4 | +0.233 | -0.624 | +0.00 pts² MSE | too few games with the flag to judge |
| rest days (home − away) | 4,861 | +0.03 pts/runs | +0.4 | -0.007 | +0.063 | -0.04 pts² MSE | no effect beyond the price |

### MLB home win vs closing moneyline

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| rest days (home − away) | 4,861 | +0.050 log-odds | +1.7 | +0.025 | +0.072 | -5.9 | no effect beyond the price |
| first 4 rounds of season (n on=126) | 4,934 | +0.303 log-odds | +1.7 | +0.301 | -20.844 | +2.7 | no effect beyond the price |
| recent net rating (home − away) | 4,853 | +0.026 log-odds | +0.9 | +0.061 | -0.017 | -0.9 | no effect beyond the price |
| away team's road-trip length | 4,934 | -0.022 log-odds | -0.8 | -0.052 | +0.008 | -14.6 | no effect beyond the price |
| home team on back-to-back (n on=4111) | 4,934 | -0.056 log-odds | -0.7 | +0.005 | -0.118 | +0.2 | no effect beyond the price |
| away team on back-to-back (n on=4155) | 4,934 | +0.028 log-odds | +0.4 | +0.048 | +0.008 | -4.8 | no effect beyond the price |
| both teams' recent scoring vs league | 4,853 | -0.008 log-odds | -0.3 | -0.037 | +0.023 | -11.9 | no effect beyond the price |
| win streak (home − away) | 4,934 | +0.005 log-odds | +0.2 | +0.042 | -0.038 | +0.0 | no effect beyond the price |
| playoffs (n on=72) | 4,934 | -0.025 log-odds | -0.1 | +0.017 | -0.067 | +0.0 | too few games with the flag to judge |
| both on back-to-back (n on=3963) | 4,934 | -0.007 log-odds | -0.1 | +0.078 | -0.091 | -2.1 | no effect beyond the price |

### Basketball total vs SportyBet line (all leagues)

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| first 4 rounds of season (n on=19) | 1,163 | +11.25 pts/runs | +2.3 | +10.759 | +11.793 | +2.01 pts² MSE | too few games with the flag to judge |
| rest days (home − away) | 1,157 | -0.27 pts/runs | -0.5 | +0.329 | -0.734 | -0.01 pts² MSE | no effect beyond the price |
| recent net margin (home − away) | 1,147 | -0.31 pts/runs | -0.4 | -0.945 | +0.182 | -0.38 pts² MSE | no effect beyond the price |
| both teams' recent totals vs line | 1,147 | +0.12 pts/runs | +0.2 | +1.361 | -1.343 | -3.69 pts² MSE | no effect beyond the price |
| either team on a back-to-back (n on=55) | 1,157 | +0.24 pts/runs | +0.1 | -6.984 | +2.148 | -2.50 pts² MSE | too few games with the flag to judge |

### Basketball margin vs SportyBet spread (all leagues)

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| rest days (home − away) | 1,153 | -0.89 pts/runs | -2.3 | -0.313 | -1.308 | +1.13 pts² MSE | **real, beyond the price** |
| recent net margin (home − away) | 1,143 | +0.77 pts/runs | +2.0 | +0.764 | +0.741 | +0.36 pts² MSE | no effect beyond the price |
| first 4 rounds of season (n on=19) | 1,159 | +4.10 pts/runs | +1.5 | +5.295 | +2.193 | -0.01 pts² MSE | too few games with the flag to judge |
| either team on a back-to-back (n on=55) | 1,153 | -2.39 pts/runs | -1.4 | -4.251 | -1.233 | +0.51 pts² MSE | too few games with the flag to judge |
| both teams' recent totals vs line | 1,143 | -0.28 pts/runs | -0.7 | -0.587 | +0.007 | +0.06 pts² MSE | no effect beyond the price |

### Basketball home win vs SportyBet price (all leagues)

| Factor | n | Effect | t | Early half | Late half | OOS (×10⁻⁴ nats, or pts² for lines) | Verdict |
|---|---|---|---|---|---|---|---|
| first 4 rounds of season (n on=16) | 998 | +1.281 log-odds | +1.7 | +0.780 | +2.076 | +31.2 | too few games with the flag to judge |
| rest days (home − away) | 994 | -0.089 log-odds | -1.2 | -0.018 | -0.144 | +7.5 | no effect beyond the price |
| either team on a back-to-back (n on=53) | 994 | -0.334 log-odds | -1.1 | -0.320 | -0.269 | +12.6 | too few games with the flag to judge |
| both teams' recent totals vs line | 985 | -0.042 log-odds | -0.6 | -0.064 | -0.020 | -1.8 | no effect beyond the price |
| recent net margin (home − away) | 985 | -0.025 log-odds | -0.3 | -0.067 | +0.021 | -2.3 | no effect beyond the price |
<!-- /PART2 -->
