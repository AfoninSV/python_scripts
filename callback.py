"""
Implement a callback function that executes a user-specified function 
after a specified event, such as a page load or completion of a process.
"""

from functools import wraps
from typing import Callable


app = dict()


def callback(url: str, callbacks: dict = app):
    def action_catcher(func: Callable):
        if app.get(url) is None:
            app[url] = func

        @wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return action_catcher


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
