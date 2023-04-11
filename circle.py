"""
Create a Circle class that is initialized with its center coordinates (X and Y) and radius (R), 
and has methods to calculate and return its area and perimeter, 
increase its radius by a factor of K, and determine if it intersects with another circle.
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

