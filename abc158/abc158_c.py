A, B = map(int, input().split())

for n in range(1, 20000):
    a = n * 8 // 100
    b = n * 10 // 100
    if a == A and b == B:
        print(n)
        break
else:
    print(-1)