def take_name():
    name = input("Название детали: ")
    return name


def pruduct_count(d_base, name):
    total_count = 0
    total_price = 0
    for i_product in d_base:
        if i_product[0] == name:
            total_count += 1
            total_price += i_product[1]

    return total_count, total_price


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

find_name = take_name()
name_count, name_price_sum = pruduct_count(shop, find_name)

print(f"Кол-во деталей — {name_count}")
print(f"Общая стоимость — {name_price_sum}")