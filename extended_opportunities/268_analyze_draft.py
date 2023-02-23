# version_2
from sys import argv
from datetime import datetime as dt
d = dt.strptime(argv[1], "%d.%m.%Y")
date = d.strftime("%d/%b/%Y")

paths = []
with open("server.log") as server_log:
    fi = server_log.readlines()

    for i in fi:
        ip, date_time, type, path, protocol, code = i.split(' ')
        if path not in paths:
            for i in fi:
                ip, date_time, type, path_, protocol, code = i.split(' ')
                date_log, hh, mm, ss = date_time.split(":")
                date_log = date_log[1:]

                if path == path_ and date == date_log:
                    paths.append(path)

count_ = 0
finish_path, path_count = 0, 0
for p in paths:
    for p_ in paths:
        if p == p_:
            count_ += 1
            if path_count < count_:
                finish_path, path_count = p, count_
    count_ = 0

print(finish_path, path_count)
