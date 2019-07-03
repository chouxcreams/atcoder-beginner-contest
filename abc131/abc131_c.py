A, B, C, D = map(int, input().split())
count = B-A+1

import sys
sys.setrecursionlimit(1000000001)

def euclid(a, b):
    if a%b == 0:
        return b
    return euclid(b, a%b)

def how_many(num):
    ans = B//num-(A-1)//num
    return ans

count -= how_many(C)
count -= how_many(D)
E = C * D // euclid(D, C)
count += how_many(E)

print(count)