#!/usr/bin/env python3
import sys
year_now = None
maximum = None
def show():
    if year_now is not None:
        print(f"{year_now}\t{maximum}")
for line in sys.stdin:
    year, val = line.strip().split("\t")
    val = float(val)
    if year != year_now:
        show()
        year_now, maximum = year, val
    else:
        maximum = max(maximum, val)
show()
