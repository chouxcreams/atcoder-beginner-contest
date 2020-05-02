import math
X = int(input())
money = 100
year = 0
while X > money:
    money *= 1.01
    money = math.floor(money)
    year += 1

print(year)