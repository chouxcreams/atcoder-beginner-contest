S=int(input())
head=int(S/100)
tail=S-head*100
head_can_month = head<=12 and head>=1
tail_can_month = tail<=12 and tail>=1
if head_can_month:
    if tail_can_month:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if tail_can_month:
        print("YYMM")
    else:
        print("NA")