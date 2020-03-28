X = int(input())
h = X // 500
s = X - 500 * h
f = s // 5
print(h * 1000 + f * 5)