def make_list():
    numbers_1 = []
    numbers_2 = []
    for i_elem in range(1, 4):
        numbers_1.append(input(f"Введите {i_elem}-е число для первого списка: "))

    for i_elem in range(1,8):
        numbers_2.append(input(f"Введите {i_elem}-е число для второго списка: "))

    return numbers_1, numbers_2


def uniq_check(numbers):
    for i_num in numbers:
        counter = numbers.count(i_num)
        for _ in range(counter - 1):
            numbers.remove(i_num)
    return numbers


num_list_1, num_list_2 = make_list()
print(f"\nПервый список {num_list_1}")
print(f"Второй список {num_list_2}")

num_list_1.extend(num_list_2)
num_list_1 = uniq_check(num_list_1)
print(f"\nНовый первый список с уникальными элементами: {num_list_1}")