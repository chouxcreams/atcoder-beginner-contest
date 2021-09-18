S1 = input()
S2 = input()
S3 = input()
T = input()

call = (S1, S2, S3)
ans = ["" for _ in range(len(T))]

for i, t in enumerate(T):
    ans[i] = call[int(t) - 1]

print("".join(ans))
