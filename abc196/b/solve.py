#!/usr/bin/env pypy3

X = input()
if '.' in X:
    ans, _ = X.split('.')
else:
    ans = X
print(ans)
