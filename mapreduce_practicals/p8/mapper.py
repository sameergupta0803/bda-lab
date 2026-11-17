#!/usr/bin/env python3
import sys, csv
for line in sys.stdin:
    row = next(csv.reader([line]))
    if len(row) >= 3 and row[1].strip() != "movieId":
        print(f"{row[1].strip()}\t{row[2].strip()}")
