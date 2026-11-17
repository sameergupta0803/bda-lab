#!/usr/bin/env python3
import sys
current = None
a, b = {}, {}
def show():
    if current is not None:
        total = sum(a[k] * b[k] for k in a if k in b)
        print(f"{current}\t{total}")
for line in sys.stdin:
    key, item = line.strip().split("\t")
    matrix, k, val = item.split(",")
    k, val = int(k), float(val)
    if key != current:
        show()
        current = key
        a, b = {}, {}
    if matrix == "A":
        a[k] = val
    else:
        b[k] = val
show()
