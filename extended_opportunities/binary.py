with open("cars.txt", "rb") as cars_file:
    cars = cars_file.read()
    print(cars)
    print(cars.__len__())
    for i in range(13):
        print(i, cars[i])
