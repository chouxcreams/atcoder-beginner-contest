N = int(input())
WholeS = input()

ans = 0
for l in range(N):
    # Z-algorithm
    A = [-1]*(N-l)
    c = 0
    S = WholeS[l:]
    for i, s in enumerate(S):
        if i == 0:
            continue
        if c+A[c] > i+A[i-c]:
            A[i] = A[i-c]
        else:
            j = max(0, A[c]-i+c)
            while i+j < N-l and S[j] == S[i+j]:
                j += 1
            A[i] = j
            c = i
        ans = max(ans, A[i] if(i>A[i]) else i)

print(ans)
