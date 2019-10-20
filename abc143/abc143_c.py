N = int(input())
S = input()

decreased = 0
prev_color = ""

for s in S:
    if s == prev_color:
        decreased += 1
    prev_color = s

print(N-decreased)
