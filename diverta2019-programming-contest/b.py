N = int(input())
x = []
y = []
for i in range(N):
    new_x, new_y = map(int, input().split())
    x.append(new_x)
    y.append(new_y)

dist_list = []
count_list = []
for i in range(N):
    for j in range(i+1, N):
        p = x[i] - x[j]
        q = y[i] - y[j]
        for index, dist in enumerate(dist_list):
            x_dist, y_dist= dist
            if (x_dist == p and y_dist == q) or (x_dist == -p and y_dist == -q):
                count_list[index] += 1
                break
        else:
            dist_list.append([p, q])
            count_list.append(1)

if N == 1:
    print(1)
else:
    print(N - max(count_list))