N = int(input())
H = list(map(int, input().split()))

max_step = 0
count = 0
prev_h = -float('inf')
for h in H:
    if h > prev_h:
        count = 0
    else:
        count += 1
    max_step = max(count, max_step)
    prev_h = h
print(max_step)
