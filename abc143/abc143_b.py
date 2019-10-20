N = int(input())
D = list(map(int, input().split()))

recovery = 0
for i in range(N-1):
    for j in range(i+1, N):
        recovery += D[i]*D[j]
print(recovery)