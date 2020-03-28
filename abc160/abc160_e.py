from heapq import heapify, heappush, heappop

X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
rev = lambda x: -int(x)
R = list(map(int, input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)
red = []
green = []
heapify(red)
heapify(green)

red_sum = 0
for i in range(X):
    red_sum += P[i]
    heappush(red, P[i])

green_sum = 0
for i in range(Y):
    green_sum += Q[i]
    heappush(green, Q[i])

min_p = heappop(red)
min_q = heappop(green)
for i in range(C):
    r = R[i]
    if min_p < min_q:
        if r > min_p:
            heappush(red, r)
            red_sum -= min_p
            red_sum += r
            min_p = heappop(red)
    else:
        if r > min_q:
            heappush(green, r)
            green_sum -= min_q
            green_sum += r
            min_q = heappop(green)
print(green_sum + red_sum)