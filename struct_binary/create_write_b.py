import struct

products = ['свинина', 'майонез', 'морковь', 'свекла', 'сыр', 'чеснок', 'масло', 'картофель']
products.sort()

with open("products.data", "wb") as f_:
    p = struct.pack("H", products.__len__())
    f_.write(p)

with open("products.data", "ab") as f:
    for prod in products:
        prod = struct.pack("60s", prod.encode())
        f.write(prod)



# version 2
with open("products2.data", "wb") as products_file:
    products = ["свинина", "майонез", "морковь", "свекла", "сыр", "чеснок", "масло", "картофель"]
    products.sort()

    count = struct.pack("H", products.__len__())
    products_file.write(count)

    for product in products:
        product = struct.pack("60s", product.encode())
        products_file.write(product)
