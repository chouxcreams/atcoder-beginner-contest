import sys
L, R = map(int, input().split())

if R-L >= 2018:
    print(0)
    sys.exit()

min_mod = 2019
for i in range(L, R+1):
    for j in range(i+1, R+1):
        mod = (i*j)%2019
        min_mod = mod if min_mod > mod else min_mod
print(min_mod)