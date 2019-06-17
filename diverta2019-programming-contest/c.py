from collections import deque

N = int(input())
inpt = input()
A = [int(a) for a in inpt.split()]
A = deque(sorted(A))
outputs = []
negative = 0
positive = 0

for a in A:
    if a > 0:
        positive += 1
    elif a <= 0:
        negative += 1
for i in range(N-1):
    maxA = A[-1]
    minA = A[0]
    if minA>0:
        positive -= 1
    else:
        negative -= 1
    if maxA>0:
        positive -= 1
    else:
        negative -= 1
    A.pop()
    A.popleft()
    if positive > negative:
        newnum = minA-maxA
        A.appendleft(newnum)
        outputs.append(str(minA)+" "+str(maxA))
    else:
        newnum = maxA - minA
        A.append(newnum)
        outputs.append(str(maxA)+" "+str(minA))
    if newnum > 0:
        positive += 1
    else:
        negative += 1

print(A[0])
for output in outputs:
    print(output)
