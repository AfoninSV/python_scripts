"""## Задача 3. Файлы
### Что нужно сделать
В одной IT-компании существует негласный закон об именовании текстовых документов:

1. Название файла не должно начинаться на один из специальных символов: `@№$%^&\*()`.
1. Файл заканчивается расширением `.txt` или `.docx`.

Напишите программу, которая получает на вход полное название файла и проверяет его по этим правилам.

Пример 1:

```
Название файла: @example.txt

Ошибка: название начинается на один из специальных символов.
```

Пример 2:

```
Название файла: example.ttx

Ошибка: неверное расширение файла. Ожидалось .txt или .docx.
```

Пример 3:

```
Название файла: example.txt

Файл назван верно.
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

"""
def name_check(ban_start, rqr_end, filename):

    for i_start in ban_start:
        if filename.startswith(i_start):
            message = 'Ошибка: название начинается на один из специальных символов.'
            return message
    else:
        if not filename.endswith(rqr_end[0]) \
                and not filename.endswith(rqr_end[1]):
            message = 'Ошибка: неверное расширение файла. Ожидалось .txt или .docx.'
            return message
        else:
            message = 'Файл назван верно.'
            return message


'''requirements to naming'''
ban_start = [sym for sym in '@№$%^&\*()']    # banned syms to start name with
rqr_end = ['.txt', '.docx']    # required file extension

file_name = input('Название файла: ').lower()
print(name_check(ban_start, rqr_end, file_name))

