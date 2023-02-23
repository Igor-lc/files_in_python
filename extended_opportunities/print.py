p_ = ["python", "sql", "django", "git", "java"]


with open("p_list.txt", "w+") as f:
    for p in p_:
        f.write("{}\t".format(p))


with open("p_list2.txt", "w+") as f:
    print(*p_, file=f, sep=", ", end='')
