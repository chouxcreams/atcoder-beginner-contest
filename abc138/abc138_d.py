import sys
input = sys.stdin.readline
N, Q = map(int, input().split())

nodes = [-1]*N # 親ノードを保存
counts = [0]*N
for _ in range(N-1):
    a, b = input().split()
    nodes[int(b)-1] = int(a)-1

for _ in range(Q):
    p, x = input().split()
    counts[int(p)-1] += int(x)

for i in range(N):
    if nodes[i] == -1:
        continue
    counts[i] += counts[nodes[i]]

print(*counts)