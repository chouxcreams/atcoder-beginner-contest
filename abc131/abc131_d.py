N = int(input())
A=[0]*N
B=[0]*N
class Job:
    def __init__(self, a, b):
        self.time = a
        self.limit = b

jobs = []
for i in range(N):
    A, B = map(int, input().split())
    jobs.append(Job(A, B))

jobs.sort(key = lambda job: job.limit)
used_time = 0
for job in jobs:
    used_time += job.time
    if used_time > job.limit:
        print("No")
        break
else:
    print("Yes")