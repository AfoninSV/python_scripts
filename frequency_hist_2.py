def get_string():
    str_mssg = input('Введите текст: ')
    return str_mssg


def letter_count(string):
    letters_dict = dict()
    for i_sym in string:
        letter = letters_dict.get(i_sym)
        if letter:
            letters_dict[i_sym] += 1
        else:
            letters_dict[i_sym] = 1

    return letters_dict


def to_letters_list(letters_dict):
    listed_dict = dict()
    for key in letters_dict.keys():
        actual_num = letters_dict[key]
        checker = listed_dict.get(actual_num, False)

        if checker:
            if key not in checker:
                listed_dict[actual_num].append(key)
        else:
            listed_dict[actual_num] = [key]

    return listed_dict


def dict_print(dict):
    for key in dict.keys():
        print(f'{key} : {dict[key]}')



text = get_string()
letters_dict = letter_count(text)
inverted_dict = to_letters_list(letters_dict)

print('Оригинальный словарь частот:')
dict_print(letters_dict)
print('\nИнвертированный словарь частот:')
dict_print(inverted_dict)