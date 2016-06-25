import sys

text = input()
maxReps = 0
maxChar = ''

if not text:
    print("INVALID INPUT")
    sys.exit()

letters = dict()

for c in text:
    if c in letters:
        letters[c] = letters[c] + 1
    else:
        letters[c] = 1
    if letters[c] > maxReps:
        maxReps = letters[c]
        maxChar = c

print(maxChar)
