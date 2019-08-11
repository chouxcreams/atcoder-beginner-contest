N = int(input())
P = list(map(int, input().split()))

flg = None
for i, p in enumerate(P):
    index = i+1
    if index != p:
        if P[p-1] == index and ((not flg) or index==flg):
            flg = p
        else:
            print('NO')
            break
else:
    print('YES')