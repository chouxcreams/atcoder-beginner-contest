N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

prev_a = 0
satisfaction = sum(B)
for a in A:
    if prev_a + 1 == a and prev_a > 0:
        satisfaction += C[prev_a-1]
    prev_a = a

print(satisfaction)