"""## Задача 2. Свой zip 2
### Что нужно сделать
Написав аналог функции zip на собеседовании, вы вспомнили, 
что этот код можно сделать даже лучше, и резко вырвали листок 
с кодом из рук работодателя, оставив его в недоумении.

Напишите функцию, которая будет являться аналогом функции zip 
и сделайте так, чтобы программа работала с любыми итерируемыми 
типами данных.

- Нельзя пользоваться циклами (за исключением генераторов), 
  условными операторами и функциями определения типа
  (isinstance или type).
- Функция должна возвращать список с кортежами, в котором 
  n-ый кортеж состоит из n-ых элементов всех последовательностей. 
  Например, десятый кортеж будет содержать десятый элемент каждой 
  из переданных последовательностей
- Основной код оставьте пустым или закомментированным
  (используйте его только для тестирования).

Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

**Пример 1**:
````python
a = [{"x": 4}, "b", "z", "d"]

b = (10, {20,}, [30], "z")

print(my_zip(a, b))  # -> [({‘x’: 4}, 10), (‘b’, {20}), (‘z’, [30]), (‘d’, ‘z’)]
````

**Пример 2**:
```python
a = [1, 2, 3, 4, 5]

b = {1: "s", 2: "q", 3: 4}

x = (1, 2, 3, 4, 5)

print(my_zip(a, b, x))  # -> [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
```


### Что оценивается
- Результат вычислений корректен.
- Основной функционал описан в отдельной функции(-ях).
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
"""
def my_zip(*args):
    zip_gen = (
        tuple(list(lst)[i_elem]
        for lst in args)
        for i_elem in range(len(min(args, key=len)))
    )

    return zip_gen


# list_1 = 'HelloWorld!'
# list_2 = list(range(5))
# diction = {1:2,3:4}
# zip_l = my_zip(list_1, list_2,diction)
# print(zip_l)
# print(list(zip_l))
