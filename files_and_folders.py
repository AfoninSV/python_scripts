"""## Задача 4. Файлы и папки
### Что нужно сделать
Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска) и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов. 

Результат работы программы на примере `python_basic\Module14`:
```
E:\PycharmProjects\python_basic\Module14
Размер каталога (в Кб): 8.373046875
Количество подкаталогов: 7
Количество файлов: 15
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- input содержит корректные приглашения для ввода. 
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
"""
import os

def get_path():
    path = input('Укажите путь до каталога:\n')
    while not os.path.exists(path):
        print('Такого каталога не существует, попробуйте снова.')
        path = input('Укажите путь до каталога:\n')
    return path


def dir_count(path):
    """
    Returns counted data:
    (directories, files, total_size)
    """
    dirs = 0
    files = 0
    t_size = 0
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            dirs += 1
        elif os.path.isfile(item_path):
            files += 1
            t_size += os.path.getsize(item_path)

    return (dirs, files, t_size)


def stats_print(stats: tuple):
    print(f'Количество подкаталогов:   {stats[0]}')
    print(f'Количество файлов:  {stats[1]}')
    print(f'Размер каталога (в Кб):  {stats[2]}')


my_path = get_path()
stats = dir_count(my_path)    # (directories, files, total_size)
stats_print(stats)
