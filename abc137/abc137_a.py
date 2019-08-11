A, B = map(int, input().split())
plus = A+B
minus = A - B
cross = A*B
print(max([plus, minus, cross]))
