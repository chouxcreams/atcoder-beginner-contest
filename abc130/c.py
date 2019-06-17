W, H, x, y= map(int, input().split())
S = W*H/2
flg = 1 if (x==W/2 and y==H/2) else 0
print('{:.6f}'.format(S)+" "+str(flg))