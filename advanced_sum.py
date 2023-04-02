"""## Задача 7. Продвинутая функция sum 
### Что нужно сделать
Как вы знаете, в Python есть полезная функция sum, которая умеет находить сумму элементов списков. Но иногда базовых возможностей функций не хватает для работы и приходится их усовершенствовать.

Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная функция sum. Она должна уметь:

- складывать числа из списка списков;
- складывать числа из набора параметров.

Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

Примеры вызовов функции:
```
sum([[1, 2, [3]], [1], 3])
Ответ в консоли: 10

sum(1, 2, 3, 4, 5)
Ответ в консоли: 15
```

### Что оценивается
- Результат вычислений корректен.
- Весь функционал описан в отдельной функции.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

"""
def my_sum(*args):
    total = 0
    for item in args:
        if isinstance(item, list):
            total += my_sum(*item)
        else:
            total += item
    return total


# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(1, 2, 3, 4, 5))