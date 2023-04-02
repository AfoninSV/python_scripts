"""## Задача 7. Стек
### Что нужно сделать
Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры данных на основе уже существующих. Одной из таких «базовых» структур является стек. 

Стек — это абстрактный тип данных, представляющий собой список элементов, организованных по принципу `LIFO` (англ. last in — first out, «последним пришёл — первым вышел»).

Простой пример: стек из книг на столе. Единственной книгой, чья обложка видна, является самая верхняя. Чтобы получить доступ к, например, третьей снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.

Напишите класс, который реализует стек и его возможности (достаточно будет добавления и удаления элемента). 

После этого напишите ещё один класс — «Менеджер задач». В менеджере задач можно выполнить команду «новая задача», в которую передаётся сама задача (`str`) и её приоритет (`int`). Сам менеджер работает на основе стека (не наследование!). При выводе менеджера в консоль все задачи должны быть отсортированы по приоритету: чем меньше число, тем выше задача.

Вот пример основной программы:
```
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

Результат:
1 отдохнуть
2 поесть; сдать дз
4 сделать уборку; помыть посуду
```

Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, а не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.

"""
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]


class Task:
    def __init__(self, task: str, priority: int):
        self.task = task
        self.priority = priority

    def __str__(self):
        return f"{self.priority} {self.task}"


class TaskManager:

    def __init__(self):
        self.tasks = {}

    def new_task(self, task: str, priority: int):
        task = Task(task, priority)
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(task)

    def __str__(self):
        sorted_priorities = sorted(self.tasks.keys())
        res = []
        for priority in sorted_priorities:
            stack = self.tasks[priority]
            task_str = "; ".join([task.task for task in stack.stack])
            res.append(f"{priority} {task_str}")
        return "\n".join(res)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
