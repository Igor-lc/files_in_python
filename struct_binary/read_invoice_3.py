# version 3

import struct
with open("bill.data", "rb") as f:
    bill = f.read()

    meta_format = "h10sh"
    meta_length = struct.calcsize(meta_format)
    product_format = "100shf"
    product_length = struct.calcsize(product_format)

    meta = struct.unpack(meta_format, bill[:meta_length])
    data = struct.unpack(product_format * meta[2], bill[meta_length:])

    count = data[1::3]
    price = data[2::3]

    summ = 0; x = 0

    for i in count:
        summ += i * price[x]
        x += 1

print(f"{summ:.2f}")
