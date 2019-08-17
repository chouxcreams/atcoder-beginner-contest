N = int(input())
A = [int(input()) for i in range(N)]
sorted_A = sorted(A, reverse=True)

max_A = sorted_A[0]

for a in A:
    if max_A != a:
        print(max_A)
    else:
        print(sorted_A[1])
