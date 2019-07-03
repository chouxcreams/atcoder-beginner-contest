N, L = map(int, input().split())
eat_one = 101+N
ideal_pie = 0
for i in range(N):
    taste = L+i
    ideal_pie += taste
    eat_one = taste if abs(eat_one) > abs(taste) else eat_one
print(ideal_pie - eat_one)