#!/usr/bin/env pypy3

H, W, A, B = map(int, input().split())

tiles = [[0 for _ in range(W)] for _ in range(H)]


def func(h, w, a, b, ans):
    if w < W - 1:
        next_h, next_w = h, w + 1
    elif h < H - 1:
        next_h, next_w = h + 1, 0
    else:
        return ans + 1
    if tiles[h][w] != 1:
        tiles[h][w] = 1
        if h + 1 < H:
            if tiles[h + 1][w] != 1 and a > 0:
                tiles[h + 1][w] = 1
                ans = func(next_h, next_w, a - 1, b, ans)
                tiles[h + 1][w] = 0
        if w + 1 < W:
            if tiles[h][w + 1] != 1 and a > 0:
                tiles[h][w + 1] = 1
                ans = func(next_h, next_w, a - 1, b, ans)
                tiles[h][w + 1] = 0
        if b > 0:
            ans = func(next_h, next_w, a, b - 1, ans)
        tiles[h][w] = 0
    else:
        ans = func(next_h, next_w, a, b, ans)
    return ans


print(func(0, 0, A, B, 0))
