#!/usr/bin/env pypy3
N = input()

if len(N) % 2 == 1:
    n = (len(N) - 1) // 2
    ans = 10 ** n - 1
else:
    former, later = 0, 0
    for i, n in enumerate(N):
        if i < len(N) // 2:
            former *= 10
            former += int(n)
        else:
            later *= 10
            later += int(n)
    if former > later:
        ans = former - 1
    else:
        ans = former
print(ans)
