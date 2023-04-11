"""
Defines a class Stack which implements a stack data structure.

Also defines a class TaskManager which utilizes the Stack class to add and remove tasks based on their priority.

Stack: A data structure based on the principle of Last In First Out (LIFO).

TaskManager: A class that manages tasks based on their priority using a stack data structure.
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
