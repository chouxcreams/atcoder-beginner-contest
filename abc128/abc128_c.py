import sys
sys.setrecursionlimit(1000000000)

N, M = map(int, input().split())

lightBulbs = [None]*M
for i in range(M):
    data = list(map(int, input().split()))
    lightBulbs[i] = data[1:]

P = list(map(int, input().split()))

def rec(pos, count, status):
    if pos == N:
        count += judge(status)
        return count
    status[pos] = 0
    count = rec(pos+1, count, status)
    status[pos] = 1
    count = rec(pos+1, count, status)
    return count

def judge(status):
    for i, lightBulb in enumerate(lightBulbs):
        toggle = 0
        for switch in lightBulb:
            toggle += status[switch-1]
        toggle %= 2
        if P[i] != toggle:
            return 0
    return 1 
    

ans = rec(0, 0, [0]*N)
print(ans)
