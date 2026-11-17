#!/usr/bin/env python3
import sys
for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) != 5 or parts[0] == "year":
        continue
    year, month, temp, rain, dew = parts
    print(f"{year}-{month}\t{temp},{rain},{dew}")
