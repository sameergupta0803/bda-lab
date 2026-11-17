#!/usr/bin/env python3
import sys
current = None
max_temp = max_rain = max_dew = None
def show():
    if current is not None:
        print(f"{current}\t{max_temp}\t{max_rain}\t{max_dew}")
for line in sys.stdin:
    key, values = line.strip().split("\t")
    temp, rain, dew = map(float, values.split(","))
    if key != current:
        show()
        current = key
        max_temp, max_rain, max_dew = temp, rain, dew
    else:
        max_temp = max(max_temp, temp)
        max_rain = max(max_rain, rain)
        max_dew = max(max_dew, dew)
show()
