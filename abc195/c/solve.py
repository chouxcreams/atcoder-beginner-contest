#!/usr/bin/env pypy3

N = int(input())
seed = 1
commas = 0
ans = 0
while True:
    if seed <= N < seed * 1000:
        ans += (N - seed + 1) * commas
        break
    else:
        ans += (seed * 1000 - seed) * commas
        seed *= 1000
        commas += 1
        continue
print(ans)
