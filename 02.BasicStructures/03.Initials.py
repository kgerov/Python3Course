fullname = input("Name: ").decode("utf-8")

names = fullname.split()

for i, name in enumerate(names):
    names[i] = name[0]

print(".".join(names))