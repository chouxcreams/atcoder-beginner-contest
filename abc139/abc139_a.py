S = input()
T = input()

count = 0
for i in range(3):
    count += 1 if S[i] == T[i] else 0
print(count)
