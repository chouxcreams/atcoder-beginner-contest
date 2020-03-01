import sys

A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = -1

for i in range(3):
    for j in range(3):
        if A[i][j] != -1:
            break
    else:
        print('Yes')
        sys.exit(0)

for i in range(3):
    for j in range(3):
        if A[j][i] != -1:
            break
    else:
        print('Yes')
        sys.exit(0)

for i in range(3):
    if A[i][i] != -1:
        break
else:
    print('Yes')
    sys.exit(0)

for i in range(3):
    if A[i][2-i] != -1:
        break
else:
    print('Yes')
    sys.exit(0)

print('No')