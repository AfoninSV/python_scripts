"""
This program creates a dictionary of synonyms from N pairs of words and returns the synonym of the input word entered by the user.
"""

def get_syns():
    syns_dict = dict()
    syns_count = int(input('Введите количество пар слов: '))
    for i_pair in range(1, syns_count + 1):
        pair = input(f'{i_pair} пара: ').lower().split(' - ')
        syns_dict[pair[0]] = pair[1]

    return syns_dict


def find_syns(syns_dict, to_find):
    syn_word = syns_dict.get(to_find)

    if not syn_word:
        for key in syns_dict.keys():
            if syns_dict[key] == to_find:
                syn_word = key
                break
        else:
            return 'Такого слова в словаре нет.'

    return f'Синоним: {syn_word.capitalize()}'


syns_dict = get_syns()
word_to_find = input('Введите слово: ').lower()
answer = find_syns(syns_dict, word_to_find)
print(answer)