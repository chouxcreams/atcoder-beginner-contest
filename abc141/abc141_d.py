from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [-a for a in list(map(int, input().split()))]

sumA = -sum(A)
heapify(A)

for _ in range(M):
    a = -heappop(A)
    sumA -= a-a//2
    heappush(A, -(a//2))

print(sumA)