#!/usr/bin/env python3
import sys
users = set()
track_stats = {}
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    if key == "ALL":
        users.add(value.replace("USER:", ""))
    else:
        track = key.replace("TRACK:", "")
        if track not in track_stats:
            track_stats[track] = [0, 0, 0, 0]
        if value.startswith("SHARED:"):
            track_stats[track][0] += int(value[7:])
        elif value.startswith("RADIO:"):
            track_stats[track][1] += int(value[6:])
        elif value == "LISTEN:1":
            track_stats[track][2] += 1
        elif value.startswith("SKIP:"):
            track_stats[track][3] += int(value[5:])
print(f"UNIQUE_LISTENERS\t{len(users)}")
for track in sorted(track_stats):
    s, r, listens, skips = track_stats[track]
    print(f"TRACK\t{track}\tSHARED\t{s}\tRADIO\t{r}\tTOTAL_LISTENS\t{listens}\tRADIO_SKIPS\t{skips}")
