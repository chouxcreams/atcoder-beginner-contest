S = input()

days =  ['SUN','MON','TUE','WED','THU','FRI','SAT']

for i, day in enumerate(days):
    if day == S:
        print(7-i)