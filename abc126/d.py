N=int(input())
u=[0]*N
v=[0]*N
w=[0]*N
for i in range(N-1):
    u[i], v[i], w[i] = map(int, input().split())

class Path:
    def __init__(self, next, length, num):
        self.next=next
        self.len=length
        self.num=num

class Node:
    def __init__(self, index):
        self.index = index
        self.paths = []

    def append(self, next, length, num):
        self.paths.append(Path(next, length, num))

nodes = [Node(i) for i in range(N)]
for i in range(N-1):
    nodes[u[i]-1].append(v[i]-1, w[i], i)
    nodes[v[i]-1].append(u[i]-1, w[i], i)

pasts = []
paints = [-1]*N

def rec(pos, color):
    if paints[pos] == -1:
        paints[pos] = color
    for path in nodes[pos].paths:
        # まだ通ってない道を通る
        if path.num not in pasts:
            pasts.append(path.num)
            if path.len % 2 == 1:
                rec(path.next, (color + 1) % 2)
            else:
                rec(path.next, color)
        # さっきの道を戻ってくる

rec(0, 0)

for i in paints:
    print(i)