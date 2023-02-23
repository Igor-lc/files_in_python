import struct

products = [
    ["Tesla".encode(), 12, 43.40],
    ["starship", 7, 87.22]
]


with open('products.data', 'wb') as f:
    for product in products:
        product = struct.pack("5shf", *product)
        f.write(product)
