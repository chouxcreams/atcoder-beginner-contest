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
