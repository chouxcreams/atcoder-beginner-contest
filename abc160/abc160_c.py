K, N = map(int, input().split())
A = list(map(int, input().split()))
D = [-1] * N
for i in range(N-1):
    D[i] = A[i + 1] - A[i]
D[N-1] = K - A[N-1] + A[0]
print(sum(D) - max(D))