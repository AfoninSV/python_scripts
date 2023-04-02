"""## Задача 4. Регистрация
### Что нужно сделать
У вас есть файл с протоколом регистраций пользователей на сайте — `registrations.txt`. Каждая строка содержит имя, емейл и возраст, разделённые пробелами. Например: `Василий test@test.ru 27`.

Напишите программу, которая проверяет данные из файла для каждой строки:

- Присутствуют все три поля.
- Поле «Имя» содержит только буквы.
- Поле «Имейл» содержит @ и . (точку).
- Поле «Возраст» является числом от 10 до 99.

В результате проверки сформируйте два файла:

- `registrations_good.log` — для правильных данных, записывать строки в том виде, как есть;
- `registrations_bad.log` — для ошибочных, записывать строку и вид ошибки.

Для валидации строки данных напишите функцию, которая может выдавать исключения:

- НЕ присутствуют все три поля: `IndexError`.
- Поле «Имя» содержит НЕ только буквы: `NameError`.
- Поле «Имейл» НЕ содержит @ и . (точку): `SyntaxError`.
- Поле «Возраст» НЕ является числом от 10 до 99: `ValueError`.

**Формат выходных данных**
```
Содержимое файла registrations_bad.log:
Ольга kmrn@gmail.com 123		Поле «Возраст» НЕ является числом от 10 до 99
Чехова kb@gmail.com 142		Поле «Возраст» НЕ является числом от 10 до 99
……
Степан ky 59		Поле «Имейл» НЕ содержит @ и . (точку)
……

Содержимое файла registrations_good.log:
Геннадий ttdababmt@gmail.com 69
Ольга ysbxur@gmail.com 20
……
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
"""
def stat_open(stats: str) -> list:
    try:
        with open(stats, 'r') as file:
            data = file.readlines()
            return data
    except FileNotFoundError:
        print(f'Ошибка: файл {stats} не найден')


def str_write(data, file_name, add_info=''):
    with open(file_name, 'a') as file:
        file.write(f'{data}{add_info}\n')

def name_check(str_name):
    for sym in str_name:
        if not sym.isalpha():
            raise NameError


def email_check(str_email):
    a_index = str_email.rfind('@')
    p_index = str_email.rfind('.')
    if (a_index == -1) or (p_index == -1) or (a_index > p_index):
        raise SyntaxError


def age_check(str_age):
    age = int(str_age)
    if not (10 < age < 99):
        raise ValueError

def string_check(str_line, good_file, ng_file):
    str_line = str_line.strip()
    lst_line = str_line.split()

    try:
        name = lst_line[0]
        email = lst_line[1]
        age = lst_line[2]
        name_check(name)
        email_check(email)
        age_check(age)

    except ValueError:
        err = 'Поле «Возраст» НЕ является числом от 10 до 99'
        str_write(str_line, ng_file, add_info=f'\t{err}')
    except SyntaxError:
        err = 'Поле «Имейл» НЕ содержит @ и . (точку)'
        str_write(str_line, ng_file, add_info=f'\t{err}')
    except NameError:
        err = 'Поле «Имя» содержит НЕ только буквы'
        str_write(str_line, ng_file, add_info=f'\t{err}')
    except IndexError:
        err = 'НЕ присутствуют все три поля'
        str_write(str_line, ng_file, add_info=f'\t{err}')
    else:
        str_write(str_line, good_file)

def out_read(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f'Ошибка: файл {file_name} не найден')
    print(f'Содержимое файла {file_name}: \n')
    print(data)

good_file = 'registrations_good.log'
ng_file = 'registrations_bad.log'
stats_file = 'registrations.txt'

for line in stat_open(stats_file):
    string_check(line, good_file, ng_file)

out_read(ng_file)
out_read(good_file)
