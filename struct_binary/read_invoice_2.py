# version 2

import struct
with open("bill.data", "rb") as bill_file:
    bill = bill_file.read()

    meta_format = "h10sh"
    product_format = "100shf"

    # Вычисляем количество байт для хранения мета данных и данных о товаре
    meta_length = struct.calcsize(meta_format)
    product_length = struct.calcsize(product_format)

    meta = struct.unpack(meta_format, bill[:meta_length])
    products_count = meta[2]

    sum = 0
    for i in range(products_count):
        product = bill[meta_length + (i * product_length):
                       meta_length + (i * product_length + product_length)]
        product = struct.unpack(product_format, product)
        sum += product[1] * product[2]

    print("{:.2f}".format(sum))
