def get_integer():
    rec_count = input('Сколько записей вносится в протокол?: ')
    while True:
        if rec_count.isdigit():
            rec_count = int(rec_count)
            break
        else:
            rec_count = input('Ошибка ввода, повторите попытку: ')

    return rec_count


def get_data():
    r_data = input().split()
    while len(r_data) < 2:
        r_data = input('Ошибка ввода, попробуйте ещё раз:\n').split()
    r_data[0] = int(r_data[0])
    return tuple(r_data)


def write_data(dbase, data_to):
    is_exist = dbase.get(data_to[1], False)
    if is_exist:
        dbase[data_to[1]].append(data_to[0])
    else:
        dbase[data_to[1]] = [data_to[0]]
    return None


score_table = dict()
records_count = get_integer()

for i_record in range(1, records_count + 1):
    print(f'{i_record}-я запись:', end=' ')
    record = get_data()    # tuple
    write_data(score_table, record)

print('\nИтоги соревнований:')
sorted_table = sorted(score_table.items(),
                      key=lambda score: sorted(score[1],reverse=True),
                      reverse=True)
for i_winner, record in enumerate(sorted_table[:3], start=1):
    print(f'{i_winner}-е место: {record[0]} - {max(record[1])}')
