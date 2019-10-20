from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        a = L[i]
        b = L[j]
        add = a+b
        sub = abs(a-b)
        head = bisect_right(L, sub)
        tail = bisect_left(L, add)
        ex = 0
        if a > sub:
            ex += 1
        if b > sub:
            ex += 1
        ans += (tail - head - ex)

print(ans//3)
