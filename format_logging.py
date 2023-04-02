"""## Задача 3. Логирование в формате
### Что нужно сделать
Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов) и в который можно передавать формат вывода даты и времени логирования.

Пример кода, передаётся формат `«Месяц День Год - Часы Минуты Секунды»`: 
```python
@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
```
Результат:
```
- Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37 
- Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37 
Тут метод test_sum_1
- Завершение 'A.test_sum_1', время работы = 0.187s 
Тут метод test_sum_1 у наследника
- Завершение 'B.test_sum_1', время работы = 0.187s 
- Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37 
Тут метод test_sum_2 у наследника
- Завершение 'B.test_sum_2', время работы = 0.370s
```
**Совет:** внимательно пересмотрите видео 29.4, если сталкиваетесь с трудностями при решении этой задачи.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры с соответствующими декораторами.
  - Для создания нового класса на основе уже существующего используется наследование.
  - Для статических и классовых методов используется декоратор `classmethod`.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.

"""
from functools import wraps
from typing import Callable
from datetime import datetime
import time


WIP >>> hrin' yakas


def logger_maker(date_format: str)
    def logger(func: Callable):
        @wraps(func)
        def wrapped(*args, **kwargs):
            print(f"Запускается '{func.__name__}'. Дата и время запуска:{datetime.utcnow()}")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time() - start_time
            print(f"Завершение '{func.__name__}', время работы ={end_time}s")
            return result
        return wrapped

def log_methods(date_time: str, decorator=):
    def cls_decorator(cls: Callable):
        @wraps(cls)
        def wrapped(*args, **kwargs):
            methods = [meth for meth in dir(cls) if not meth.startswith('__')]
            for method in methods:
                curr_method = getattr(cls, method)
                setattr(cls, curr_method,
            #instance = cls(*args, **kwargs)
            return cls_decorator(cls(*args, **kwargs))
        return wrapped
    return cls_decorator

# def log_methods(cls):
#     @wraps(cls)
#     def wrapped(*args, **kwargs):
#         methods = [meth for meth in dir(cls) if not meth.startswith('__')]
#         instance = cls(*args, **kwargs)
#         print(methods)
#         return instance
#     return wrapped

#@log_methods
# @log_methods("b d Y - H:M:S")
# class Counter:
#     def __init__(self):
#         self.n = 0
#
#     def nx(self):
#         self.n += 1
#         return self.n
#
# a = Counter()
# print(a.nx())

@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

