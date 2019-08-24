N = int(input())
Sp = []
for i in range(N):
    s, p = input().split()
    Sp.append((s, int(p), i))

Sp.sort(key = lambda x: x[1], reverse=True)
Sp.sort(key = lambda x: x[0])

for sp in Sp:
    print(sp[2]+1)