N = int(input())
X = list(map(int, input().split()))
average = round(sum(X) / N)

ans = 0
for x in X:
    ans += (x - average) ** 2
print(ans)