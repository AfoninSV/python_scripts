def data_check(lst_data):
    oper_syms = {'+', '-', '*', '/', '**', '%'}
    if (len(lst_data) != 3) or \
            (lst_data[1] not in oper_syms) or \
            (not lst_data[0].isdigit()) or \
            (not lst_data[2].isdigit()):
        raise ValueError


def get_answer(ng_str):
    print(f'Обнаружена ошибка в строке: {ng_str}, исправить?: ', end='')
    qst = input().lower()
    pos_answ = {'+', 'yes', 'да', 'конечно'}
    if qst in pos_answ:
        answ = input('Введите исправленную строку: ')
        return answ


def my_calc():
    s_file = 'calc.txt'
    total_sum = 0
    with open(s_file, 'r') as doc:
        lst_data = doc.readlines()

    for line in lst_data:
        line = line.strip()
        try:
            cls_data = line.split()
            data_check(cls_data)
            total_sum += eval(line)
        except ValueError:
            answer = get_answer(line)
            if answer:
                lst_data.append(answer)
    return total_sum


t_num = my_calc()
print(f'\nСумма результатов: {t_num}')