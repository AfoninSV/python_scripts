import random


def nums_ckeck(lst: list):
    returnable = list()
    for num in lst:
        try:
            num = int(num)
            returnable.append(num)
        except ValueError as exc:
            print(f'{type(exc)} Ошибка преобразования числа, проверьте входные данные')
    else:
        return returnable


def divide_xy(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print('X / Y: на ноль делить нельзя')
        return 0


def divide_yz(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        result = y / x
        return result
    except ZeroDivisionError:
        print('Y / X: на ноль делить нельзя')
        return 0


def file_read(file_name):
    with open(file_name, 'r') as pairs:
        data = pairs.readlines()
    return data


def res_write(*args):
    sorted_list = sorted([num for num in args])
    with open('result.txt', 'a') as res_file:
        res_file.write(f'{sorted_list}\n')


file = 'coordinates.txt'
try:
    for line in file_read(file):
        nums_list = nums_ckeck(line.split())
        res1 = divide_xy(nums_list[0], nums_list[1])
        res2 = divide_yz(nums_list[0], nums_list[1])
        r_num = random.randint(0, 100)
        res_write(res1, res2, r_num)

except FileNotFoundError as exc:
    print(f'{type(exc)}: Файл не найден')
except ValueError as exc:
    print(f'{type(exc)} {exc}')
except IndexError as exc:
    print(f'{type(exc)}: Выход за границу списка, проверьте входные данные')
