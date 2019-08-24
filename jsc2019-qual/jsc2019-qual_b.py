import sys
input = sys.stdin.readline
D = 10**9+7

N, K = map(int, input().split())
A = list(map(int, input().split()))

afters = [0]*N
alls = [0]*N

for i, key in enumerate(A):
    for j, a in enumerate(A):
        if a < key:
            alls[i] += 1
            if j > i:
                afters[i] += 1

ans = sum(afters)*K + sum(alls)*K*(K-1)//2
print(ans % D)