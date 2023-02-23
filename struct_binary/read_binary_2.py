import struct

with open("film.data", "rb") as f:
    data = f.read()
    n_ru, n_en, budget, rating, date = struct.unpack('50s50sif10s', data)
    print(n_ru.decode('cp1251').rstrip("\x00"), f"({date.decode()[:4]})")


with open("film.data", "rb") as f2:
    film = f2.read()
    film = struct.unpack("50s50sif10s", film)
    name = film[0].decode("windows-1251").rstrip("\x00")
    date = film[4].decode("windows-1251").split("-")
    print("{} ({})".format(name, date[0]))


