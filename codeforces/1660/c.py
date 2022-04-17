import sys
sys.setrecursionlimit(10000000)

t = int(input())

for _ in range(t):
    S = input()
    n = len(S)

    memo = [-1] * n


    def rcc(last, pos, ans):
        if pos == n:
            if last is None:
                return ans
            return ans + 1
        if last is None:
            if memo[pos] != -1:
                return memo[pos]
            a = rcc(S[pos], pos + 1, ans)
            b = rcc(None, pos + 1, ans + 1)
            memo[pos] = min(a, b)
            return memo[pos]
        if S[pos] == last:
            return rcc(None, pos + 1, ans)
        else:
            if ans + 1 > memo[pos] != -1:
                return memo[pos]
            return rcc(last, pos + 1, ans + 1)

    print(rcc(None, 0, 0))

