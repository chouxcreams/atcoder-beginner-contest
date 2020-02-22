A, B, C = map(int, input().split())

if A == B or B == C or C == A:
    if A == B and B == C:
        print('No')
    else:
        print('Yes')
else:
    print('No')