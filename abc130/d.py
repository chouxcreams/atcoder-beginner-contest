N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = 0
head = 0
tail = 0
sum_of_set = 0
while head < N:
    while tail < N and sum_of_set < K:
        sum_of_set += A[tail]
        tail += 1
    front_len = 0
    back_len = N - tail
    if tail >= N and sum_of_set < K:
        break
    while head < tail-1 and sum_of_set >= K:
        front_len += 1
        sum_of_set -= A[head]
        head += 1
    if sum_of_set < K:
        head -= 1
        sum_of_set += A[head]
        front_len -= 1
    counter += (front_len+1)*(back_len+1)
    sum_of_set -= A[head]
    head += 1
print(counter)
