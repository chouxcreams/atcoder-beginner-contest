#!/usr/bin/env pypy3

from math import ceil, floor
X = input()
M = int(input())


def convert(S, n):
    c = 0
    for s in S:
        c = c * n + int(s)
    return c


d = max(map(int, list(X)))  # O(|X|)
order = len(X)
n = d + 1
if order == 1:
    if M >= d:
        print(1)
    else:
        print(0)

else:
    lower = floor(M ** (1 / order))
    upper = ceil(M ** (1 / (order - 1)))

    def rec(head, tail):
        if tail - head <= 1:
            if convert(X, tail) <= M:
                return tail
            return head
        nxt = (head + tail) // 2
        if convert(X, nxt) <= M:
            return rec(nxt, tail)
        else:
            return rec(head, nxt)


    ans = rec(lower, upper) - d  # O(logM)
    print(max(ans, 0))
