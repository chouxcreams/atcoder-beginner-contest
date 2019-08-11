N = int(input())
A = list(map(int, input().split()))

total_rain = sum(A) // 2

one = total_rain
for j in range(1, N-1, 2):
    one -= A[j]
rain = one*2
ans = str(rain)
prerain = rain

for m in range(1, N):
    rain = (A[m-1] - prerain//2)*2
    ans+=" "
    ans+=str(rain)
    prerain = rain

print(ans)