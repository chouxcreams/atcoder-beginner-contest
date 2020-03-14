import sys
sys.setrecursionlimit(1000000000)

N = int(input())
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
seed = ['a'] * N

def rec(S, depth, count):
    if depth == N:
        print(''.join(S))
        return
    for i in range(count+1):
        S.append(data[i])
        if i == count:
            count += 1
        rec(S, depth+1, count)
        S.pop()

rec([], 0, 0)
