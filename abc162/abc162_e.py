N, K = map(int, input().split())
MOD = 10 ** 9 + 7
GCDs = [-1] * (K + 1)

ans = 0
for i in range(K, 0, -1):
    num = K // i
    GCDs[i] = pow(num, N, MOD)
    for n in range(2, num + 1):
        GCDs[i] -= GCDs[i * n] % MOD
    ans = (GCDs[i] * i % MOD + ans) % MOD

print(ans)
