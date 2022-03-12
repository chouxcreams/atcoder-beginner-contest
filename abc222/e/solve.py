#!/usr/bin/env pypy3
import sys

sys.setrecursionlimit(1000000000)
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
U = [0] * (N - 1)
V = [0] * (N - 1)
MOD = 998244353


class Node:
    def __init__(self, index):
        self.index = index
        self.path = []


nodes = [Node(n) for n in range(N)]

for i in range(N - 1):
    u, v = map(int, input().split())
    U[i], V[i] = u - 1, v - 1
    nodes[u - 1].path.append(i)
    nodes[v - 1].path.append(i)

passed = [0] * (N - 1)


def dfs(pos, dest, come_from):
    if pos == dest:
        return True
    node = nodes[pos]
    for path in node.path:
        if come_from is not None:
            if path == come_from:
                continue
        if U[path] == pos:
            res = dfs(V[path], dest, path)
        else:
            res = dfs(U[path], dest, path)
        if res:
            passed[path] += 1
            return True
    return False


for i in range(M - 1):
    dfs(A[i] - 1, A[i + 1] - 1, None)


tmp = passed[0]
T = sum(passed)
dp = [[0] * (T + 1) for _ in range(N - 1)]
dp[0][0] = 1
dp[0][tmp] = 1

for i in range(1, N - 1):
    p = passed[i]
    for j in range(T + 1):
        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= MOD
        if j - p < 0:
            continue
        dp[i][j] += dp[i - 1][j - p]
        dp[i][j] %= MOD


if T - K % 2 == 1:
    print(0)
elif T < abs(K):
    print(0)
else:
    B = (T - abs(K)) // 2
    print(dp[N - 2][B])
