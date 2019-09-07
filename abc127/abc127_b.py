import sys
input = sys.stdin.readline
r, D, prev_x = map(int, input().split())

for y in range(1, 11):
    x = r*prev_x - D
    print(x)
    prev_x = x