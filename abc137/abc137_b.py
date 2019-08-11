K, X = map(int, input().split())

K-=1
ans = ""
for num in range(X-K, X+K+1):
    ans += str(num) + " "
print(ans)