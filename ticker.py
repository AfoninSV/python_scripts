def get_input_parameters():
    '''lists initialisation'''
    list_1 = input("Первая строка: ")
    list_1 = [sym for sym in list_1]

    list_2 = input("Вторая строка: ")
    list_2 = [sym for sym in list_2]

    return list_1, list_2


def shift_list(list_1):
    for _ in range(1):
        last_num = list_1[-1]
        for index in range(len(list_1) - 1, 0, -1):
            list_1[index] = list_1[index - 1]
        list_1[0] = last_num

    return list_1


def list_compare(list_1, list_2):
    diff_flag = False
    for i_sym in range(len(list_1)):
        if list_1[i_sym] != list_2[i_sym]:
            diff_flag = True
            return diff_flag


list_1, list_2 = get_input_parameters()
counter = 0
for i_shift in range(len(list_1)):
    if list_compare(list_1, list_2):
        list_1 = shift_list(list_1)
        counter += 1
    else:
        print(f'Первая строка получается из второй со сдвигом {counter}.')
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
