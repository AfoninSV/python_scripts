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
