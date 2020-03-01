N, R = map(int, input().split())

if N > 10:
    K = 10
else:
    K = N

print(R + 100 * (10-K))