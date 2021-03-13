#!/usr/bin/env pypy3
from copy import copy

N, M, Q = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
X = list(map(int, input().split()))

for _ in range(Q):
    L, R = map(int, input().split())
    copiedX = copy(X)
    for m in range(L - 1, R):
        copiedX[m] = 0
    sortedX = sorted(copiedX)
    copiedV = copy(V)
    ans = 0
    for capacity in sortedX:
        if capacity == 0:
            continue
        current_index = -1
        current_value = 0
        for n in range(N):
            if W[n] > capacity:
                continue
            if copiedV[n] > current_value:
                current_index = n
                current_value = copiedV[n]
        if current_index != -1:
            ans += current_value
            copiedV[current_index] = -1
    print(ans)


