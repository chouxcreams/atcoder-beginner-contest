N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

beated_monsters = 0
for i in range(N):
    if A[i] >= B[i]:
        beated_monsters += B[i]
        continue
    else:
        beated_monsters += A[i]
        left = B[i] - A[i]
        if A[i+1] < left:
            beated_monsters += A[i+1]
            A[i+1] = 0
        else:
            beated_monsters += left
            A[i+1] -= left

print(beated_monsters)