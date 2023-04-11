"""
Take input N orders and output a sorted list of customers along with their orders.
Each order is a string containing "Customer - Pizza Name - Quantity" in the given format.
"""

def make_orders(ord_count, orders):
    for i_ord in range(1, ord_count + 1):
        order = input(f'{i_ord}-ый заказ: ').split()
        name, pizza, num = order[0], order[1], int(order[2])

        check = orders.setdefault(
            name, {pizza : []}
        ).setdefault(pizza, [])
        orders[name][pizza].append(num)
    print()


def dict_print(to_view):
    for name in sorted(to_view.keys()):
        print(f'{name} :')
        for i_dict in sorted(to_view[name]):
            print(f'\t{i_dict} : {sum(to_view[name][i_dict])}')



orders_history = dict()    # orders dictionary init
orders_count = int(input('Введите количество заказов: '))
make_orders(orders_count, orders_history)   # get and add order to dict
dict_print(orders_history)  # print of orders dictionary

