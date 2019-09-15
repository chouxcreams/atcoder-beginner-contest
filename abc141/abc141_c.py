import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
A = [int(input())-1 for _ in range(Q)]
answered_list = [0] * N
for a in A:
    answered_list[a] += 1

for answered in answered_list:
    if K-Q+answered > 0:
        print('Yes')
    else:
        print('No')

