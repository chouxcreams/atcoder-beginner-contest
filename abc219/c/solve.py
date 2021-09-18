X = input()
N = int(input())
S = [input() for _ in range(N)]

dictionary = {}
for i, x in enumerate(X):
    dictionary[x] = i + 1


def calc(word):
    ans = 0
    for j, s in enumerate(word):
        ans += dictionary[s] * (27 ** (10 - j))
    return ans


S.sort(key=lambda x: calc(x))

for s in S:
    print(s)
