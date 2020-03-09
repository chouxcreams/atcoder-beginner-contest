import sys
sys.setrecursionlimit(1000000000)

A, B, X = map(int, input().split())


def val(N, dN):
    return A * N + B * dN

cmp = 0
prev = 0
for power in range(9):
    cmp += 9 * (10**power)
    dN = power + 1
    value = val(cmp, dN)
    if value > X:
        break
    prev = cmp
else:
    if val(1000000000, 10) <= X:
        print('1000000000')
    else:
        print(cmp)
    sys.exit()


def bis(s, l):
    if l - s == 1:
        return s
    m = (s + l) // 2
    if val(m, dN) > X:
        return bis(s, m)
    else:
        return bis(m, l)


ans = bis(prev, cmp)
print(ans)
