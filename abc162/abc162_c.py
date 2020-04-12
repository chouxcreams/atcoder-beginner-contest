K = int(input())


def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a%b)


ans = 0
for i in range(1, K + 1):
    for j in range(1, i + 1):
        for k in range(1, j + 1):
            tmp = euclid(i, j)
            if k < tmp:
                gcd = euclid(tmp, k)
            else:
                gcd = euclid(k, tmp)
            if i == j == k:
                ans += gcd
            elif i == j or j == k or k == i:
                ans += gcd * 3
            else:
                ans += gcd * 6
print(ans)