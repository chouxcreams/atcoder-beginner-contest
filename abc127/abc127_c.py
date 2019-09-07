import sys
input = sys.stdin.readline

N, M = map(int, input().split())
gates = [list(map(int, input().split())) for _ in range(M)]

leftest = 1
rightest = N
for gate in gates:
    L = gate[0]
    R = gate[1]
    if L > leftest:
        if L > rightest:
            print(0)
            break
        leftest = L
    if R < rightest:
        if R < leftest:
            print(0)
            break
        rightest = R
else:
    print(rightest - leftest + 1)