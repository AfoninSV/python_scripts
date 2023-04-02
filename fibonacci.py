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
# print(f'{fibonacci_2(pos)}')