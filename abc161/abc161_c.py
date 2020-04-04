N, K = map(int, input().split())
ans = N % K
print(min(K-ans, ans))