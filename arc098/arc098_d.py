N = int(input())
A = list(map(int, input().split()))

l = 0
r = 1
all_xor = A[0]
all_sum = A[0]
count = 0

while True:
    count += r-l
    while r < N:
        # print("l:"+str(l)+" r:"+str(r)+" xor:"+str(all_xor)+" sum:"+str(all_sum))
        all_sum += A[r]
        all_xor = all_xor ^ A[r]
        r += 1
        if all_xor == all_sum:
            count += r-l
        else:
            break
    else:
        break
    while l < r-1:
        all_sum -= A[l]
        all_xor = all_xor ^ A[l]
        l += 1
        if all_sum == all_xor:
            break
else:
    count += l-r
print(count)
