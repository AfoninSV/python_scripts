"""## Задача 2. Координаты
### Что нужно сделать
Есть файл `coordinates.txt`, в котором хранится `N` пар из чисел X и Y. Оба числа передаются в первую функцию, где к каждой координате прибавляется случайное число (от 0 до 5 и от 0 до 10) и возвращается результат деления X на Y. Затем эти же координаты передаются во вторую функцию, где уже отнимается случайное число и возвращается Y / X.

После этого формируется случайное число от 0 до 100, затем в файл `result.tx`t в каждую строку записывается отсортированный список, состоящий из этого случайного числа и двух полученных результатов.

Один программист уже написал за нас программу для этой задачи, но «почему-то» его вариант решения отклонили. Вот его код:

```python
import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    file = open('coordinates.txt', 'r')
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            try:
                number = random.randint(0, 100)
                file_2 = open('result.txt', 'w')
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(my_list))
            except Exception:
                print("Что-то пошло не так : ")
        except Exception:
            print("Что-то пошло не так со второй функцией")
        finally:
            file.close()
            file_2.close()
except Exception:
    print("Что-то пошло не так с первой функцией")
```

Отредактируйте и исправьте программу, убрав лишние вложенности `try..except`.
### Что оценивается
- Результат вычислений корректен.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.

"""
import random


def nums_ckeck(lst: list):
    returnable = list()
    for num in lst:
        try:
            num = int(num)
            returnable.append(num)
        except ValueError as exc:
            print(f'{type(exc)} Ошибка преобразования числа, проверьте входные данные')
    else:
        return returnable


def divide_xy(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print('X / Y: на ноль делить нельзя')
        return 0


def divide_yz(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        result = y / x
        return result
    except ZeroDivisionError:
        print('Y / X: на ноль делить нельзя')
        return 0


def file_read(file_name):
    with open(file_name, 'r') as pairs:
        data = pairs.readlines()
    return data


def res_write(*args):
    sorted_list = sorted([num for num in args])
    with open('result.txt', 'a') as res_file:
        res_file.write(f'{sorted_list}\n')


file = 'coordinates.txt'
try:
    for line in file_read(file):
        nums_list = nums_ckeck(line.split())
        res1 = divide_xy(nums_list[0], nums_list[1])
        res2 = divide_yz(nums_list[0], nums_list[1])
        r_num = random.randint(0, 100)
        res_write(res1, res2, r_num)

except FileNotFoundError as exc:
    print(f'{type(exc)}: Файл не найден')
except ValueError as exc:
    print(f'{type(exc)} {exc}')
except IndexError as exc:
    print(f'{type(exc)}: Выход за границу списка, проверьте входные данные')
