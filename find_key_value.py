"""
Find the value of the specified key in a dictionary, with an optional maximum depth level.
"""

# for example
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def dict_check(data, to_find, depth=None):
    if to_find in data:
        return data[to_find]
    else:
        if isinstance(data, dict):
            for k, v in data.items():
                if depth and depth > 1:
                    if value := dict_check(v, to_find, depth=depth - 1):
                        return value
                elif not depth:
                    if value := dict_check(v, to_find):
                        return value
    return None


def get_info():
    str_key = input('Введите искомый ключ: ')
    if (depth := input('Хотите ввести максимальную глубину? Y/N: ').lower()) == 'n':
        return str_key, None
    elif depth == 'y':
        depth = int(input('Введите максимальную глубину: '))
        return str_key, depth


find_value, depth_check = get_info()
result = dict_check(site, find_value, depth=depth_check)
print(f'Значение ключа: {result}')
