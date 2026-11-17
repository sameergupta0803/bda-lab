#!/usr/bin/env python3
import sys
for line in sys.stdin:
    name, marks = line.strip().split("\t")
    m = float(marks)
    grade = "A" if m >= 80 else ("B" if m >= 60 else ("C" if m >= 40 else "F"))
    print(f"{name}\t{m}\t{grade}")
