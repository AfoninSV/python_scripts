import os


def get_path():
    my_path = input('Введите путь директории: ')
    if os.path.exists(my_path):
        return my_path


def get_root_drive():
    return os.path.abspath(os.sep)


def gen_files_path(path):
    if path is None:
        path = get_root_drive()

    to_find = input('Введите искомую директорию: ')
    for root, dirs, files in os.walk(path):
        if os.path.split(root)[1] == to_find:
            print('\nДиректория найдена:')
            for file in files:
                print(os.path.join(root, file))
            return True
    else:
        print('\nДиректория не найдена.')


my_path = get_path()
var = gen_files_path(path=my_path)
