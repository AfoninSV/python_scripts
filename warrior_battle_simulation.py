"""
Simulate a battle between two warriors with 100 health points each, where they attack each other in random order,
and the attacked warrior loses 20 health points per attack, until one of them reaches 0 health points.
"""

import random


class Warrior:
    _id_couter = 0
    id = int()
    health = 100
    damage = 20

    def __init__(self, name='Воин'):
        self.name = name
        Warrior._id_couter += 1
        self.id = Warrior._id_couter

    def unit_name(self):
        info_str = f'{self.name} {self.id}'
        return info_str

    def unit_health(self):
        if self.health > 0:
            return self.health
        return 0

    def hit(self, target):
        print(f'{self.unit_name()} атакует.')
        target.health -= self.damage
        print(f'{target.unit_name()} принял удар. '
              f'Осталось {target.unit_health()} очков здоровья')
        print(f'{"":-^45}')


def health_check(unit):
    if unit.health <= 0:
        print(f'{unit.unit_name()} умер')
        return True


def fight():
    unit_1 = Warrior()
    unit_2 = Warrior()
    print(f'Сражаются {unit_1.unit_name()} и {unit_2.unit_name()}\n')

    while True:
        if random.randint(1, 3) == 1:
            unit_1.hit(unit_2)
            if health_check(unit_2):
                print(f'\n* Победил {unit_1.unit_name()}')
                del unit_2
                break
        else:
            unit_2.hit(unit_1)
            if health_check(unit_1):
                print(f'\n* Победил {unit_2.unit_name()}')
                del unit_1
                break


fight()