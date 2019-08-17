N = int(input())
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

status = [0] * N
answers = []
for i in range(N, 0, -1):
    if A[i-1] == status[i-1]:
        continue
    answers.append(i)
    divisors = get_divisors(i)
    a = A[i-1]
    for divisor in divisors:
        status[divisor-1] = (1 + status[divisor-1]) % 2

print(len(answers))
for ans in answers:
    print(ans, end=" ")
