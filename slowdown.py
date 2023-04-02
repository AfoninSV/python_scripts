import time
from typing import Callable, Any
from functools import wraps


def freezer(func: Callable) -> Any:
    """
    Останавливает выполение программы на 3 секунды
    перед выполнением функции
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        time.sleep(3)
        result = func(*args, **kwargs)
        return result
    return wrapped_func
