goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for key in goods.keys():
    t_price = 0
    t_qty = 0
    
    for i_dict in store[goods[key]]:
        t_qty += i_dict.get('quantity')
        t_price += i_dict.get('quantity') * i_dict.get('price')

    print(f'{key} - {t_qty} шт, стоимость {t_price:3,} р.')
