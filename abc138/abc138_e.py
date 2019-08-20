from bisect import bisect_left
import sys
s = input()
t = input()

alpha = [[] for _ in range(26)]
c2i = lambda x: ord(x) - ord('a')

for i, sl in enumerate(s):
    alpha[c2i(sl)].append(i)

pos = -1
count = 0
length = len(s)
for tl in t:
    places = alpha[c2i(tl)]
    if len(places) == 0:
        print(-1)
        break

    index = bisect_left(places, pos+1)
    if index != len(places):
        place = places[index]
        count += place - pos
        pos = place
    else:
        count += (length-pos-1) + places[0] + 1
        pos = places[0]
else:
    print(count)