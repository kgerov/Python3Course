import sys
import os
from os import R_OK

#fileName = input()
fileName = "Input/steps.txt"

xcoor = 0.0
ycoor = 0.0

if os.access(fileName, R_OK) and os.path.isfile(fileName) and os.stat(fileName).st_size != 0:
    with open(fileName) as f:
        for line in f:
            if len(line.strip('\n')) > 0:
                tokens = line.strip('\n').split()

                if len(tokens) != 2:
                    print("INVALID INPUT")
                    sys.exit()

                direction = tokens[0]
                try:
                    step = float(tokens[1])
                except:
                    print("INVALID INPUT")
                    sys.exit()

                if direction == "right":
                    xcoor += step
                elif direction == "left":
                    xcoor -= step
                elif direction == "up":
                    ycoor += step
                elif direction == "down":
                    ycoor -= step
                else:
                    print("INVALID INPUT")
                    sys.exit()
else:
    print('INVALID INPUT')
    sys.exit()

print("X {:.3f}".format( xcoor))
print("Y {:.3f}".format( ycoor))