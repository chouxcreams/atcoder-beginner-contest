N, P = map(int, input().split())
S = input()

if P == 2 or P == 5:
    ans = 0
    for i, s in enumerate(S):
        if int(s) % P == 0:
            ans += i+1
    print(ans)
    import sys
    sys.exit(0)

surpluses = [0] * P
s = 0
power = 1
for i in range(N):
    s = (s + int(S[-1-i]) * power) % P
    surpluses[s % P] += 1
    power = (power * 10) % P

ans = surpluses[0]
for count in surpluses:
    ans += count * (count - 1) // 2

print(ans)
