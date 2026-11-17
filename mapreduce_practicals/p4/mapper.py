#!/usr/bin/env python3
import sys
M, P = 2, 2
for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) != 4:
        continue
    matrix, r, c, val = parts[0].strip(), int(parts[1]), int(parts[2]), float(parts[3])
    if matrix == "A":
        for j in range(P):
            print(f"{r},{j}\tA,{c},{val}")
    elif matrix == "B":
        for i in range(M):
            print(f"{i},{c}\tB,{r},{val}")
