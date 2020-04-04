K = int(input())
from collections import deque

queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

x = 0
for _ in range(K):
    x = queue.popleft()
    nx = x * 10 + x % 10
    if x % 10 != 0:
        queue.append(nx - 1)
    queue.append(nx)
    if x % 10 != 9:
        queue.append(nx + 1)
print(x)
