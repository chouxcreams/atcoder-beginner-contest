S = input()
T = input()

if len(S) + 1 != len(T):
    print('No')
else:
    for i in range(len(S)):
        if S[i] != T[i]:
            print('No')
            break
    else:
        print('Yes')