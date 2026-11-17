#!/usr/bin/env python3
import sys
movie_now = None
tags = []
def show():
    if movie_now is not None:
        print(f"{movie_now}\t{', '.join(tags)}")
for line in sys.stdin:
    movie, tag = line.rstrip("\n").split("\t", 1)
    if movie != movie_now:
        show()
        movie_now, tags = movie, []
    tags.append(tag)
show()
