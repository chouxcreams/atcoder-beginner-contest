#!/usr/bin/env pypy3
N, X = map(int, input().split())
S = list(input())
S2 = list()
for s in S:
    if s == 'U' and len(S2) and (S2[-1] == "L" or S2[-1] == "R"):
        S2.pop()
    else:
        S2.append(s)

for s in S2:
    if s == 'L':
        X *= 2
    elif s == 'R':
        X = X * 2 + 1
    else:
        X //= 2

print(X)
