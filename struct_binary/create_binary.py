import struct


with open("scientist.bin", 'wb') as f:
    scientist = struct.pack("50s50shh", 'Альберт'.encode(), 'Эйнштейн'.encode(), 1879, 1955)
    f.write(scientist)


first_name = 'Альберт'.encode()
last_name = 'Эйнштейн'.encode()
year_of_birth = 1879
year_of_death = 1955

with open("scientist_2.bin", "wb") as f2:
    scientist = struct.pack("50s50shh", first_name, last_name, year_of_birth, year_of_death)
    f2.write(scientist)
