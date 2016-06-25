exchangeFile = input()
amountsFile = input()

exchangeRates = dict()

with open('DataFiles/' + exchangeFile) as f:
    for line in f:
        tokens = line.split()
        exchangeRates[tokens[0]] = float(tokens[1])

with open('DataFiles/' + amountsFile) as f:
    for line in f:
        tokens = line.split()
        amount = float(tokens[0])
        currency = tokens[1]
        print("{:.2f}".format(amount/exchangeRates[currency]))

