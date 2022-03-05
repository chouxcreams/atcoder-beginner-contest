#!/usr/bin/env pypy3
import copy

N = int(input())
MOD = 998244353

ls = [1] * 9
ls_new = [1] * 9
for _ in range(N - 1):
    for j in range(9):
        if j == 0:
            ls_new[j] = (ls[j] + ls[j + 1]) % MOD
        elif j == 8:
            ls_new[j] = (ls[j] + ls[j - 1]) % MOD
        else:
            ls_new[j] = (ls[j - 1] + ls[j] + ls[j + 1]) % MOD
    ls = copy.copy(ls_new)

print(sum(ls_new) % MOD)
