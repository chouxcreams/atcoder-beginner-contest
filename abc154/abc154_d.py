from collections import deque

N, K = map(int, input().split())
P = list(map(int, input().split()))

exps = [-1.0] * 1001
seed = 0
for i in range(1, 1001):
    seed += i
    exps[i] = seed / i

total = 0
heads = deque()
for k in range(K):
    p = P[k]
    exp = exps[p]
    total += exp
    heads.append(exp)
ans = total
for k in range(K, N):
    exp = exps[P[k]]
    head = heads.popleft()
    heads.append(exp)
    total = total - head + exp
    ans = max(ans, total)

print(ans)