N = int(input())
A = list(map(int, input().split()))

total = 0
for a in A:
    total += 1/a

print(1/total)