#!/usr/bin/env pypy3

N = int(input())
A = [0 for _ in range(N)]
T = [0 for _ in range(N)]

for i in range(N):
    A[i], T[i] = map(int, input().split())
Q = int(input())
X = list(map(int, input().split()))

lower = -float('inf')
upper = float('inf')
offset = 0
flag = False
ans = 0

for i in range(N):
    t = T[i]
    a = A[i]
    if t == 1:
        offset += a
    elif t == 2:
        lower = max(lower, a - offset)
        upper = max(upper, a - offset)
    else:
        upper = min(upper, a - offset)
        lower = min(lower, a - offset)

for q in range(Q):
    x = X[q]
    if flag:
        print(ans)
    elif x < lower:
        print(lower + offset)
    elif lower <= x <= upper:
        print(x + offset)
    else:
        print(upper + offset)
