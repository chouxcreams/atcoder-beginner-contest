A, B, M = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
ans = min(As) + min(Bs)

for _ in range(M):
    x, y, c = map(int, input().split())
    value = As[x-1] + Bs[y-1] - c
    ans = min(ans, value)

print(ans)