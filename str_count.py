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
