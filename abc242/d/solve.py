#!/usr/bin/env pypy3
S = input()
Q = int(input())
L = len(S)
squares = [1]
for i in range(Q):
    t, k = map(int, input().split())
    k = k - 1
    count = 0
    fix = 0
    while k != 0 and count < t:
        fix += 1 + k % 2
        k = k // 2
        count += 1
    fix += t - count
    if S[k] == "B":
        fix += 1
    elif S[k] == "C":
        fix += 2
    if fix % 3 == 0:
        print("A")
    elif fix % 3 == 1:
        print("B")
    else:
        print("C")
