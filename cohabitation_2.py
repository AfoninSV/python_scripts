import family

"""
stats (dict): словарь для сохранения статистики
Ниже представлены алгоритмы поведения с сохранением статистики
"""


def one_year(home: family.House, *members):
    """
    Имитация года жизни, вызывает функции поведения представленные выше,
    создает сет для каждого типа жильца и вызывает алгоритм его поведения 365 раз,
    выходит из цикла в случае смерти жильца

    :type home: (family.House)
    :type members: (family.Husband | family.Wife | family.Child | family.Cat)
    :return: None
    """
    mans, women, cats, children = set(), set(), set(), set()

    for member in members:
        if isinstance(member, family.Husband):
            mans.add(member)
        if isinstance(member, family.Wife):
            women.add(member)
        if isinstance(member, family.Cat):
            cats.add(member)
        if isinstance(member, family.Child):
            children.add(member)

    for day in range(1, 366):
        for member in mans:
            member.act(stats)
            if member.home.dirt > 90:
                member.happy -= 10
        for member in women:
            member.act(stats)
            if member.home.dirt > 90:
                member.happy -= 10
        for member in cats:
            member.act()
        for member in children:
            member.act()
        for member in [*mans, *women, *cats, *children]:
            if member.self_check():
                print(f'Дней прожитых без смертей: {day}')
                return
        home.dirt += 5
    print(f'Итоги года:'
          f'\nСьедено еды: {stats.get("total_eaten")}'
          f'\nЗаработано денег: {stats.get("total_earn")}'
          f'\nКуплено шуб: {stats.get("total_coats")}')


stats = {
    'total_earn': 0,
    'total_coats': 0,
    'total_eaten': 0
}

house = family.House()
cat = family.Cat('Star', house)
man = family.Husband('Vasya', house)
women = family.Wife('Katy', house)
child = family.Child('Viktor', house, women, man)

one_year(house, cat, man, women)
