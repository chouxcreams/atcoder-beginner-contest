#!/usr/bin/env pypy3

N = int(input())
S = list(input())
X = list(input())

dp = [set() for _ in range(N + 1)]
dp[N].add(0)
for i in range(N - 1, -1, -1):
    num = int(S[i])
    person = X[i]
    if person == "A":
        for mod in range(7):
            if (mod * 10) % 7 in dp[i + 1] and (mod * 10 + num) % 7 in dp[i + 1]:
                dp[i].add(mod)
    else:
        for mod in range(7):
            if (mod * 10) % 7 in dp[i + 1] or (mod * 10 + num) % 7 in dp[i + 1]:
                dp[i].add(mod)
    if dp[i] == {}:
        print("Aoki")
        break
else:
    if 0 in dp[0]:
        print("Takahashi")
    else:
        print("Aoki")


