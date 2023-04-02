import random

def zero_sort(num_list):
    sorted_list = num_list[:]
    for i_elem in sorted_list:
        ii_elem = sorted_list.index(i_elem)
        if i_elem == 0:
            sorted_list.pop(ii_elem)
            sorted_list.insert(len(sorted_list), 0)
    return sorted_list


numbers_count = int(input('Количество чисел в списке: '))

raw_list = [random.randint(0, 2) for _ in range(numbers_count)]
sorted_list = zero_sort(raw_list)
compressed_list = [sym for sym in raw_list if sym != 0]

print(f'Список до сжатия: {raw_list}')
print(f'Список после сжатия: {compressed_list}')