import math


class Car:
    """Базовый класс автомобиля"""
    def __init__(self, x: int = 0, y: int = 0, angle: int = 0):
        self.x = x
        self.y = y
        self.angle = abs(angle)

    def __str__(self):
        return 'Автомобиль'

    def move(self, distance: int, angle: int = None):
        """Меняет координату автомобиля"""
        self.angle = angle if angle else self.angle
        self.x = distance * round(math.cos(angle), 2)
        self.y = distance * round(math.sin(angle), 2)

    def set_angle(self, angle: int):
        """Меняет угол направления автомобиля"""
        self.angle = abs(angle)

    def get_info(self):
        print(f'\n{self}:\n'
              f'Позиция (x, y): {self.x, self.y}\n'
              f'Направление (угол): {self.angle}')


class Bus(Car):
    """Дочерний класс автомобиля"""

    def __init__(self, x: int = 0, y: int = 0, angle: int = 0):
        super().__init__(x, y, angle)
        self.people_in = 0
        self.money = 0

    def __str__(self):
        return 'Автобус'

    def get_info(self):
        super().get_info()
        print(f'Пассажиров внутри: {self.people_in}\n'
              f'Касса: {self.money}')

    def come_in(self, people_to_in: int):
        """Добавляет пассажиров в автобус"""
        self.people_in += people_to_in

    def go_out(self, people_to_out: int):
        """Убавляет пассажиров из автобуса"""
        if self.people_in < people_to_out:
            raise ArithmeticError('Выйти не могут больше чем есть внути')
        self.people_in -= people_to_out

    def move(self, distance: int, angle: int = None):
        """Передвигает автобус и добавляет денег"""
        super().move(distance, angle)
        self.money += self.people_in * distance * 2    # 2 - условная цена проезда
