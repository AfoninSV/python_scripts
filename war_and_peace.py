"""## Задача 9. Война и мир
### Что нужно сделать
Мало кто не знает про знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное произведение лежит в архиве `voina-i-mir.zip`. Напишите программу, которая подсчитывает статистику по буквам (не только русского алфавита) в этом романе и выводит результат на экран (или в файл). Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию). Регистр символов имеет значение.

Постарайтесь написать программу так, чтобы для её работы не требовалась распаковка архива «вручную».
### Что оценивается
- Результат вычислений корректен.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входной файл назван так, как указано в задании, выходной файл имеет значащее имя.
"""
from zipfile import ZipFile
import io


def get_zip_data(name, db):
    with ZipFile(f'{name}.zip') as arch:
        with arch.open(f'{name}.txt') as to_read:
            decoded = io.TextIOWrapper(to_read, encoding='utf-8')
            data = decoded.read()
            for sym in data:
                if sym.isalpha():
                    if sym in db:
                        db[sym] += 1
                    else:
                        db[sym] = 1


def sort_dict(dict_to_sort):
    return sorted(dict_to_sort.items(), key=lambda x: x[1])


def print_stat(data):
    for item in data:
        print(item[0], item[1])


my_file = 'voyna-i-mir'
syms_db = dict()

get_zip_data(my_file, syms_db)
sorted_data = sort_dict(syms_db)
print_stat(sorted_data)
