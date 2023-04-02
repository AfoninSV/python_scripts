"""## Задача 3. Круг
### Что нужно сделать
На координатной плоскости рисуются круги, у каждого круга следующие параметры: координаты X и Y центра круга и значение R ― радиус круга. По умолчанию центр находится в (0, 0), а радиус равен 1.

Реализуйте класс «Круг», который инициализируется по этим параметрам. Круг также может:

1. Находить и возвращать свою площадь.
1. Находить и возвращать свой периметр.
1. Увеличиваться в K раз.
1. Определять, пересекается ли он с другой окружностью.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.

"""
import math


class Circle:
    id = 0

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def perimeter(self) -> float:
        return round(2 * self.r * math.pi, 3)

    def area(self) -> float:
        return round(math.pi * self.r ** 2, 3)

    def increase(self, k: float) -> None:
        self.r *= k

    def cross_check(self, circle_2) -> bool:

        distance = abs(math.sqrt(
            (self.x - circle_2.x) ** 2 + (self.y - circle_2.y) ** 2)
        )
        if distance < (self.r + circle_2.r):
            return True
        else:
            return False


main_circle = Circle()
second_circle = Circle(x=2, y=2)
main_circle.increase(2)
if main_circle.cross_check(second_circle):
    print('Обнаружено пересечение кругов.')

