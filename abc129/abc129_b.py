N = int(input())
W = list(map(int, input().split()))

total = sum(W)
now = 0
ans = total
for w in W:
    now += w
    ans = min(abs(total-now*2), ans)

print(ans)