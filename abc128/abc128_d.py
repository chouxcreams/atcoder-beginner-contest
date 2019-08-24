from collections import deque
from heapq import heapify, heappush, heappop
from copy import deepcopy
N, K = map(int, input().split())
D = deque(map(int, input().split()))
ans = 0

for r in range(1, min(N, K)+1):
    for a in range(0, r+1):
        total = 0
        V = deepcopy(D)
        bag = []
        heapify(bag)
        minus = 0
        b = r-a
        for i in range(a):
            stone = V.popleft()
            total += stone
            heappush(bag, stone)
            if stone < 0:
                minus += 1
        for i in range(b):
            stone = V.pop()
            total += stone
            heappush(bag, stone)
            if stone < 0:
                minus += 1
        for i in range(minus):
            if i == (K-r):
                break
            total -= heappop(bag)
        ans = max(total, ans)

print(ans)