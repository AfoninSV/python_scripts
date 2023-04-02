from typing import Callable, Any
from functools import wraps


def logging(func: Callable) -> Any:
    """
    Ведёт логирование. Записывает название ф-ции
    и записывает ее название и ошибку в файл
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        print(f'Function name: {func.__name__}\nFunction docs: {func.__doc__}\n')
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exc:
            with open('function_errors.log', 'a') as file:
                file.write(f'\nFunction name: {func.__name__}, '
                           f'Error name: {exc.__class__.__name__}')
    return wrapped_func


@logging
def raise_error() -> None:
    """Raises TypeError"""
    raise TypeError


raise_error()
