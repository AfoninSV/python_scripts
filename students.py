import random


class Student:

    def __init__(self, lf_name: str, group_n: int, performance: list):
        self.lf_name = lf_name
        self.group_n = group_n
        self.performance = performance

    def average_performance(self):
        return sum(self.performance) / len(self.performance)

    def sdt_info(self):
        print(f'Имя студента: {self.lf_name} | '
              f'Номер группы: {self.group_n} | '
              f'Средний бал: {self.average_performance()}')


def rand_student():
    name = f'Имя {random.randint(1, 100)}'
    group = random.randint(1, 10)
    perf = [random.randint(1, 5) for _ in range(5)]
    return Student(name, group, perf)


# Initialization 10 random students
students_list = sorted([rand_student() for _ in range(10)],
                       key=lambda x: x.average_performance())
# Student info output
for i_student, student in enumerate(students_list, start=1):
    print(f'{i_student}.', end=' ')
    student.sdt_info()