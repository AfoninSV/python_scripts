"""## Задача 5. Сохранение
### Что нужно сделать
Мы продолжаем работать над усовершенствованием своего текстового редактора. Конечно же, при работе с редактором пользователь, скорее всего, захочет сохранить то, что он написал, в отдельный файл. Ну или перезаписать тот, в котором он продолжил работать. 

Пользователь вводит строку text. Реализуйте функцию, которая запрашивает у пользователя, куда он хочет сохранить эту строку: вводится последовательность папок и имя файла (расширение `.txt`). Затем в этот файл сохраняется значение переменной text. Если этот файл уже существует, то нужно спросить у пользователя, действительно ли он хочет перезаписать его.

Обеспечьте контроль ввода: указанный из папок путь должен существовать на диске.

**Пример 1:**
```
Введите строку: programm test

Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

Введите имя файла: my_document
Файл успешно сохранён!
```

*Содержимое файла `my_document.txt`:*
```
programm test
```

**Пример 2:**
```
Введите строку: testiruyem

Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

Введите имя файла: my_document
Вы действительно хотите перезаписать файл? да
Файл успешно перезаписан!
```

*Содержимое файла `my_document.txt`:*
```
testiruyem
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- input содержит корректные приглашения для ввода. 
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
"""
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
