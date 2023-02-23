import struct

with open("order.data", "rb") as f:
    order = f.read()

    d_NUM, d_DATE, d_PROD, d_COUNT, d_SUM = struct.unpack("i10s70shf", order)
    Y, m, order = d_DATE.decode().split("-")
    d_date = f"{order}.{m}.{Y}"

    order = f"Заказ {d_NUM} от {d_date} на сумму {d_COUNT * d_SUM:.2f}"


'''
    print(d_NUM)
    print(d_DATE.decode())
    print(d_PROD.decode().rstrip("\x00"))
    print(d_COUNT)
    print(f"{d_SUM:.2f}")
    '''


print(order)
