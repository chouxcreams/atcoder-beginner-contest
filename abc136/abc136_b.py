N = input()
length = len(N)

count = 0
last = 0
for i in range(length-1):
    last = i
    if i % 2 == 0:
        count += 9*(10**i)

number = int(N)
if length == 1:
    count = number
elif last%2 == 1:
    count += number + 1 - 10**(last+1)
print(count)