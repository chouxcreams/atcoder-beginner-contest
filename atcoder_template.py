map(int, input().split())
list(map(int, input().split()))
int(input())

# nの[素因数, その数]のリストを返す
def prime_factoring(n):
    from math import sqrt
    factors = []
    for num in range(2, int(sqrt(n))+1):
        print(num)
        if n % num == 0:
            count = 0
            while(n % num == 0):
                n //= num
                count += 1
            factors.append([num, count])
    else:
        factors.append([n, 1])
    return factors

# Character to Index
c2i = lambda c: ord(c) - ord('a')

def get_divisors(n, reverse=False):
    from math import sqrt
    divisors = []
    for num in range(1, int(sqrt(n))+1):
        if n % num == 0:
            divisors.append(n//num)
            if n//num != num:       
                divisors.append(n//num)
    return sorted(divisors, reverse=reverse)

import sys
sys.setrecursionlimit(1000000000)

import sys
input = sys.stdin.readline

from heapq import heapify, heappush, heappop

def cmb(n, r):
    if n<0 or r<0 or r>n:
        return None
    r = min(r, n-r)
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [0]*r
    denominator = [0]*r
    for k in range(r):
        numerator[k] = n-r+k+1
        denominator[k] = k+1
    for p in range(2, r+1):
        pivot = denominator[p-1]
        if pivot > 1:
            offset = (n-r) % p
            for k in range(p-1, r, p):
                numerator[k-offset] //= pivot
                denominator[k] //= pivot
    res = 1
    for n in numerator:
        if n > 1:
            res *= n
    return res