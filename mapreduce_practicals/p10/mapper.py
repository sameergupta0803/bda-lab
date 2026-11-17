#!/usr/bin/env python3
import sys
for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) != 5 or parts[0].strip() == "UserId":
        continue
    user, track, shared, radio, skip = [x.strip() for x in parts]
    print(f"ALL\tUSER:{user}")
    print(f"TRACK:{track}\tSHARED:{shared}")
    print(f"TRACK:{track}\tRADIO:{radio}")
    print(f"TRACK:{track}\tLISTEN:1")
    print(f"TRACK:{track}\tSKIP:{int(radio) * int(skip)}")
