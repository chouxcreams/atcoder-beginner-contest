N, M = map(int, input().split())
A = list(map(int, input().split()))
ops = [list(map(int, input().split())) for _ in range(M)]
A.sort()
ops.sort(key=lambda x:x[1], reverse=True)

a_index = 0
for op in ops:
    b, c = op
    tail = min(a_index+b, N)
    for i in range(a_index, a_index+b):
        if i >= N:
            a_index = None
            break
        if A[i] > c:
            a_index = None
            break
        A[i] = c
    else:
        a_index += b
    if a_index is None:
        break

print(sum(A))

