S = input()

prev = 'i'
for s in S:
    if s == 'h' and prev == 'i':
        pass
    elif s == 'i' and prev == 'h':
        pass
    else:
        print('No')
        break
    prev = s
else:
    if prev == "h":
        print('No')
    else:
        print('Yes')