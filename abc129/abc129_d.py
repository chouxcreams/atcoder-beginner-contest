H, W = map(int, input().split())
Ss = []
for i in range(H):
    S = list(input())
    Ss.append(S)

seq = 0
w_bright_cell = [[0]*W for i in range(H)]
for i in range(H):
    seq = 0
    for j in range(W):
        if Ss[i][j] == "#":
            seq = 0
            w_bright_cell[i][j] = -1
            continue
        seq += 1
        w_bright_cell[i][j] = seq
    
    obstacle_flag = True
    for j in range(W-1, -1, -1):
        if w_bright_cell[i][j] == -1:
            obstacle_flag = True
            continue
        if obstacle_flag:
            obstacle_flag = False
            seq = w_bright_cell[i][j]
            continue
        w_bright_cell[i][j] = seq

seq = 0
h_bright_cell = [[0]*W for i in range(H)]
for j in range(W):
    seq = 0
    for i in range(H):
        if Ss[i][j] == "#":
            seq = 0
            h_bright_cell[i][j] = -1
            continue
        seq += 1
        h_bright_cell[i][j] = seq

    obstacle_flag = True
    for i in range(H-1, -1, -1):
        if h_bright_cell[i][j] == -1:
            obstacle_flag = True
            continue
        if obstacle_flag:
            obstacle_flag = False
            seq = h_bright_cell[i][j]
            continue
        h_bright_cell[i][j] = seq

now_max = 0
for i in range(H):
    for j in range(W):
        h = h_bright_cell[i][j]
        w = w_bright_cell[i][j]
        now_max = max((now_max, h+w))

print(now_max-1)