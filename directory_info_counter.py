"""
Counts the number of files and subdirectories 
in the given directory and displays the size of the directory in kilobytes.
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
