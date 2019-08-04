A, B, C = map(int, input().split())
ans = C+B-A
if ans < 0:
    ans = 0
print(ans)