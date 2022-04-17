#!/usr/bin/env pypy3
from math import log, ceil

A, B, K = map(int, input().split())
print(ceil(log(B/A, K)))
