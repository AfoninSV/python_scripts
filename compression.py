def compress(string):
    pointer = 0
    index = 0
    compressed = ''

    for sym in string + ' ':
        if sym != string[pointer]:
            compressed += '{0}{1}'.format(
                string[pointer],
                index - pointer)
            pointer = index
        index += 1

    return compressed


full_str = input('Введите строку: ')
compressed_str = compress(full_str)
print(f'Закодированная строка: {compressed_str}')
