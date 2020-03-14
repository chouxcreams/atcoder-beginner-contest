a, b, c = map(int, input().split())

T = c - a - b
if T < 0:
    print('No')
elif T ** 2 > 4 * a * b:
    print('Yes')
else:
    print('No')