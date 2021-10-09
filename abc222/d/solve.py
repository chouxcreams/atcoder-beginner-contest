#!/usr/bin/env pypy3

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

dp = [[0] * 3001 for _ in range(N)]

now = 0
for i in range(A[0], 3001):
    if i <= B[0]:
        now += 1
        now %= MOD
    dp[0][i] = now

for n in range(1, N):
    now = 0
    for i in range(A[n], 3001):
        if i <= B[n]:
            now += dp[n - 1][i]
            now %= MOD
        dp[n][i] = now

print(dp[N - 1][-1] % MOD)
