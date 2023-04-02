"""## Задача 1. Квадраты чисел
### Что нужно сделать
Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N (`1 ** 2`, `2 ** 2`, `3 ** 2` и так далее). Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

"""
from math import pow


class PowIter:
    """
    Iter class
    Returns power of 2 from every number till limit

    :rtype: int
    """

    def __init__(self, peak: int):
        self.peak = peak
        self.counter = 1

    def __iter__(self):
        self.counter = 1
        return self

    def __next__(self):
        if self.counter >= self.peak:
            raise StopIteration
        pow_num = pow(self.counter, 2)
        self.counter += 1
        return pow_num


def pow_generator(peak: int):
    for num in range(1, peak):
        yield pow(num, 2)


def pow_expression(peak: int):
    return (pow(num, 2) for num in range(1, peak))


def print_examples(cls, func, exp):
    """Outputs objects themselves and as list"""
    print(cls, list(cls))
    print(func, list(func))
    print(exp, list(exp))


peak_number = int(input('Введите число: '))

class_iter = PowIter(peak_number)
func_generator = pow_generator(peak_number)
gen_expression = pow_expression(peak_number)
print_examples(class_iter,
               func_generator,
               gen_expression)
