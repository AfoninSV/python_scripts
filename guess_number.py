"""## Задача 8. Угадай число
### Что нужно сделать
Артём и Борис играют в игру. Артём загадал натуральное число от 1 до N. Борис пытается угадать это число, для этого он называет несколько чисел подряд. Артём говорит Борису «да», если среди названных Борисом чисел есть задуманное. В противном случае Артём говорит «нет». После нескольких заданных вопросов Борис сдался и попросил вас помочь ему определить, какие числа мог задумать Артём.

Напишите программу, которая имитирует диалог Артёма и Бориса. В начале на вход подаётся число N — это максимальное число, которое мог загадать Артём. Затем Борис предполагает, что среди некоторых чисел есть то, которое загадал Артём (несколько чисел через пробел), а Артём отвечает. Так продолжается до тех пор, пока Борис не попросит помощи (пока не введётся строка «Помогите!»). В конце программы необходимо вывести, какие числа мог загадать Артём.

Пример реализации:

```
Введите максимальное число: 10

Нужное число есть среди вот этих чисел: 1 2 3 4 5
Ответ Артёма: Да

Нужное число есть среди вот этих чисел: 2 4 6 8 10
Ответ Артёма: Нет

Нужное число есть среди вот этих чисел: Помогите!
Артём мог загадать следующие числа: 1 3 5
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
"""
import random


def answ_a(nums_list, desired_num):
    if not nums_list:
        desired_num = int(desired_num)

        if desired_num > 2:
            help_list = list(range(desired_num - 2, desired_num + 3, 2))
        else:
            help_list = list(range(1, 4))
        random.shuffle(help_list)
        message = f'Артём мог загадать следующие числа: {help_list}'

    elif len(nums_list) == 1 and nums_list[0] == desired_num:
        message = 'Победа!'
        return message, False

    elif desired_num in nums_list:
        message = 'Ответ Артёма: Да'

    else:
        message = 'Ответ Артёма: Нет'

    return message, True


def get_nums():
    """get numbers"""
    help_words = {'помогите', 'помогите!', 'памагити'}
    string = input('\nНужное число есть среди вот этих чисел: ').lower()

    if string.lower() not in help_words:
        appr_nums = string.split()
    else:
        appr_nums = False

    return appr_nums


max_num = int(input('Введите максимальное число: '))
desired_num = str(random.randint(1, max_num))
game_flag = True

while game_flag:
    attempt_num = get_nums()
    answer, game_flag = answ_a(attempt_num, desired_num)
    print(f'{answer}')
