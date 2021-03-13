#!/usr/bin/env pypy3
from math import ceil
A, B, W = map(int, input().split())
W *= 1000
maximum = W // A
carry = W % A
if A + carry / maximum > B:
    print("UNSATISFIABLE")
    import sys
    sys.exit()

minimum = ceil(W / B)
carry = B - W % B
if carry != B and B - carry / minimum < A:
    print("UNSATISFIABLE")
    import sys
    sys.exit()

print(minimum, maximum)
