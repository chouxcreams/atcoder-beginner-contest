N = int(input())
D = {}
ans = []
ansval = 0
for _ in range(N):
    s = input()
    if s not in D:
        D[s] = 1
    else:
        D[s] += 1
    if ansval == D[s]:
        ans.append(s)
    elif ansval < D[s]:
        ans = [s]
        ansval = D[s]
ans.sort()
for a in ans:
    print(a)