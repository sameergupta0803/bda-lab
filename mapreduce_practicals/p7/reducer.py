#!/usr/bin/env python3
import sys
country_now = None
total = 0
def show():
    if country_now is not None:
        print(f"{country_now}\t{total}")
for line in sys.stdin:
    country, count = line.strip().split("\t")
    if country != country_now:
        show()
        country_now, total = country, 0
    total += int(count)
show()
