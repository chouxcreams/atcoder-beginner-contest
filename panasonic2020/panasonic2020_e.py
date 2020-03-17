a = list(input())
b = list(input())
c = list(input())
A, B, C = map(len, (a, b, c))
OFFSET = 4000
L = 8001
ab = [True] * L
ac = [True] * L
bc = [True] * L

for i in range(A):
    for j in range(B):
        if a[i] != b[j] and a[i] != '?' and b[j] != '?':
            k = i - j + OFFSET
            ab[i - j + OFFSET] = False  # BをAからi-jずらした時を考える

for i in range(A):
    for j in range(C):
        if a[i] != c[j] and a[i] != '?' and c[j] != '?':
            ac[i - j + OFFSET] = False  # CをAからi-jずらした時を考える

for i in range(B):
    for j in range(C):
        if b[i] != c[j] and b[i] != '?' and c[j] != '?':
            bc[i - j + OFFSET] = False  # CをBからi-jずらした時を考える

ans = float('inf')
for i in range(L):  # Bの左端をずらす
    for j in range(L):  # Cの左端をずらす
        k = j - i + OFFSET
        if k >= L or k < 0:
            continue
        if ab[i] and ac[j] and bc[k]:
            head = min(i, j, OFFSET)
            tail = max(A + OFFSET, B + i, C + j)
            ans = min(ans, tail - head)

print(ans)
