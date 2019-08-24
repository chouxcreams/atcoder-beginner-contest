import sys
import time
from queue import Queue
limit_time = time.time() + 1.70
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

N, M, P = map(int, input().split())

A = [-1]*M
B = [-1]*M
C = [-1]*M
nodes_edges = [[] for _ in range(N)]
rev_nodes_edges = [[] for _ in range(N)]
coin = [-float('inf')]*N
coin[0] = 0
availables = set()

for edge in range(M):
    a, b, c = map(int, input().split())
    A[edge] = a-1
    B[edge] = b-1
    C[edge] = c-P
    nodes_edges[a-1].append(edge)
    rev_nodes_edges[b-1].append(edge)

def cut_graph(node):
    edges = rev_nodes_edges[node]
    availables.add(node)
    for edge in edges:
        prev = A[edge]
        if prev in availables:
            continue
        cut_graph(prev)

cut_graph(N-1)
q = Queue()
q.put(0)
count = 0
limit = M*(1+len(availables))
while not q.empty():
    if time.time() >= limit_time:
        print(-1)
        break
    node = q.get()
    edges = nodes_edges[node]
    for edge in edges:
        nxt = B[edge]
        if nxt not in availables:
            continue
        new_coin = C[edge]+coin[node]
        if new_coin > coin[nxt]:
            coin[nxt] = new_coin
            q.put(nxt)
    count += 1
else:
    ans = coin[N-1]
    ans = 0 if ans < 0 else ans
    print(ans)
