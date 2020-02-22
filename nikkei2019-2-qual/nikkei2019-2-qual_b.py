import sys
input = sys.stdin.readline
MOD = 998244353
N = int(input())
D = list(map(int, input().split()))

L = [0] * N

for d in D:
    L[d] += 1
if D[0] != 0:
    print(0)
    sys.exit()
total = 1
prev_l = 1
for i, l in enumerate(L):
    if i == 0:
        prev_l = l
        if l != 1:
            total = 0
            break
        continue
    total *= (prev_l**l)
    total %= MOD
    prev_l = l

print(total%MOD)
