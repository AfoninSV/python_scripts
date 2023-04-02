"""## Задача 8. Развлечение
### Что нужно сделать
N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i включительно. Определите, какие палки остались стоять на месте.

Напишите программу, которая получает на вход количество палок N и количество бросков K. Далее идёт K пар чисел Left_i, Right_i, при этом 1 ≤ Left_i ≤ Right_i ≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

Пример:

```
Количество палок: 10 
Количество бросков: 3
Бросок 1. Сбиты палки с номера 8 
по номер 10.
Бросок 2. Сбиты палки с номера 2 
по номер 5.
Бросок 3. Сбиты палки с номера 3 
по номер 6.

Результат: I.....I...
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

"""
from random import randint

def throw(raw_list, counter):
    '''imitates throw, delete numbers from list'''
    start_num = raw_list[randint(0, len(raw_list) - 1)]
    fallen = []
    for i_stick in range(randint(1, 4)):
        if start_num + i_stick in raw_list:
            raw_list.pop(raw_list.index(start_num + i_stick))
            fallen.append(start_num + i_stick)
    print(f"Бросок {counter}. Сбиты палки с номера {fallen[0]} по номер {fallen[-1]}.")


def view_make(sticks_list):
    '''takes list of numbers and change it to string list'''
    sticks = ['I' if i_elem in sticks_list else '.' for i_elem in range(1, stick_count + 1)]
    for stick in sticks:
        print(stick, end="")


stick_count = int(input("Количество палок: "))    # sticks total
thr_count = int(input("Количество бросков: "))    # throws total
raw_list = list(range(1, stick_count + 1))        # list of stick indexes

for i_throw in range(1, thr_count + 1):
    throw(raw_list, i_throw)
view_make(raw_list)