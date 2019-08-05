N = int(input())
H = list(map(int, input().split()))

pre_h = 0
for h in H:
    if pre_h == h:
        continue
    if pre_h < h:
        pre_h = h-1
        continue
    print('No')
    break
else:
    print('Yes')
