"""## Задача 7. Функция сортировки
### Что нужно сделать
Напишите функцию, которая сортирует по возрастанию кортеж, состоящий из целых чисел, и возвращает его отсортированным. Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

Пример вызова функции:

```
print(tpl_sort(6, 3, -1, 8, 4, 10, -5))
Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)
```
### Что оценивается
- Результат вычислений корректен.
- Весь функционал программы описан в виде функции
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом — в видео 2.3).
"""
def tpl_sort(nums_tpl):
    '''using sorted func '''
    for num in nums_tpl:    # check for float numbers
        if int(num) != num:
            return nums_tpl
    else: # returning sorted list
        return tuple(sorted(nums_tpl))


def tpl_sort_2(nums_tpl):
    '''hand-written sort function'''
    nums_list = list(nums_tpl)

    for num in nums_list:   # check for float numbers
        if int(num) != num:
            return nums_tpl
    else:   # sorting
        for i_num in range(1, len(nums_list)):
            for num in range(i_num, 0, -1):
                if nums_list[num] < nums_list[num - 1]:
                    nums_list[num], nums_list[num - 1] = \
                        nums_list[num - 1], nums_list[num]

    return tuple(nums_list)


some_nums_1 = (6, 3, -1, 8, 4, 10.5, -5)
some_nums_2 = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(some_nums_1))
print(tpl_sort(some_nums_2))

print(tpl_sort_2(some_nums_1))
print(tpl_sort_2(some_nums_2))