#!/usr/bin/env python3
import sys
for line in sys.stdin:
    date, values = line.strip().split("\t")
    temp, sunshine = map(float, values.split(","))
    result = "Sunny" if sunshine >= 6 else ("Cool" if temp <= 20 else "Not Sunny/Cool")
    print(f"{date}\t{result}")
