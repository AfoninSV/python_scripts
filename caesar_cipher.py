alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

string = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
print('Зашифрованное сообщение:', end=' ')

for i_sym in string:
    if i_sym in alphabet:
        i_shifted = alphabet.index(i_sym) + 3
        if i_shifted > len(alphabet) - 1:
            i_shifted %= len(alphabet)
        print(alphabet[i_shifted], end='')
    else:
        print(i_sym, end='')
