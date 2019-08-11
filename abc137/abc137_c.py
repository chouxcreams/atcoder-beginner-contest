N = int(input())
S = []
for i in range(N):
    S.append(input())
anaglams = {}
count = 0
for s in S:
    chrs = [0]*26
    for c in s:
        index = ord(c) - ord('a')
        chrs[index] += 1
    if str(chrs) not in anaglams:
        anaglams[str(chrs)] = 0
    else:
        anaglams[str(chrs)] += 1
    count += anaglams[str(chrs)]
print(count)