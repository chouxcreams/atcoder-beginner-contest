from math import atan, pi
a, b, x = map(int, input().split())
if (x/a > (a*b)/2):
    d = 2*x/(a**2) - b
    rad = atan((b-d)/a)
    print(rad*180/pi)
else:
    d = 2*x / (a*b)
    rad = atan(b/d)
    print(rad*180/pi)
