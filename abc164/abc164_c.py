N = int(input())
goods = set()
ans = 0
for _ in range(N):
    good = input()
    if good not in goods:
        goods.add(good)
        ans += 1
print(ans)