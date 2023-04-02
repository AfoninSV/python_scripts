from datetime import datetime

def len_string_check(text):
    line_len = len(text.strip())
    if line_len < 3:
        raise ValueError
    return line_len


def syms_counter(file_name):
    total_syms = 0
    l_counter = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data.readlines():
                try:
                    l_counter += 1
                    total_syms += len_string_check(line)
                except ValueError as v_err:
                    print(f'Ошибка: менее трёх символов в строке {l_counter}')
                    with open('errors.log', 'a') as log:
                        log.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} '
                                  f'{type(v_err)}: '
                                  f'Ошибка: менее трёх символов в строке {l_counter}\n')
    except FileNotFoundError:
        print('Ошибка: файл не найден')

    return total_syms



my_file = 'people.txt'
file_syms = syms_counter(my_file)
print(f'Общее количество символов: {file_syms}')