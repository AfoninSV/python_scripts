import property


def choose_property():
    """
    Возвращает выбранный тип имущества
    или завершает цикл
    """

    print('\n|1 - Квартира\n'
          '|2 - Автомобиль\n'
          '|3 - Дачный дом\n'
          '|0 - Конец списка')

    property_type = int(input('|Выберите тип имущества: '))
    if property_type == 0:
        return False
    property_price = int(input('|Введите стоимость имущества: '))

    if property_type == 1:
        return property.Apartment(property_price)
    elif property_type == 2:
        return property.Car(property_price)
    elif property_type == 3:
        return property.CountryHouse(property_price)


def get_total_tax(property_list):
    """Возвращает сумму налогов имущества"""

    total_tax = int()
    for prop in property_list:
        total_tax += prop.get_tax()
    return total_tax


def calculation():
    """
    Собирает список имущества и считает разницу
    между наличными деньгами и налогами к уплате
    """

    total_money = int(input('Введите сумму денег в наличии: '))
    property_list = list()
    while True:
        property_type = choose_property()
        if not property_type:
            break
        property_list.append(property_type)
    total_taxes = get_total_tax(property_list)
    difference = total_money - total_taxes
    print(f'Общая сумма налогов: {total_taxes}')

    if difference > 0:
        print('Всё хорошо, денег хватает')
    else:
        print(f'Ой, для уплаты налогов не хватает: {difference}.')


try:
    calculation()
except ValueError:
    print('\nОшибка! Вводить нужно только цифры.')
