"""## Задача 1. Права доступа
### Что нужно сделать
На вас возложили задачу по созданию и поддержке специализированного сайта-форума. Вы только начали выполнять задачу и сейчас остановились на реализации действий, которые могут совершать посетители форума. И конечно же, для разных пользователей прописаны разные возможности.

Напишите декоратор `check_permission`, который проверяет, есть ли у пользователя доступ к вызываемой функции, и если нет, то выдаёт исключение `PermissionError`.

Пример кода:
```python
user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
```
Результат:
```
Удаляем сайт
PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.

"""
from functools import wraps
from typing import Callable


def check_permission(user: str):

    def permission_decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if user in user_permissions:
                return func(*args, **kwargs)
            raise PermissionError(
                f'У пользователя недостаточно прав, чтобы выполнить функцию '
                f'{func.__name__}')

        return wrapped_func

    return permission_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
