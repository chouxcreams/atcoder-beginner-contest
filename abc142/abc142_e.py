import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [-1]*M
B = [-1]*M
C = [-1]*M

for i in range(M):
    A[i], B[i] = map(int, input().split())
    ls = list(map(int, input().split()))
    c = 0
    for j in range(len(ls)):
        c += 2 ** (ls[j]-1)
    C[i] = c


dp = [[float('inf')]*(2**N) for _ in range(M)]

j = 0
for i, di in enumerate(C):
    if i == 0:
        dp[i][di] = A[i]
        dp[i][0] = 0
        continue
    for j in range(2**N):
        stay = dp[i - 1][j | di]
        buy = dp[i - 1][j] + A[i]
        now = dp[i][j | di]
        dp[i][j | di] = min(stay, buy, now)
    for j in range(2**N):
        dp[i][j] = min(dp[i][j], dp[i-1][j])

ans = dp[-1][2**N-1]
if ans > sum(A):
    print(-1)
else:
    print(ans)