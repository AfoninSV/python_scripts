"""## Задача 4. Число наоборот 3
### Что нужно сделать
Пользователь вводит два вещественных числа — N и K. Напишите программу, которая сначала заменяет целую часть на число. Оно должно отличаться от исходного тем, что цифры записаны в обратном порядке. Затем то же самое программа делает с дробной частью. После этого числа складываются и сумма выводится на экран.

**Пример работы программы:**
```bash
Введите первое число: 102.12
Введите второе число: 123.34

Первое число наоборот: 201.21
Второе число наоборот: 321.43
Сумма: 522.64
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Основной функционал, переворачивание вещественного числа, описан в отдельной функции.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
"""
from decimal import Decimal

def revert(number):
    point_flag = False
    reverted = 0
    base = int(number)
    decimal_str = ''
    decimal_int = 0

    while base != 0:
        reverted = reverted * 10 + base % 10
        base //= 10

    for symbol in str(number):
        if symbol == ".":
            point_flag = True
        elif point_flag:
            decimal_str += symbol
    else:
        decimal_str = int(decimal_str)

    while decimal_str != 0:
        decimal_int = decimal_int * 10 + decimal_str % 10
        decimal_str //= 10

    while decimal_int >= 1:
        decimal_int = Decimal(decimal_int) / Decimal(10)

    reverted += decimal_int
    return reverted

number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))

reverted_1 = revert(number_1)
reverted_2 = revert(number_2)
reverted_sum = reverted_1 + reverted_2

print(f"\nПервое число наоборот: {reverted_1}")
print(f"Второе число наоборот: {reverted_2}")
print(f"Сумма: {reverted_sum}")