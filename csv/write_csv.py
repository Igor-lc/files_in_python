import csv

with open("cars_2.csv", "w") as f:
    space = csv.writer(f, delimiter=";", quotechar="'")

    space.writerow(["mark", "year", "country"])
    space.writerow(["Starship,Tesla", 2023, "US"])
