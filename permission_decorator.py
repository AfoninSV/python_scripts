"""
A decorator that checks if the user has permission to call a certain function and raises a PermissionError if not.
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
