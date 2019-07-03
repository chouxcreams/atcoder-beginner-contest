N = int(input())
D = list(map(int, input().split()))

D.sort()

mid = int(N/2)
if D[mid - 1] == D[mid]:
    print(0)
else:
    print(D[mid] - D[mid-1])
