#!/usr/bin/env pypy3

a, b = map(int, input().split())
c, d = map(int, input().split())

ans = -float("inf")
for x in range(a, b + 1):
    for y in range(c, d + 1):
        ans = max(x - y, ans)
print(ans)
