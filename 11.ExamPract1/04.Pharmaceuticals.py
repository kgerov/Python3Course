import sys
import itertools

def fitsInBox(dimMed, dimBox):
    outer_comb = itertools.permutations(dimBox, 3)
    inner_comb = itertools.permutations(dimMed, 3)
    for o in outer_comb:
        for i in inner_comb:
            if o[0] >= i[0] and o[1] >= i[1] and o[2] >= i[2]:
                return True
    return False

try:
    a = float(input())
    b = float(input())
    c = float(input())
except:
    print("INVALID INPUT")
    sys.exit()

#fileName = input()
fileName = "DataFiles/packages.txt"
medicine = dict()

with open(fileName) as f:
    for line in f:
        if len(line.strip('\n')) > 0:
            tokens = line.strip('\n').split(',')
            dim = [float(tokens[1]), float(tokens[2]), float(tokens[3])]
            if fitsInBox(dim, [a, b, c]):
                print(tokens[0])
for m in medicine:
    if fitsInBox(medicine[m], [a, b, c]):
        print(m)