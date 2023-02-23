import csv

with open("cars.csv") as f:
    space = csv.reader(f, delimiter=";", quotechar="'")
    print(space)

    for i in space:
        print(i)

print()


with open("cars.csv") as f2:
    space = csv.DictReader(f2, delimiter=";", quotechar="'")
    print(space)

    for i in space:
        print(i)
