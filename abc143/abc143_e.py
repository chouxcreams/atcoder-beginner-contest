import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())

distance = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    distance[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    distance[a-1][b-1] = c
    distance[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

for i in range(N):
    for j in range(N):
        if i == j:
            distance[i][j] = 0
        elif distance[i][j] <= L:
            distance[i][j] = 1
        else:
            distance[i][j] = float('inf')

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    ans = distance[s-1][t-1]-1
    if ans is float('inf'):
        ans = -1
    print(ans)
