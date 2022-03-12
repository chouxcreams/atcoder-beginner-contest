#!/usr/bin/env pypy3
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

exsits = set()
res1 = 0
res2 = 0

for i in range(N):
    a, b = A[i], B[i]
    if A[i] == B[i]:
        res1 += 1
        continue
    if a in exsits:
        res2+=1
    else:
        exsits.add(a)
    if b in exsits:
        res2 += 1
    else:
        exsits.add(b)

print(res1)
print(res2)