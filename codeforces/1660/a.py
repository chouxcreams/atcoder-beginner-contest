t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a == 0:
        print(1)
    else:
        print(b * 2 + a + 1)
