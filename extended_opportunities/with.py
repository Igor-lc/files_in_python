lower = open("lower.txt", "r", encoding="utf8")
upper = open("upper.txt", "w", encoding="utf8")
for line in lower.readlines():
    upper.write(line.upper())
upper.close()
lower.close()


with open("lower_.txt", "r") as lower, open("upper_.txt", "w") as upper_:
    for line in lower.readlines():
        upper_.write(line.upper())
