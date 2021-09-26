#!/usr/bin/env pypy3
MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
dp = [[0 for _ in range(10)] for _ in range(N)]

for k in range(10):
    if k == A[0]:
        dp[0][k] = 1

for index, a in enumerate(A[1:]):
    i = index + 1
    for k in range(10):
        f = (k + a) % 10
        dp[i][f] += dp[i - 1][k] % MOD
        dp[i][f] %= MOD
        g = (k * a) % 10
        dp[i][g] += dp[i - 1][k] % MOD
        dp[i][g] %= MOD

for p in dp[N - 1]:
    print(p)
