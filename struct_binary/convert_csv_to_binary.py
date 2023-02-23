import struct

with open("sport_food.csv", "rb") as f:
    a = f.read()
    a = a.decode("windows-1251").split("\n")
    count = a[1:].__len__()

    products = []
    for i in a[1:]:
        a, b, c = i.replace('"', '').split(',')
        products.append([a.encode(), int(b), int(c)])

    with open("sport_food.bin", "wb") as f2:
        f2.write(struct.pack("I", count))

        for prod in products:
            prod = struct.pack('100sHH', *prod)
            f2.write(prod)
