import struct, csv

with open("sport_food.csv", "r", encoding='windows-1251') as sport_food_file:

    # Подключаем CSV файл
    food_reader = csv.DictReader(sport_food_file, delimiter=',', quotechar='"')

    products = []
    for row in food_reader:
        products.append(row)

    with open("sport_food_2.bin", "wb") as products_file:
        count = struct.pack("I", products.__len__())
        products_file.write(count)

        for prod in products:
            prod = struct.pack(
                "100sHH",
                prod["Название"].encode(),
                int(prod["Вес"]),
                int(prod["Стоимость"])
            )
            products_file.write(prod)
