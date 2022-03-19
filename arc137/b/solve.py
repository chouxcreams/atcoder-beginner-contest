#!/usr/bin/env pypy3

N = int(input())
A = list(map(int, input().split()))
resMax = 0
resMin = 0
lastMax = 0
lastMin = 0
for a in A:
    if a == 0:
        lastMax = max(lastMax + 1, 1)
        lastMin = min(lastMin + 1, 1)
    else:
        lastMin = min(lastMin - 1, -1)
        lastMax = max(lastMax - 1, -1)
    resMax = max(lastMax, resMax)
    resMin = min(lastMin, resMin)
print(resMax - resMin + 1)
