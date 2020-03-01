import sys
sys.setrecursionlimit(1000000000)

N, M, K = map(int, input().split())

class Account:
    def __init__(self, val):
        self.val = val
        self.friends = []
        self.valid_blocks = 0
        self.graph = 0


def rec(index, past, graph):
    past.add(index)
    graph.add(index)
    account = accounts[index]
    account.graph = count
    for friend in account.friends:
        if friend in past:
            continue
        past, graph = rec(friend, past, graph)
    return past, graph


accounts = [Account(i - 1) for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    accounts[a-1].friends.append(b - 1)
    accounts[b-1].friends.append(a - 1)

past = set()
graphs = []
count = 0
for i in range(N):
    if i in past:
        continue
    past, graph = rec(i, past, set())
    graphs.append(graph)
    count += 1

for _ in range(K):
    c, d = map(int, input().split())
    C = accounts[c-1]
    D = accounts[d-1]
    if C.graph == D.graph:
        C.valid_blocks += 1
        D.valid_blocks += 1

answers = [0]*N
for i, account in enumerate(accounts):
    answers[i] = len(graphs[account.graph]) - len(account.friends) - 1 - account.valid_blocks

print(*answers)