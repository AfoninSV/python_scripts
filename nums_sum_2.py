"""## Задача 1. Сумма чисел 2
### Что нужно сделать
Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк. Напишите программу, которая выводит сумму чисел в выходной файл answer.txt.

Пример:

```
Содержимое файла numbers.txt
     2

2
  2
         2

Содержимое файла answer.txt
8
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
"""
def counter(file_name) -> str:
    file = open(file_name, 'r')
    file_data = file.read()
    print(f'Содержимое файла {file_name}\n{file_data}')
    total = sum([int(elem)
                 for elem in file_data.split()
                 if elem.isdigit()]
                )
    file.close()
    return str(total)


def to_write(data, file_name):
    file = open(file_name, 'w')
    file.write(data)
    file.close()
    print(f'Содержимое файла {file_name}\n{data}')


result = counter('numbers.txt')
to_write(result, 'answer.txt')
