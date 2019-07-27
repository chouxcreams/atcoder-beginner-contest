D = 10**9+7
S = input()
mod_table = [[0]*13]
mod_table[0][0] = 1

for i, s in enumerate(S):
    mod_table.append([0]*13)
    if s == "?":
        for num in range(10):
            for d in range(13):
                mod_table[i+1][(d*10+num)%13] += mod_table[i][d]
    else:
        num = int(s)
        for d in range(13):
            mod_table[i+1][(d*10+num)%13] += mod_table[i][d]
    mod_table[i+1] = [m%D for m in mod_table[i+1]]

print(mod_table[-1][5] % D)