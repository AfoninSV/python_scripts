"""
Create a function that determines whether a point 
with given coordinates (x, y) lies inside a circle of radius r with center at (0, 0), 
and displays a message based on the result.
"""

def distance_check(x, y, r):
    point_distance = x ** 2 + y ** 2
    if point_distance <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


print("Введите координаты монетки:")
pos_x = float(input("X: "))
pos_y = float(input("Y: "))
radius = float(input("Введите радиус:" ))

distance_check(pos_x, pos_y, radius)



