#!/bin/sh
# football-data.co.uk CSVs (corners/cards counts for 21 European leagues) -> engine/fdcsv/
mkdir -p fdcsv
for s in 2425 2526 2627; do for lg in E0 E1 E2 E3 SC0 SC1 SC2 SC3 D1 D2 I1 I2 SP1 SP2 F1 F2 N1 B1 P1 T1 G1; do
  [ "$s" != 2627 ] && [ -s fdcsv/${lg}_$s.csv ] && continue
  curl -sL -m 30 -o fdcsv/${lg}_$s.csv https://www.football-data.co.uk/mmz4281/$s/$lg.csv
done; done
ls fdcsv | wc -l
