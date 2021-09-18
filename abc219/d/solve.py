N = int(input())
X, Y = map(int, input().split())
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    A[i], B[i] = map(int, input().split())

dp = [[[1000 for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0][0] = 0

for i in range(1, N + 1):
    a = A[i - 1]
    b = B[i - 1]
    for x in range(X + 1):
        for y in range(Y + 1):
            if x +a >= X:
                x1 = X
            else:
                x1 = x + a
            if y + b >= Y:
                y1 = Y
            else:
                y1 = y + b
            dp[i][x1][y1] = min(dp[i - 1][x][y] + 1, dp[i][x1][y1])
            dp[i][x][y] = min(dp[i][x][y], dp[i - 1][x][y])

ans = dp[N][X][Y]

if ans == 1000:
    print(-1)
else:
    print(ans)
