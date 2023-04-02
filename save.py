import os


def check_path():
    str_path = input('Укажите путь до каталога:\n')
    path = os.path.join(*str_path.split())

    while not os.path.exists(path):
        print('Такого каталога не существует, попробуйте снова.')
        str_path = input('Укажите путь до каталога:\n')
        path = os.path.join(*str_path.split())
    print(path)
    return path


def get_file():
    file_name = input('Введите имя файла: ') + '.txt'
    print(file_name)
    return file_name


def get_string():
    str_text = input('Введите строку: ') + '\n'
    return str_text


def get_answer():
    answers = {'да', 'конечно', 'ага', 'yes', 'sure'}
    answer = input('Вы действительно хотите перезаписать файл?: ').lower()
    if answer in answers:
        return True
    else:
        return False


def write_to_file(path, text):
    file = open(path, 'w')
    file.write(text)
    file.close()


my_text = get_string()
path_to_file = check_path()
name_file = get_file()
full_path = os.path.join(path_to_file, name_file)

if os.path.isfile(full_path):
    if get_answer():
        write_to_file(full_path, my_text)
        print('Файл успешно перезаписан!')
    else:
        print('Процедура остановлена.')
else:
    write_to_file(full_path, my_text)
    print('Файл успешно сохранён!')
