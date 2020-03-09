N = int(input())
S = list(input())
c2i = lambda c: ord(c) - ord('A')
i2c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i, s in enumerate(S):
    index = c2i(s)
    index += N
    if index >= 26:
        index -= 26
    S[i] = i2c[index]

print(''.join(S))