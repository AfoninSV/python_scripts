def dict_print(data: dict, nest_count=2):
    tabs = ''.join(['\t' for _ in range(nest_count)])

    for key, value in data.items():
        if isinstance(value, dict):
            print(f"{tabs}'{key}': {{")
            dict_print(value, nest_count=nest_count+1)
        else:
            print(f"{tabs}'{key}': {value}")
    print(f'{tabs}}}')


def add_struct(add_count):
    name = input('Введите название продукта для нового сайта: ')

    if name in sites_collection:
        print('Такой продукт уже существует.')
    else:
        sites_collection[name] = {
            'html': {
                'head': {
                    'title': 'Куплю/продам телефон недорого'
                },
                'body': {
                    'h2': f'У нас самая низкая цена на {name}',
                    'div': 'Купить',
                    'p': 'продать'
                }
            }
        }

    for s_name, s_struct in sites_collection.items():
        print(f'\nСайт для {s_name}:\nsite = {{')
        dict_print(s_struct)
    if add_count > 1:
        add_struct(add_count - 1)


sites_collection = dict()    # {'name': structure, ...}
sites_count = int(input('Сколько сайтов: '))
add_struct(sites_count)