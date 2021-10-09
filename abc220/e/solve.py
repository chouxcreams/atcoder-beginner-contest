#!/usr/bin/env pypy3
from math import ceil

MOD = 998244353
N, D = map(int, input().split())

ans = 0
start = min(D, N - 1)
end = max(1, ceil(D / 2))
squares = [1]
for n in range(N):
    squares.append(squares[-1] * 2 % MOD)
D_SQUARE = 2 ** D % MOD

for d in range(start, end - 1, -1):
    trees = squares[N - d] - 1
    if d == D:
        tmp = D_SQUARE * 2 % MOD
    elif d == D // 2:
        tmp = D_SQUARE // 2 % MOD
    else:
        tmp = D_SQUARE
    tmp = (tmp * trees) % MOD
    ans = (ans + tmp) % MOD
print(ans % MOD)
