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

