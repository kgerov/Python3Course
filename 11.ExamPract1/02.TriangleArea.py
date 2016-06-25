import sys
import math

try:
    a = float(input())
    b = float(input())
    c = float(input())
except:
    print("INVALID INPUT")
    sys.exit()

p = (a + b + c) / 2.0

S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("{:.2f}".format(S))