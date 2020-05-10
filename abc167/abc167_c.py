import sys
sys.setrecursionlimit(1000000000)

N, M, X = map(int, input().split())
Matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    Matrix.append(row)

U = [0] * (M + 1)
def rec(ans, pos):
    if pos == N:
        return ans
    row = Matrix[pos]
    for i in range(M  + 1):
        U[i] += row[i]

    for u in U[1:]:
        if u < X:
            ans = min(rec(ans, pos + 1), ans)
            break
    else:
        ans = min(U[0], ans)

    for i in range(M  + 1):
        U[i] -= row[i]
    return min(rec(ans, pos + 1), ans)

ans = rec(float('inf'), 0)
if ans == float('inf'):
    ans = -1
print(ans)