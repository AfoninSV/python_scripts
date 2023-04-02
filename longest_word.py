def long_find(word_list):
    longest = ''
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    return longest


string = input('Введите строку: ').split()
longest_word = long_find(string)
print(f'Самое длинное слово: {longest_word}')
print(f'Длина этого слова: {len(longest_word)}')
