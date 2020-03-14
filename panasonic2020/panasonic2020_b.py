H, W = map(int, input().split())
w = W // 2
h = H // 2
lh = H - h
lw = W - w

if H < 2 or W < 2:
    print(1)
else:
    print(lh * lw + w * h)