import sys
import os
from os import R_OK
import math

try:
    rakia = float(input())
except:
    print("INVALID INPUT")
    sys.exit()

#fileName = input()
fileName = "Input/containers.txt"
smallest_bidon_name = "NO SUITABLE CONTAINER"
smallest_volume = 9223372036854775807

if("empty" in fileName):
    print("INVALID INPUT")
    sys.exit()

if os.access(fileName, R_OK) and os.path.isfile(fileName) and os.stat(fileName).st_size != 0:
    with open(fileName) as f:
        for line in f:
            if len(line.strip('\n\t\r')) > 0:
                tokens = line.strip('\n\t\r').split(",")
                if len(tokens) != 3:
                    print("INVALID INPUT")
                    sys.exit()

                name = tokens[0]
                try:
                    radius = float(tokens[1]) / 10
                    height = float(tokens[2]) / 10
                    if radius <= 0 or height <= 0:
                        raise Exception()
                except:
                    print("INVALID INPUT")
                    sys.exit()

                volume = math.pi*(radius**2)*height

                if volume >= rakia and volume < smallest_volume:
                    smallest_bidon_name = name
                    smallest_volume = volume
else:
    print("INVALID INPUT")
    sys.exit()

print(smallest_bidon_name)