from collections import deque

N = int(input())
S = input()
rgb = {"R":0, "G":0, "B":0}
RGBs = 0
for s in S:
    rgb[s] += 1

for i in range(N):
    tail = (N - 1 - i) // 2
    for d in range(1, tail + 1):
        Si = S[i]
        Sj = S[i + d]
        Sk = S[i + d * 2]
        if Si == Sj or Sj == Sk or Sk == Si:
            continue
        RGBs += 1

ans = rgb["R"] * rgb["G"] * rgb["B"] - RGBs
print(ans)