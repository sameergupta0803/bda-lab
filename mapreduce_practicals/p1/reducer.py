#!/usr/bin/env python3
import sys
total = 0
for line in sys.stdin:
    word, count = line.strip().split("\t")
    total += int(count)
print(f"hadoop\t{total}")
