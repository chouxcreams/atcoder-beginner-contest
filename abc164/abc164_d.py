S = input()

N = len(S)
table = [-1] * N
T = [-1] * N
prev = 0
for i, s in enumerate(reversed(S)):
    prev += (int(s) * pow(10, i, 2019)) % 2019
    prev %= 2019
    T[i] = prev

DP = [0] * 2019
for t in T:
    DP[t] += 1

ans = DP[0]
for num in DP:
    ans += num * (num - 1) // 2

print(ans)