N = int(input())

def get_divisors(n, reverse=False):
    from math import sqrt
    divisors = []
    for num in range(1, int(sqrt(n))+1):
        if n % num == 0:
            divisors.append(num)
            divisors.append(n//num)
    return sorted(divisors, reverse=reverse)

divisors = get_divisors(N)

l = len(divisors)
ans = float('inf')
for i in range(l//2):
    ans = min(ans, divisors[i] + divisors[l - 1 - i])
print(ans-2)