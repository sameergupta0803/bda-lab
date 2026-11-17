#!/usr/bin/env python3
import sys
counts = {}
for line in sys.stdin:
    year, val = line.strip().split("\t")
    counts[year] = counts.get(year, 0) + int(val)
for year in sorted(counts):
    print(f"{year}\t{counts[year]}")
if counts:
    best = max(counts, key=counts.get)
    print(f"MAX_BOOKS_YEAR\t{best}\t{counts[best]}")
