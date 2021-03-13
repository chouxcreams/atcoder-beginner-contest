#!/usr/bin/env pypy3
M, H = map(int, input().split())
if H %M == 0:
    print("Yes")
else:
    print("No")
