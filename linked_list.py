"""## Задача 6. Односвязный список
### Что нужно сделать
Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.

Связный список — это структура данных, которая состоит из элементов, называющихся узлами. В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.

![](linkedlist.PNG)

В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в сторону конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и дополнительных модулей. Для структуры реализуйте следующие методы:

- append — добавление элемента в конец списка;
- get — получение элемента по индексу;
- remove — удаление элемента по индексу.

Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.

Пример основной программы:

```python
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
```

Результат:
```
Текущий список: [10 20 30]
Получение третьего элемента: 30
Удаление второго элемента.
Новый список: [10 30]
```
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.
"""
from typing import Any, Optional


class Node:

    def __init__(self, value: Any):
        self.__value = value
        self.__next_element = None

    def __repr__(self):
        return str(self.__value)

    def get_next(self):
        return self.__next_element

    def set_next(self, value: Any):
        if value is None:
            # for case when we set None as end of list
            # to avoid Node with None inside
            self.__next_element = value
        else:
            self.__next_element = Node(value)


class LinkedList:

    def __init__(self):
        self.__start: Optional[Node] = None      # first object
        self.__end: Optional[Node] = None        # last object
        self.__pointer: Optional[Node] = None    # to keep in memory obj for itering

    def __repr__(self):
        nodes = (repr(node) for node in self)
        return f"[{', '.join(nodes)}]"

    def __iter__(self):
        self.__pointer = self.__start
        return self

    def __next__(self):
        item = self.__pointer
        if self.__pointer:
            self.__pointer = item.get_next()
        if item:
            return item
        elif item is None:
            raise StopIteration

    def isempty(self) -> bool:
        if self.__start is None:
            return True
        return False

    def init_append(self, value: Node | None):
        """Changes initial links"""

        self.__start = value
        self.__pointer = value
        self.__end = value

    def append(self, value):
        if self.isempty():
            item = Node(value)
            self.init_append(item)
        else:
            self.__end.set_next(value)
            self.__end = self.__end.get_next()

    def get(self, index: int) -> Node | None:
        for i_item, item in enumerate(self):
            if i_item == index:
                return item

    def remove(self, index: int):
        if index == 0 and not self.__start.get_next():
            self.init_append(None)
            return
        elif index == 0:
            item = self.get(0)
            self.__start = item.get_next()
        else:
            prev_node = self.get(index - 1)     # elem before deleted one
            if prev_node is None:
                raise IndexError('Index is out of range')
            curr_node = prev_node.get_next()    # to be deleted
            next_node = curr_node.get_next()    # to set as next on prev

            prev_node.set_next(next_node)
            if next_node is None:
                # if elem is last -> change end link to it
                self.__end = prev_node


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
