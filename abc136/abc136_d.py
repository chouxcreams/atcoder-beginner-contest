S = input()
N = len(S)
cells = [0]*N

seq = 0
for i, s in enumerate(S):
    if s == 'R':
        seq += 1
        cells[i] = seq
        continue
    seq = 0

rev_S = S[::-1]
seq = 0
for i, s in enumerate(rev_S):
    if s == 'L':
        seq += 1
        cells[N-1-i] = seq
        continue
    seq = 0

ans = [0]*N
pre_cell = 0
pre_s = 'R'
l_flag =False
for i, s in enumerate(S):
    cell = cells[i]
    if pre_s == 'R' and s == 'L':
        ans[i] = cell//2 + cell%2 + pre_cell//2
        ans[i-1] = pre_cell//2 + pre_cell % 2 + cell//2
    pre_s = s
    pre_cell = cell

ans_str = ""
for a in ans:
    ans_str += str(a)+" "
print(ans_str)