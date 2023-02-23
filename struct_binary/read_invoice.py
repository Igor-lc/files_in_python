# version 1

import struct
with open("bill.data", "rb") as f:
    bill = f.read()
    b = struct.unpack("h10sh", bill[:14])
    data = struct.unpack("100shf" * b[2], bill[14:])

    count = data[1::3]
    price = data[2::3]

    summ = 0; x = 0

    for i in count:
        summ += i * price[x]
        x += 1

print(f"{summ:.2f}")
