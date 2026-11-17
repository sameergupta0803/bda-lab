#!/usr/bin/env python3
import sys
for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) == 3:
        print(f"{parts[0].strip()}\t{parts[2].strip()}")
