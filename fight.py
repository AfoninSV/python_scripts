"""## Задача 1. Драка
### Что нужно сделать
Вы работаете в команде разработчиков мобильной игры, и вам досталась такая часть от ТЗ заказчика:

Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

Реализуйте такую программу.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- Сообщения о процессе получения результата осмысленны и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.

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