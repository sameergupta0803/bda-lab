#!/usr/bin/env python3
import sys, csv
for line in sys.stdin:
    row = next(csv.reader([line]))
    if len(row) >= 8 and row[7].strip() != "Country":
        country = row[7].strip()
        if country:
            print(f"{country}\t1")
