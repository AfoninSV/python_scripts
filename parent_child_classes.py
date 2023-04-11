"""
Create Parent and Child classes with certain attributes and methods.

The Parent class has a name, age, and a list of children, and it can provide information about itself, calm a child, and feed a child.
The Child class has a name, age (which must be at least 16 years younger than the parent's age), and the state of calmness and hunger.
"""

class Child:
    calm = False
    hungry = False

    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name


class Parent:

    def __init__(self, name: str, age: int, children: list[Child, ...] = None):
        self.name = name
        self.age = age
        self.children = list()

        for child in children:
            self.add_child(child)

    def add_child(self, child: Child):
        if (self.age - child.age) >= 16:
            self.children.append(child)
        else:
            raise Exception(f'Ребёнок не младше родителя на 16 лет')

    def get_by_name(self, child_name) -> Child:
        for child in self.children:
            if child_name in child.name:
                kid = child
                return kid
        return None

    def listen_children(self):
        for child in self.children:
            if child.hungry or not child.calm:
                print(f'Ребёнок {child.name} почему-то плачет.')

    def self_info(self):
        print(f'\nЯ родитель и имя моё {self.name}.')
        print(f'Мне {self.age} лет и я имею {len(self.children)} детей.')

    def child_calm(self, childname: str):
        if child := self.get_by_name(childname):
            if child.hungry:
                print('Почему-то ребёнок не успокаиваеться')
            elif not child.calm:
                child.calm = True
                print('Ура, ребёнок перестал плакать.')
            else:
                print('Ребёнок стал счастливее')
        else:
            print(f'Никто из детей не отзываеться на {childname}')

    def child_feed(self, childname: str):
        if child := self.get_by_name(childname):
            if not child.hungry:
                child.hungry = False
                if not child.calm:
                    print('Ребёнок теперь сыт, но почему-то плачет.')
            else:
                print('Ребёнок не хочет кушать.')
                child.calm = False
        else:
            print(f'Никто из детей не отзываеться на {childname}')
