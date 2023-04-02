"""## Задача 5. Счётчик
### Что нужно сделать
Реализуйте декоратор `counter`, считающий и выводящий количество вызовов декорируемой функции.

Для решения задачи нельзя использовать операторы `global` и `nonlocal` (об этом мы ещё расскажем).
### Что оценивается
- Результат вычислений корректен.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.
- Во всех декораторах используется `functools.wraps`.

"""
from typing import Callable, Any
from functools import wraps


def counter(func: Callable) -> Any:
    """
    Счётчик - считает количество вызовов
    той или иной декорируемой функции
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.called_times += 1
        print(f'Функция {func.__name__} была вызвана {wrapped_func.called_times} раз.')
        return func(*args, **kwargs)

    wrapped_func.called_times = 0
    return wrapped_func


@counter
def test() -> None:
    print('<Тут что-то происходит...>')


test()
test()
