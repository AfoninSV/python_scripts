"""## Задача 8. Частотный анализ
### Что нужно сделать
Есть файл `text.txt`, который содержит текст. Напишите программу, которая выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат в файл `analysis.txt`. Символы, не являющиеся буквами английского алфавита, учитывать не нужно. 

В файл `analysis.txt` выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.

Пример:
```
Содержимое файла text.txt:
Mama myla ramu.

Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
"""
def read_data(filename):
    data = dict()
    len_syms = 0
    file = open(filename, 'r')

    for line in file.readlines():
        for sym in line.lower():
            if sym.isalpha():
                len_syms += 1
                if sym in data:
                    data[sym] += 1
                else:
                    data[sym] = 1

    file.close()
    return data, len_syms


def letter_analysis(data: dict, total: int):
    for point in data:
        data[point] = round((data[point] / total), 3)


def sort_condition(element: tuple):
    alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    return element[1], alphabet.index(element[0])


def sort_data(data_dict) -> list:
    data_sorted = sorted(data_dict.items(),
                         reverse=True,
                         key=lambda x: sort_condition(x))
    return data_sorted


def write_result(filename, data: list):
    file = open(filename, 'a')
    for item in data:
        string = f'{item[0]} {item[1]}\n'
        file.write(string)
    file.close()


to_analyze = 'text.txt'
write_to = 'analysis.txt'
# get letters dict, total letters count
lets_data, lets_count = read_data(to_analyze)
# make frequency analysis, rewrite current dict
letter_analysis(lets_data, lets_count)
# make list with sorted data
listed_data = sort_data(lets_data)
# write got data to new file
write_result(write_to, listed_data)
