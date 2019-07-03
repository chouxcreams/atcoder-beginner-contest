from copy import copy

N, M, Q = map(int, input().split())
area = [copy([0]*N) for i in range(N)]
L = [0]*N
R = [0]*N

# O(M)
for i in range(M):
    l, r = map(int, input().split())
    area[l-1][r-1] += 1

# O(N^2)
for i in range(N):
    for j in range(i, -1, -1):
        if j!=i:
            area[j][i] += area[j+1][i]

# O(N^2)
for i in range(N):
    for j in range(i, -1, -1):
        if j != i:
            area[j][i] += area[j][i-1]

# O(Q)
count = 0
for i in range(Q):
    p, q = map(int, input().split())
    print(area[p-1][q-1])
