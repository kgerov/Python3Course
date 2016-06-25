import sys
import os
from os import R_OK
from datetime import datetime
import iso8601
import collections

#fileName = input()
fileName = "Input/city-temperature-data.txt"

temp_info = dict()
cities = []

if os.access(fileName, R_OK) and os.path.isfile(fileName) and os.stat(fileName).st_size != 0:
    with open(fileName) as f:
        for line in f:
            if len(line.strip('\n\t\r')) > 0:
                tokens = line.strip('\n\t\r').split(",")
                if len(tokens) != 3:
                    print("INVALID INPUT")
                    sys.exit()

                city = tokens[1]
                try:
                    date = iso8601.parse_date(tokens[0])
                    temp = float(tokens[2])
                except:
                    print("INVALID INPUT")
                    sys.exit()

                if city not in cities:
                    cities.append(city)

                if date not in temp_info:
                    temp_info[date] = []

                temp_info[date].append(city)
else:
    print("INVALID INPUT")
    sys.exit()

dates_to_remove = []

for k in temp_info.keys():
    if len(temp_info[k]) == len(cities):
        dates_to_remove.append(k)

for d in dates_to_remove:
    del temp_info[d]

if len(temp_info) == 0:
    print("ALL DATA AVAILABLE")
    sys.exit()

od = collections.OrderedDict(sorted(temp_info.items()))

for k in od.keys():
    noinfo_cities = set(od[k]).symmetric_difference(set(cities))
    print("{0},{1}".format(k.strftime("%Y-%m-%d"), ",".join(sorted(noinfo_cities))))