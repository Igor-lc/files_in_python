'''Когда вы заходите на сайт, web-сервер сохраняет информацию
 о посещении в лог-файл. Напишите программу, которая будет анализировать
  лог-файл и выводить самую посещаемую страницу за определенную дату.
  Дату получаем из аргумента командной строки в формате ДД.ММ.ГГГГ.
  Программа должна выводить адрес страницы и количество посещений.'''
# version_1
import sys
from datetime import datetime as dt
search_date = sys.argv[1]
search_date = dt.strptime(search_date, "%d.%m.%Y")

paths = {}
with open("server.log") as server_log:
    for line in server_log:
        ip, date, get, path, http, answer = line.strip().split(" ")
        date = date[1:-1]
        date = dt.strptime(date, "%d/%b/%Y:%H:%M:%S")

        if date.strftime("%d.%m.%Y") == search_date.strftime("%d.%m.%Y"):
            if path not in paths:
                paths[path] = 0

            paths[path] += 1

max_path_count = 0
max_path = ""
for path in paths.keys():
    if paths[path] > max_path_count:
        max_path_count = paths[path]
        max_path = path

print(max_path, max_path_count)
