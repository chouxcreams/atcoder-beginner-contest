from fractions import gcd
A, B = map(int, input().split())
G = gcd(A, B)

# nの[素因数, その数]のリストを返す
def prime_factoring(n):
    from math import sqrt
    factors = []
    for num in range(2, int(sqrt(n))+1):
        if n % num == 0:
            count = 0
            while(n % num == 0):
                n //= num
                count += 1
            factors.append([num, count])
    else:
        if n != 1:
            factors.append(n)
    return factors

print(len(prime_factoring(G))+1)
