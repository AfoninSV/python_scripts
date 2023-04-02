from functools import wraps
from typing import Callable, Any


def how_are_you(func: Callable) -> Any:
    """Спрашивает у пользователя как дела перед вызовом ф-ции"""

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        input('\nКак дела?: ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func_result = func(*args, **kwargs)
        return func_result
    return wrapped_func


@how_are_you
def test_1() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def test_2(number) -> int:
    result = number * number
    print(f'Square of {number} is {result}')
    return result


@how_are_you
def test_3(name: str = 'Standart name', age: int = 0, job: bool = False) -> str:
    hello_string = f'Name: {name}, age: {age}\n' \
                   f'Job availability: {"Yes" if job else "No"}'
    print(hello_string)
    return hello_string


test_1()
test_2(3)
test_3(name='Joe', age=25, job=True)
