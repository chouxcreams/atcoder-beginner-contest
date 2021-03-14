S = input()
c2i = lambda c: ord(c) - ord('A')
for i, s in enumerate(S):
    if i % 2 == 1 and c2i(s) >= 26:
        print('No')
        break
    if i % 2 == 0 and c2i(s) < 26:
        print('No')
        break
else:
    print('Yes')
