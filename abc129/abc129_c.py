N, M = map(int, input().split())
A = [int(input()) for i in range(M)]

DENOMINATOR = 1000000007

pos = 0
route = 1
before = 0

for i in range(1, N+1):
    route, before = route+before, route
    if pos < M:
        if A[pos] == i:
            route = 0
            pos+=1

print(route%DENOMINATOR)