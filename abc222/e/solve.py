#!/usr/bin/env pypy3
import sys

sys.setrecursionlimit(1000000000)
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
U = [0] * (N - 1)
V = [0] * (N - 1)


class Node:
    def __init__(self, index):
        self.index = index
        self.to = []
        self.count = 0


nodes = [Node(n) for n in range(N)]

for i in range(N - 1):
    u, v = map(int, input().split())
    U[i], V[i] = u, v
    nodes[u].to.append(i)
    nodes[v].to.append(i)

paths = [0] * (N - 1)


def rec(pos, to, oa):
    if pos == to:
        return True
    node = nodes[pos]
    for path in node.to:
        if oa is not None:
            if path == oa:
                continue
        if U[path] == pos:
            res = rec(V[path], to, path)
        else:
            res = rec(U[path], to, path)
        if res:
            paths[path] += 1
    return False


for to in range(M):
    rec(0, to, None)
