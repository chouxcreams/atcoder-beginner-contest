#!/usr/bin/env pypy3
MOD = 998244353
N, M, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N)]
for total in range(1, K + 1):
    if total > M:
        break
    dp[0][total] = 1

for element in range(1, N):
    for total in range(1, K + 1):
        for toAdd in range(1, M + 1):
            if total + toAdd > K:
                break
            dp[element][total + toAdd] += dp[element - 1][total]
            dp[element][total + toAdd] %= MOD
cnt = 0
for total in range(1, K+1):
    cnt += dp[-1][total]
    cnt %= MOD
print(cnt)
