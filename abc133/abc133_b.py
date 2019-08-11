from math import sqrt

N, D = map(int, input().split())

X = []
for i in range(N):
    x_line = list(map(int, input().split()))
    X.append(x_line)

count = 0
for i in range(N):
    for j in range(i+1, N):
        dist = 0
        for d in range(D):
            dist += (X[i][d] - X[j][d])**2
        droot = sqrt(float(dist))
        if droot.is_integer():
            count += 1

print(count)