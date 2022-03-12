#!/usr/bin/env pypy3
N = int(input())
X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]


class Point:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s


for i in range(N):
    X[i], Y[i] = map(int, input().split())

S = list(input())

points = [Point(X[i], Y[i], S[i]) for i in range(N)]
points.sort(key=lambda x: x.x)

willRight = set()
for p in points:
    if p.y in willRight and p.s == "L":
        print("Yes")
        break
    if p.s == "R":
        willRight.add(p.y)
else:
    print("No")
