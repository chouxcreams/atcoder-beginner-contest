N, K = map(int, input().split())

n = 1
for i in range(100):
    if N < n:
        print(i)
        break
    n *= K

