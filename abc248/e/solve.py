#!/usr/bin/env pypy3
import sys
N, K = map(int, input().split())

if K == 1:
    print("Infinity")
    sys.exit()


class Point:
    def __init__(self, i, x, y):
        self.i, self.x, self.y = i, x, y


class Line:
    def __init__(self, p1, p2):
        self.points = [p1, p2]
        self.checked = set()
        self.checked.add(p1.i)
        self.checked.add(p2.i)

    def isContain(self, p):
        p1, p2 = self.points[0], self.points[1]
        return (p2.x - p1.x) * (p2.y - p.y) == (p2.y - p1.y) * (p2.x - p.x)


points = []
lines = []

for i in range(N):
    x, y = map(int, input().split())
    checked = set()
    newPoint = Point(i, x, y)
    for line in lines:
        if line.isContain(newPoint):
            line.points.append(newPoint)
            line.checked.add(newPoint.i)
            checked = checked | line.checked
    for point in points:
        if point.i in checked:
            continue
        lines.append(Line(point, newPoint))
    points.append(newPoint)

cnt = 0
for line in lines:
    if len(line.points) >= K:
        cnt += 1
print(cnt)

