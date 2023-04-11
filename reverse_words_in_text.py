"""
Reverses all words in a text, while leaving punctuation marks unchanged.
"""

def str_cleaner(text):
    '''purification from commas'''
    clean_str = ''
    for sym in text:
        if sym.isalpha():
            clean_str += sym
        else:
            clean_str += ' '

    return clean_str


def str_reverse(words):
    '''reversing of words from list into string'''
    rw_list = [word[::-1] for word in words]   # reversed words list
    clean_str = ''
    for word in rw_list:
        clean_str += word
    return clean_str


def strings_join(pure_str, raw_str):
    '''joining raw text with reversed words'''
    joined = ''
    counter = 0
    for i_sym in range(len(raw_str)):
        if raw_str[i_sym].isalpha():
            joined += pure_str[counter]
            counter += 1
        else:
            joined += raw_str[i_sym]

    return joined


message = input('Сообщение: ')

listed_mssg = [sym if sym.isalpha() else ' ' for sym in message]
clean_words = str_cleaner(message).split()    # list of words
reversed_string = str_reverse(clean_words)    # string of reversed words
result = strings_join(reversed_string, message)
print(f'Новое сообщение: {result}')