"""## Задача 5. Гистограмма частоты 2
### Что нужно сделать
Мы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз в строке встречается каждый символ. Теперь задача немного поменялась: максимальную частоту выводить не нужно, однако необходимо написать функцию, которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота, а в качестве значения — список символов с этой частотой. Реализуйте такую программу.

Пример:

```
Введите текст: здесь что-то написано
Оригинальный словарь частот:
  : 2
- : 1
З : 1
а : 2
д : 1
е : 1
и : 1
н : 2
о : 3
п : 1
с : 2
т : 2
ч : 1
ь : 1

Инвертированный словарь частот:
1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
2 : ['с', ' ', 'т', 'н', 'а']
3 : ['о']
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
"""
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