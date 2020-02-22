from bisect import bisect_left, bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
posi = N - bisect_right(A, 0)
nega = bisect_left(A, 0)
zeroes = N - (posi+nega)
if nega * posi > K:
    k = 0
    head = 0
    tail = N - 1
    for _ in range(N):
        print(nega, posi)
        numPosi = posi-(N-tail) + 1
        numNega = nega - head
        if numNega + numPosi + k < K:
            k = numNega + numPosi
            head += 1
            tail -= 1
            continue
        ks = []
        for i in range(numPosi):
            index = tail - i - 1
            ks.append(A[index] * A[head])
        for i in range(1, numNega):
            index = head + 1 + i
            ks.append(A[index] * A[tail])
        ks.sort()
        print(ks)
        print(ks[K-k+1])
elif zeroes * (nega + posi) < K - (nega*posi):
    print(0)
else:
    pass
