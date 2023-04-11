"""
Calculate the total value of goods in the store based on the information about goods and their quantities and prices.

The information is stored in two dictionaries: the first one contains the product codes, the second one - 
the lists of various products quantities in stock with their prices.

The program should calculate the total value of each product in stock and display it on the screen.
"""

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
