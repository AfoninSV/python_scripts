"""## Задача 3. Дзен Пайтона 2
### Что нужно сделать
Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк в файле zen.txt (который содержит всё тот же «Дзен Пайтона»). Выведите три найденных числа на экран.

Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.

Обратите внимание, что регистр буквы не имеет значение. (А и а - одинаковые буквы).

Формат вывода:
```
Количество букв в файле: 
Количество слов в файле: 
Количество строк в файле: 
Наиболее редкая буква: 
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входной файл назван так, как указано в задании.
"""
import os

def counter(file_path):
    """
    Returns a tuple of counter stats:
    (letters, words, lines, min_used_letter)
    """
    zen_file = open(file_path, 'r')
    l_dict = dict()
    lines = 0
    words = 0
    letters = 0

    for line in zen_file.readlines():
        lines += 1
        clear_line = str()

        for sym in line.lower():
            if sym.isalpha():
                clear_line += sym
                letters += 1
                if sym in l_dict:
                    l_dict[sym] += 1
                else:
                    l_dict[sym] = 1
            elif sym == ' ':
                clear_line += sym
        words += len(clear_line.split())

    zen_file.close()
    min_letter = min(l_dict.items(), key=lambda x: x[1])[0]
    return (letters, words, lines, min_letter)


def stats_print(stats: tuple):
    print(f'Количество букв в файле:  {stats[0]}')
    print(f'Количество слов в файле:  {stats[1]}')
    print(f'Количество строк в файле:  {stats[2]}')
    print(f'Наиболее редкая буква: {stats[3]}')

# path to read file
zen_path = os.path.join('..', '02_zen_of_python', 'zen.txt')

zen_stat = counter(zen_path)
stats_print(zen_stat)
