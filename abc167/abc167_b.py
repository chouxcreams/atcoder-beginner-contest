import sys
A, B, C, K = map(int, input().split())

if A >= K:
    print(K)
elif A + B >= K:
    print(A)
elif A + B + C >= K:
    print(A - (K - A - B))
else:
    print(A-C)


