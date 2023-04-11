"""
Return the number at the specified position in the Fibonacci sequence.

The function takes an integer num_pos as input, representing the position of the number in the sequence.
It recursively calculates the number at the position by adding the two previous numbers in the sequence.
It returns the number at the specified position in the sequence.

:param num_pos: An integer representing the position of the number in the Fibonacci sequence.
:return: The number at the specified position in the Fibonacci sequence.
"""

def fibonacci(number, prev_num=0, start=1, counter=1):
    if number == counter:
        return start
    return fibonacci(number,
              prev_num = start,
              start = prev_num + start,
              counter = counter + 1)


def fibonacci_2(number):
    if number < 2:
        return number
    return fibonacci_2(number - 1) + fibonacci_2(number - 2)

pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {fibonacci(pos)}')
