import random


class Player:
    def __init__(self):
        self.deck = list()

    def take_card(self, *cards):
        for card in cards:
            if (self.total() > 21) and (card.rank == 'Туз'):
                card.price = 1
            self.deck.append(card)

    def info(self):
        for card in self.deck:
            print(card.info())
        print(f'Сумма очков: {self.total()}\n')

    def total(self):
        total_price = 0
        for card in self.deck:
            total_price += card.price
        return total_price

    def action(self):
        try:
            answer = int(input('0 - остановиться, 1 - продолжить: '))
        except ValueError:
            print('Введите число...')
            answer = self.action()
            return answer

        if answer == 1:
            return True
        return False


class Card:
    def __init__(self, suit, rank, price):
        self.suit = suit
        self.rank = rank
        self.price = price

    def info(self) -> str:
        return f'{self.rank} {self.suit} ({self.price})'


class Deck:
    suits = ['Бубны', 'Червы', 'Пики', 'Трефы']
    names = ['Король', 'Дама', 'Валет']
    numbers = [str(num) for num in range(2, 11)]
    # ranks = zip(names, numbers)
    names.extend(numbers)

    name_price = {name: 10 for name in names} | {'Туз': 11}
    num_price = {str(num): num for num in range(2, 11)}
    prices = name_price | num_price

    def __init__(self):
        self.deck = list()
        # self.used = list()

        for suit in Deck.suits:
            for rank in Deck.names:
                self.deck.append(Card(suit, rank, Deck.prices.get(rank)))

    def give_card(self):
        i_card = random.randint(0, len(self.deck) - 1)
        card = self.deck.pop(i_card)
        # self.used.append(card)
        return card

    def give_2_cards(self):
        return self.give_card(), self.give_card()


def win_check(player1: int, player2: int):
    if player1 > 21:
        print('Больше 21, сгорел.')
    elif player1 == player2:
        print('Ничья!')
    elif (player1 == 21) or (player1 > player2):
        print(f'Игрок победил! Очки опонента: {player2}')


def play():
    deck = Deck()
    player = Player()
    ai_player = Player()

    player.take_card(*deck.give_2_cards())
    ai_player.take_card(*deck.give_2_cards())
    player.info()

    while player.action():
        card = deck.give_card()
        player.take_card(card)
        player.info()

    pl_total = player.total()
    ai_total = ai_player.total()
    win_check(pl_total, ai_total)


play()

