N, X, Y = map(int, input().split())
X -= 1
Y -= 1
circle = Y - X + 1

D = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if i < X and X <= j <= Y:
            start_to_ent = X - i
            ent_to_goal = j - X
            d = min(ent_to_goal, circle - ent_to_goal) + start_to_ent
            D[d] += 1
        elif X <= i <= Y and X <= j <= Y:
            start_to_goal = j - i
            d = min(start_to_goal, circle - start_to_goal)
            D[d] += 1
        elif X <= i <= Y and Y < j:
            start_to_ent = j - Y
            ent_to_goal = Y - i
            d = min(ent_to_goal, circle - ent_to_goal) + start_to_ent
            D[d] += 1
        elif i < X and Y < j:
            start_to_ent = X - i
            ent2_to_goal = j - Y
            r = Y - X
            d = start_to_ent + min(r, circle-r) + ent2_to_goal
            D[d] += 1
        else:
            d = j - i
            D[d] += 1

for i in range(1, N):
    print(D[i])
