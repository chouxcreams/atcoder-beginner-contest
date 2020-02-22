N = int(input())
A = list(map(int, input().split()))

exists = set()

for a in A:
    if a in exists:
        print('NO')
        break
    exists.add(a)
else:
    print('YES')