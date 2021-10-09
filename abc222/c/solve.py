#!/usr/bin/env pypy3
N, M = map(int, input().split())

A = [list(input()) for _ in range(2 * N)]

rank = [n for n in range(N * 2)]
win = [0] * (2 * N)

for i in range(M):
    for k in range(N):
        k1 = rank[2 * k]
        k2 = rank[2 * k + 1]
        p1 = A[k1][i]
        p2 = A[k2][i]
        if p1 == p2:
            continue
        elif p1 == "G":
            if p2 == "C":
                win[k1] += 1
            elif p2 == "P":
                win[k2] += 1
        elif p1 == "C":
            if p2 == "G":
                win[k2] += 1
            elif p2 == "P":
                win[k1] += 1
        elif p1 == "P":
            if p2 == "C":
                win[k2] += 1
            elif p2 == "G":
                win[k1] += 1
    rank.sort()
    rank.sort(key=lambda x: win[x], reverse=True)

for n in range(2 * N):
    print(rank[n] + 1)
