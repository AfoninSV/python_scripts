"""## Задача 6. Сжатие списка
### Что нужно сделать
Дан список из N целых случайных чисел (число от 0 до 2). Напишите программу, которая выполняет «сжатие списка» — переставляет все нулевые элементы в конец массива. При этом все ненулевые элементы располагаются в начале массива в том же порядке. Затем все нули из списка удаляются.

Пример:

```
Количество чисел в списке: 10
Список до сжатия: [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
Список после сжатия: [2, 1, 1, 2]
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

"""
import random

def zero_sort(num_list):
    sorted_list = num_list[:]
    for i_elem in sorted_list:
        ii_elem = sorted_list.index(i_elem)
        if i_elem == 0:
            sorted_list.pop(ii_elem)
            sorted_list.insert(len(sorted_list), 0)
    return sorted_list


numbers_count = int(input('Количество чисел в списке: '))

raw_list = [random.randint(0, 2) for _ in range(numbers_count)]
sorted_list = zero_sort(raw_list)
compressed_list = [sym for sym in raw_list if sym != 0]

print(f'Список до сжатия: {raw_list}')
print(f'Список после сжатия: {compressed_list}')