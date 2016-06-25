import sys
import os
from os import R_OK
from datetime import datetime
import iso8601
import collections

#fileName = input()
fileName = "Input/salex.txt"

products = dict()

if os.access(fileName, R_OK) and os.path.isfile(fileName) and os.stat(fileName).st_size != 0:
    with open(fileName) as f:
        for line in f:
            if len(line.strip('\n\t\r')) > 0:
                tokens = line.strip('\n\t\r').split(",")
                if len(tokens) != 5:
                    print("INVALID INPUT")
                    sys.exit()

                product = tokens[0].strip("\"\'")
                country = tokens[1]
                city = tokens[2].strip("\"\'")

                try:
                    date = iso8601.parse_date(tokens[3].strip("\"\'"))
                    price = float(tokens[4])
                except:
                    print("INVALID INPUT")
                    sys.exit()

                if product not in products:
                    products[product] = []

                if city not in products[product]:
                    products[product].append(city)
else:
    print("INVALID INPUT")
    sys.exit()

products_to_remove = []
cities = dict()

for k in products.keys():
    if len(products[k]) == 1:
        if  products[k][0] not in cities:
            cities[products[k][0]] = []
        cities[products[k][0]].append(k)


if len(cities) == 0:
    print("NO UNIQUE SALES")
    sys.exit()

od = collections.OrderedDict(sorted(cities.items()))

for k in od.keys():
    print("{0},{1}".format(k, ",".join(sorted(od[k]))))