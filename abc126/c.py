N, K = map(int, input().split())
seq = [-1]*N
pos=N
kei = 1
count = 0
result = 0
for i in reversed(range(N)):
    while K>(i+1)*kei:
        kei*=2
        count+=1
    result += 1/kei
print(result/N)