N, A, B = map(int, input().split())

if N % (A+B) > A:
    left = A
else:
    left = N % (A+B)
ans = (N // (A+B)) * A + left
print(ans)