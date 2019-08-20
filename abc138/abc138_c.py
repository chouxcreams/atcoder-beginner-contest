from heapq import heapify, heappush, heappop
N = int(input())
V = list(map(int, input().split()))

heapify(V)

now_value = 0
while len(V) > 1:
    x = heappop(V)
    y = heappop(V)
    heappush(V, (x+y)/2)

print(heappop(V))