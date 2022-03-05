#!/usr/bin/env pypy3

A, B, C, X = map(int, input().split())

if X <= A:
    print(1.0)
elif X <= B:
    print(C / (B - A))
else:
    print(0)
