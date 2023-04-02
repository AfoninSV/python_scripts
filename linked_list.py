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
