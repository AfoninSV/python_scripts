"""
Encode a string using a simple compression algorithm 
where groups of identical characters are replaced by the character and the count of its repetitions.

Example: 'aaaabbcaa' is encoded as 'a4b2c1a2'.

:param string: the input string to be encoded
:return: the encoded string using the given compression algorithm
"""
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
