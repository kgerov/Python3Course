import sys
import math

try:
    paper =float(input())
    boxA = float(input())
    boxB = float(input())
    boxC = float(input())
except:
    print("INVALID INPUT")
    sys.exit()

if paper <= 0 or boxA <= 0 or boxB <= 0 or boxC <= 0:
    print("INVALID INPUT")
    sys.exit()

boxArea = 2*(boxA*boxB + boxB*boxC + boxC*boxA)
print boxArea
print(math.ceil(1.098*(boxArea/(paper))))