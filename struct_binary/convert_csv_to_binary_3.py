import struct, csv

with open("sport_food.csv", encoding='windows-1251') as f:
    with open("sport_food.bin", "wb") as f2:
        products = csv.DictReader(f)

        x = 0
        new = struct.pack("I", x)
        f2.write(new)
        for i in products:
            prod = struct.pack(
                "100sHH",
                i['Название'].encode(encoding="UTF-8"),
                int(i['Вес']),
                int(i['Стоимость'])
            )
            f2.write(prod)
            x += 1

        f2.seek(0)
        new_2 = struct.pack("I", x)
        f2.write(new_2)
