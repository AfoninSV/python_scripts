"""
Create a class hierarchy to represent employees in a company, 
with each subclass having its own method for calculating salary, 
and create a list of nine employees (three each of Managers, Agents, and Workers) 
to display their respective salaries.
"""

class Person:
    """Base class of persons"""

    def __init__(self, first_name: str, last_name: str, age: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def get_info(self):
        info = f'{self.__first_name} ' \
               f'{self.__last_name} ' \
               f'{self.__age}'
        return info


class Employee(Person):
    """
    Child class of Person
    and base for employee positions
    """

    def get_salary(self):
        pass


class Manager(Employee):
    """Employee position class"""

    def get_salary(self):
        return 13_000


class Agent(Employee):
    """Employee position class"""

    _sales_volume = 0

    def set_volume(self, volume: int):
        self._sales_volume = volume

    def get_salary(self):
        return 5_000 + (round(0.05 * self._sales_volume, 2))


class Worker(Employee):
    """Employee position class"""
    
    _working_hours = 0

    def set_working_hours(self, hours: int):
        self._working_hours = hours

    def get_salary(self):
        return round(100 * self._working_hours, 2)



# creating custom examples
managers = [
    Manager(f'Manager_{count}', 'Family#', count + 20)
    for count in range(1, 4)
]

agents = [
    Agent(f'Agent_{count}', 'Family#', count + 20)
    for count in range(1, 4)
]

workers = [
    Worker(f'Worker_{count}', 'Family#', count + 20)
    for count in range(1, 4)
]

# set volume sales
for volume, agent in enumerate(agents):
    agent.set_volume(volume * 100)
# set working hours
for hours, worker in enumerate(workers):
    worker.set_working_hours(hours + 100)

# print each info
for employee in list([*managers, *agents, *workers]):
    print(f'\n{employee.get_info()}\nSalary: {employee.get_salary()}')
