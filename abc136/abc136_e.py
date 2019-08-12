N, K = map(int, input().split())
A = list(map(int, input().split()))

def get_divisors(n, reverse=False):
    from math import sqrt
    divisors = []
    for num in range(1, int(sqrt(n))+1):
        if n % num == 0:
            divisors.append(num)
            if n//num != num:
                divisors.append(n//num)
    return sorted(divisors, reverse=reverse)

total = sum(A)
divisors = get_divisors(total, reverse=True)
ans = -1
for d in divisors:
    R = [a%d for a in A]
    R.sort(reverse=True)
    pr = 0
    nr = -sum(R)
    for i, r in enumerate(R):
        pr += d-r
        nr += r
        if nr+pr >= 0:
            if pr <= K and nr+pr == 0:
                ans = d
            break
    if ans != -1:
        print(ans)
        break
else:
    print(1)
