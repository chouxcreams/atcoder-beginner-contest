N = int(input())
K = int(input())
NStr = str(N)

# def one(string):
#     L = len(string)
#     ans = (L-1)*9
#     ans += int(string[0])
#     return ans

# def two(string):
#     L = len(string)
#     ans = sum(range(L - 1)) * 81
#     head = int(string[0])
#     ans += (head - 1) * 9 * (L - 1)
#     ans += one(string[1:])
#     return ans

def A1(l):
    if l == 0:
        return 0
    return 9 * (l + 1) * l // 2

def A2(l):
    if l <= 1:
        return 0
    return 27 * l * (l + 1) * (l + 2) // 2

def A3(l):
    return l

def one(string):
    L = len(string)
    head = int(string[0])
    return A1(L-1) + head

def two(string):
    L = len(string)
    head = int(string[0])
    ans = A2(L-1)
    ans += (head - 1) * A1(L - 1)
    ans += one(string[1:])
    return ans

def three(string):
    L = len(string)
    head = int(string[0])
    ans = A3(L - 1)
    ans += (head - 1) * A2(L - 1)
    ans += two(string[1:])
    return ans

if K == 1:
    ans = one(NStr)
elif K == 2:
    ans = two(NStr)
else:
    ans = three(NStr)
    # seed = [0]*(L-1)
    # for i in range(1, L-1):
    #     seed[i] = seed[i-1] + i
    # ans = sum(seed[:L-2]) * 81 *9
    # head = int(NStr[0])
    # ans += (head-1) * 81 * (seed[L-2])
    # ans += two(NStr[1:])

print(ans)