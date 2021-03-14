#!/usr/bin/env pypy3

N, K = map(int, input().split())


def g1(x):
    return int(''.join(sorted(str(x))))


def g2(x):
    return int(''.join(sorted(str(x), reverse=True)))


def f(x):
    return g2(x) - g1(x)


a = N
for _ in range(K):
    a = f(a)
print(a)

