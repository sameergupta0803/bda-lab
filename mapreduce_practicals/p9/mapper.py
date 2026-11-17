#!/usr/bin/env python3
import sys, csv
for line in sys.stdin:
    row = next(csv.reader([line]))
    if len(row) >= 3 and row[2].strip() != "Published Year":
        year = row[2].strip()
        if year:
            print(f"{year}\t1")
