t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    if n == 1:
        if A[0] == 1:
            print('Yes')
        else:
            print('NO')
    else:
        A.sort(reverse=True)
        if A[0] - A[1] >= 2:
            print('NO')
        else:
            print('YES')
