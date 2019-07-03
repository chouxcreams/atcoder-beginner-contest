S = input()
pres = ""
for s in S:
    if pres == s:
        print('Bad')
        break
    pres = s
else:
    print('Good')