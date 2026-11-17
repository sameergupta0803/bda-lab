#!/usr/bin/env python3
import sys, re
TARGET = "hadoop"
for line in sys.stdin:
    for word in re.findall(r"[A-Za-z0-9]+", line.lower()):
        if word == TARGET:
            print(f"{TARGET}\t1")
