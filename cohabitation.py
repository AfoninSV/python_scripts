"""## Задача 7. Совместное проживание
### Что нужно сделать
Чтобы понять, стоит ли ему жить с кем-то или всё же лучше остаться в гордом одиночестве, Артём решил провести довольно необычное исследование. Для этого он реализовал модель человека и модель дома.

Человек может:

1. Есть (+ сытость, − еда).
1. Работать (− сытость, + деньги).
1. Играть (− сытость).
1. Ходить в магазин за едой (+ еда, − деньги).

У человека есть имя, степень сытости (изначально 50) и дом.

В доме есть холодильник с едой (изначально 50 еды) и тумбочка с деньгами (изначально 0 денег).

Если сытость человека становится меньше нуля, то человек умирает.

Логика действий человека определяется следующим образом:

1. Генерируется число кубика от 1 до 6.
1. Если сытость < 20, то поесть.
1. Иначе, если еды в доме < 10, то сходить в магазин.
1. Иначе, если денег в доме < 50, то работать.
1. Иначе, если кубик равен 1, то работать.
1. Иначе, если кубик равен 2, то поесть.
1. Иначе играть.

По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз. 
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- Сообщения о процессе получения результата осмысленны и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.

"""
from random import randint


class House:
    def __init__(self):
        self.fridge = 50
        self.money_shelf = 0


class Man:
    def __init__(self, name: str, home: House):
        self.name = name
        self.starving = 50
        self.home = home

    def eat(self):
        if self.home.fridge > 0:
            self.starving += 1

    def work(self):
        self.starving -= 1
        self.home.money_shelf += 1

    def play(self):
        self.starving += 1

    def shopping(self):
        if self.home.money_shelf > 0:
            self.home.fridge += 1
            self.home.money_shelf -= 1

    def action(self):
        if self.starving == 0:
            print(f'{self.name} умер с голоду.')
            return False
        cube = randint(1, 6)
        if self.starving < 20:
            self.eat()
        elif self.home.fridge < 10:
            self.shopping()
        elif self.home.money_shelf < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()
        return True


def living(man_1, man_2):
    lived_days = 0
    while lived_days < 365:
        if not all([man_1.action(), man_2.action()]):
            break
        lived_days += 1
    print(f'Успех, прожито вместе дней: {lived_days}')


house = House()
man = Man('Вася', house)
women = Man('Ира', house)

for _ in range(5):
    living(man, women)
