#!/usr/bin/env pypy3
from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))

e = [[] for _ in range(N + 1)]
for i, a in enumerate(A):
    e[a].append(i + 1)
Q = int(input())
for _ in range(Q):
    L, R, X = map(int, input().split())
    head = bisect_left(e[X], L)
    tail = bisect_right(e[X], R)
    print(tail - head)
