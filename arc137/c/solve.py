#!/usr/bin/env pypy3

N = int(input())
A = list(map(int, input().split()))

if A[-1] - A[-2] >= 2:
    print('Alice')
elif (A[-1] - (N-1)) % 2 == 0:
    print('Bob')
else:
    print('Alice')
