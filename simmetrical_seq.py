"""## Задача 10. Симметричная последовательность
### Что нужно сделать
Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево. Например, следующие последовательности являются симметричными:

```
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
```

Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет, какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной.

Пример 1:

```
Кол-во чисел: 5
Число: 1
Число: 2
Число: 1
Число: 2
Число: 2

Последовательность: [1, 2, 1, 2, 2]
Нужно приписать чисел: 3
Сами числа: [1, 2, 1]
```

Пример 2:

```
Кол-во чисел: 5
Число: 1
Число: 2
Число: 3
Число: 4
Число: 5

Последовательность: [1, 2, 3, 4, 5]
Нужно приписать чисел: 4
Сами числа: [4, 3, 2, 1]
```
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

#"""
def make_list(count):
    seq = []
    for _ in range(count):
        seq.append(int(input("Число: ")))
    return seq


def symmetry_check(seq):
    absence = []
    flag = False
    # cut last same numbers
    counter = 0
    while True:
        if seq[-1] == seq[counter - 1]:
            counter -= 1
        else:
            break

    # check for symmetry through both list sides
    for right_num in range(len(seq) - 1, -1 + abs(counter), -1):
        left_num = len(seq) - 1 - right_num
        if flag:
            absence.insert(0, seq[left_num])
        elif seq[left_num] != seq[right_num]:
            flag = True
            absence.insert(0, seq[left_num])

    return absence


seq_count = int(input("Кол-во чисел: "))
sequence = make_list(seq_count)
absenced_nums = symmetry_check(sequence)

print(f"\nПоследовательность: {sequence}")
print(f"Нужно приписать чисел: {len(absenced_nums)}")
print(f"Сами числа: {absenced_nums}")
