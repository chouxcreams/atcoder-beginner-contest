#!/usr/bin/env pypy3

A, B, C = map(int, input().split())
ans = A // C * C
if A % C == 0:
    print(ans)
else:
    ans += C
    if ans <= B:
        print(ans)
    else:
        print(-1)
