N = int(input())

count = 0
for i in range(1, N//2+1):
    j = N - i
    if i != j:
        count += 1

print(count)