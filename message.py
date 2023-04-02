"""## Задача 9. Сообщение
### Что нужно сделать
Вашему другу надоело общаться простыми сообщениями, и он решил делать это необычным способом: он переворачивает каждое слово в тексте, при этом не трогая знаки препинания. 

Пользователь вводит текст, состоящий из слов и знаков препинания. Напишите программу, которая переворачивает (записывает в обратном порядке) все слова текста, оставив знаки препинания без изменений. Словом в тексте считается последовательность символов из прописных и строчных букв кириллицы.

Пример 1:

```
Сообщение: Это задание очень! простое.

Новое сообщение: отЭ еинадаз ьнечо! еотсорп.
```

Пример 2:

```
Сообщение: Хотя ,. возм:ожно и нет.

Новое сообщение: ятоХ ,. мзов:онжо и тен.
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

"""
def str_cleaner(text):
    '''purification from commas'''
    clean_str = ''
    for sym in text:
        if sym.isalpha():
            clean_str += sym
        else:
            clean_str += ' '

    return clean_str


def str_reverse(words):
    '''reversing of words from list into string'''
    rw_list = [word[::-1] for word in words]   # reversed words list
    clean_str = ''
    for word in rw_list:
        clean_str += word
    return clean_str


def strings_join(pure_str, raw_str):
    '''joining raw text with reversed words'''
    joined = ''
    counter = 0
    for i_sym in range(len(raw_str)):
        if raw_str[i_sym].isalpha():
            joined += pure_str[counter]
            counter += 1
        else:
            joined += raw_str[i_sym]

    return joined


message = input('Сообщение: ')

listed_mssg = [sym if sym.isalpha() else ' ' for sym in message]
clean_words = str_cleaner(message).split()    # list of words
reversed_string = str_reverse(clean_words)    # string of reversed words
result = strings_join(reversed_string, message)
print(f'Новое сообщение: {result}')