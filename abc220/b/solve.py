#!/usr/bin/env pypy3
from functools import reduce

K = int(input())
A, B = map(list, input().split())

a = int(reduce(lambda x, y: int(x) * K + int(y), A, 0))
b = int(reduce(lambda x, y: int(x) * K + int(y), B, 0))

print(a * b)
