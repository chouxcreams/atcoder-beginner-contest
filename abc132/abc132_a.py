S = input()
one = 0
two = 0
strs = ["", ""]

for s in S:
    if strs[0] == s:
        one += 1
    elif strs[1] == s:
        two += 1
    elif strs[0] == "":
        strs[0] = s
        one += 1
    elif strs[1] == "":
        strs[1] = s
        two += 1
    else:
        print("No")
        break
    if one > 2 or two > 2:
        print("No")
        break
else:
    print("Yes")