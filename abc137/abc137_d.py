from heapq import heapify, heappush, heappop
N, M = map(int, input().split())
heap = []
heapify(heap)

A = [[] for i in range(M)]

for i in range(N):
    a, b = map(int, input().split())
    if a > M:
        continue
    A[a-1].append(b)

count = 0
for a in A:
    for b in a:
        heappush(heap, -b)
    if len(heap) == 0:
        continue
    num = heappop(heap)
    count += num

print(-count)
