from time import sleep
from os import remove


def inc_visitors():
    while True:
        try:
            with open("visitors.lock", "x"):
                with open("visitors.txt", "r+") as v_f:
                    visitors = int(v_f.read().strip())
                    print(visitors)
                    sleep(2)
                    v_f.seek(0)
                    v_f.write((str(visitors + 1)))
            remove("visitors.lock")
            break
        except FileExistsError:
            continue


inc_visitors()
