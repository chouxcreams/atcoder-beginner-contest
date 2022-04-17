#!/usr/bin/env pypy3
S = input()
notChecked = [False] * 10

for s in S:
    notChecked[int(s)] = True

for i in range(10):
    if not notChecked[i]:
        print(i)
        break
