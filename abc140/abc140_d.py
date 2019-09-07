N, K = map(int, input().split())
S = input()

r_area = 0
l_area = 0
flag = None
for i, s in enumerate(S):
    if s == "R":
        if flag == "R":
            continue
        flag = "R"
        r_area += 1
    if s == "L":
        if flag == "L":
            continue
        flag = "L"
        l_area += 1

small_area = min(r_area, l_area)
large_area = max(r_area, l_area)
if small_area <= K:
    print(N-1)
else:
    print(N-(small_area+large_area-2*K))