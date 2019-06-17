N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
counter = 1
for l in L:
    D += l
    if D > X:
        break
    counter += 1
print(counter)