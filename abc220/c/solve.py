#!/usr/bin/env pypy3

import bisect

N = int(input())
A = list(map(int, input().split()))
X = int(input())

pa = 0
sumA = []
for a in A:
    sumA.append(pa + a)
    pa += a
acc = X // sumA[-1]
cur = X % sumA[-1]


offset = bisect.bisect_right(sumA, cur) + 1

print(N * acc + offset)
