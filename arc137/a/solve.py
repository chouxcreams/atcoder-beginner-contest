#!/usr/bin/env pypy3
from collections import deque
from math import gcd

L, R = map(int, input().split())

inStack = set()

queue = deque([(L, R)])

while len(queue) != 0:
    x, y = queue.popleft()
    inStack.add((x, y))
    if gcd(x, y) == 1:
        print(y - x)
        break
    if (x + 1, y) not in inStack:
        queue.append((x + 1, y))
    if (x, y - 1) not in inStack:
        queue.append((x, y - 1))
else:
    print(1)
