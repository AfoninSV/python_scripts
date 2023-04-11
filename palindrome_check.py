"""Check if the given string can be rearranged to form a palindrome."""

def pl_check(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict.keys():
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    pair_counter = len([num for num in sym_dict.values() if num == 2])
    if pair_counter == len(string) // 2 or \
            (pair_counter * 2) == len(string):
        message = 'Можно сделать палиндромом'
    else:
        message = 'Нельзя сделать палиндромом'

    return message


string = input('Введите строку: ')
message = pl_check(string)
print(message)