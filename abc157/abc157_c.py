N, M = map(int, input().split())
S = [0]*M
C = [0]*M
num = [-1]*N

for i in range(M):
    s, c = map(int, input().split())
    if num[s-1] == -1:
        num[s-1] = c
    elif num[s-1] == c:
        continue
    else:
        print(-1)
        break
else:
    if num[0] == 0:
        if N == 1:
            print(0)
        else:
            print(-1)
    else:
        for i in range(N):
            if num[i] == -1:
                if i == 0 and N != 1:
                    num[i] = 1
                    continue
                num[i] = 0
        print(''.join(map(str, num)))