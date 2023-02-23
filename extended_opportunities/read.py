with open("cities.txt") as cities_file:
    cities = cities_file.read().strip().split(",")
    print(cities)


with open("cities_2.txt") as cities_file_2:
    print(cities_file_2.readlines())


with open("cities_2.txt") as cities_file_2:
    cities = []
    for citi in cities_file_2:
        if citi.__len__() < 8:
            cities.append(citi.strip())
    print(cities)
