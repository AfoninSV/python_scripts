"""## Задача 1. Имена 2
### Что нужно сделать
Есть файл `people.txt`, в котором построчно хранится N имён пользователей. 

Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму. Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой именно строке возникла ошибка. Программа при этом не завершается и обрабатывает все имена файла.

Также при желании можно вывести все ошибки в отдельный файл `errors.log`.

**Пример работы программы**
```
Содержимое файла people.txt:
Василий
Николай
Надежда
Никита
Ян
Ольга
Евгения
Кристина

Ответ в консоли:
Ошибка: менее трёх символов в строке 4.
Общее количество символов: 48.
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
"""
from datetime import datetime

def len_string_check(text):
    line_len = len(text.strip())
    if line_len < 3:
        raise ValueError
    return line_len


def syms_counter(file_name):
    total_syms = 0
    l_counter = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data.readlines():
                try:
                    l_counter += 1
                    total_syms += len_string_check(line)
                except ValueError as v_err:
                    print(f'Ошибка: менее трёх символов в строке {l_counter}')
                    with open('errors.log', 'a') as log:
                        log.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} '
                                  f'{type(v_err)}: '
                                  f'Ошибка: менее трёх символов в строке {l_counter}\n')
    except FileNotFoundError:
        print('Ошибка: файл не найден')

    return total_syms



my_file = 'people.txt'
file_syms = syms_counter(my_file)
print(f'Общее количество символов: {file_syms}')