"""
Write a function that prints all numbers from 1 to num without using loops.
"""

def sequence(stop, start = 1):
    if start > stop:
        return None
    print(start)
    sequence(stop, start = start + 1)


stop_point = int(input("Введите num: "))
sequence(stop_point)