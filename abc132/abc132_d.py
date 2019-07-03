N, K = map(int, input().split())
mod = 10**9+7

import math

def combination(a, b):
    minb = min(a-b, b)
    r = 1
    for j in range(1, minb+1):
        r = r * (a-minb+j)//j
    return int(r)

for i in range(1, K+1):
    if N==K and i!=1:
        print(0)
        continue
    must = combination(K-1, i-1)
    if must is None:
        print("K:"+str(K)+", i:"+str(i))
    left_ball = N-K-i+1
    if left_ball < 0:
        print(0)
        continue
    can = combination(left_ball+i, i)
    print((must*can)%mod)
