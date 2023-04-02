"""## Задача 6. Словарь синонимов
### Что нужно сделать
Одна библиотека поручила вам написать программу для оцифровки словарей синонимов. На вход в программу подаётся N пар слов. Каждое слово является синонимом к своему парному слову. 

Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода: если такого слова нет, то выведите ошибку и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов.

Пример:

```
Введите количество пар слов: 3
Первая пара: Привет — Здравствуйте
Вторая пара: Печально — Грустно
Третья пара: Весело — Радостно

Введите слово: интересно
Такого слова в словаре нет.
Введите слово: здравствуйте
Синоним: Привет
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
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