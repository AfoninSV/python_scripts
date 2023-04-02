"""## Задача 6. Паранойя
### Что нужно сделать
Артуру постоянно кажется, что за ним следят и все хотят своровать «крайне важную информацию» с его компьютера, включая переписку с людьми. Поэтому он эти переписки шифрует. И делает это с помощью шифра Цезаря (чем веселит агента службы безопасности).

Напишите программу, которая шифрует содержимое текстового файла `text.txt` шифром Цезаря, при этом символы первой строки файла должны циклически сдвигаться на один, второй строки — на два, третьей строки — на три и так далее. Результат выведите в файл `cipher_text.txt`.

Пример:

```
Содержимое файла text.txt:
Hello
Hello
Hello
Hello

Содержимое файла cipher_text.txt:
Ifmmp
Jgnnq
Khoor
Lipps

```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
"""
import os

def caesar(crp_line, shift):
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    encrypted_str = ''
    shift = shift + shift

    for sym in crp_line:
        if sym in alphabet:
            i_shifted = alphabet.index(sym) + shift
            if i_shifted > len(alphabet) - 1:
                i_shifted %= len(alphabet)
            encrypted_str += alphabet[i_shifted]
        else:
            encrypted_str += sym

    return encrypted_str


decr_file = open('text.txt', 'r')   # decrypted filename here
encr_file = open('cipher_text.txt', 'a')    # crypted file name
shift = 1

for line in decr_file.readlines():
    new_line = caesar(line, shift)
    encr_file.write(new_line)
    shift += 1

decr_file.close()
encr_file.close()