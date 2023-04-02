"""## Задача 4. Тренируемся со срезами
### Что нужно сделать
Дана строка, в которой хранятся первые семь букв английского алфавита. 

`alphabet = 'abcdefg'`

Напишите программу, которая выводит на экран десять вот таких результатов:

1. Копию строки.
1. Элементы строки в обратном порядке.
1. Каждый второй элемент строки (включая самый первый).
1. Каждый второй элемент строки после первого.
1. Все элементы до второго.
1. Все элементы начиная с конца до предпоследнего.
1. Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
1. Последние три элемента строки.
1. Все элементы в диапазоне индексов от 3 до 4.
1. То же, что и в предыдущем пункте, но в обратном порядке.

Для получения и вывода результатов используйте только команду print и срезы.

Результаты работы программы:

```
1: abcdefg
2: gfedcba
3: aceg
4: bdf
5: a
6: g
7: d
8: efg
9: de
10: ed
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Для получения результата используются только print и срезы переменной alphabet.

"""
alphabet = 'abcdefg'

print(f"1: {alphabet[:]}")
print(f"2: {alphabet[::-1]}")
print(f"3: {alphabet[::2]}")
print(f"4: {alphabet[1::2]}")
print(f"5: {alphabet[:1]}")
print(f"6: {alphabet[-1:-2:-1]}")
print(f"7: {alphabet[3:4]}")
print(f"8: {alphabet[-3:]}")
print(f"9: {alphabet[3:5]}")
print(f"10: {alphabet[4:2:-1]}")