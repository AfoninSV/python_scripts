def make_bank(count):
    bank_list = []
    for i_friend in list(range(1, count + 1)):
        bank_list.append([i_friend, 0])
    return bank_list


def get_debts(friends, debts):
    for i_db in range(1, debts + 1):
        print(f"\n{i_db}-я расписка")
        to = int(input("Кому: "))
        who_from = int(input("От кого: "))
        # input check
        if 0 > to < friends + 1 or 0 > who_from < friends + 1:
            print(f"Ошибка ввода, друзей всего {friends}")
        amount = int(input("Сколько: "))
        statement[to - 1][1] -= amount
        statement[who_from - 1][1] += amount


def balance_print(statement):
    print("\nБаланс друзей:")
    for i_db in statement:
        print(f"{i_db[0]}: {i_db[1]}")


friends_count = int(input("Кол-во друзей: "))
debt_count = int(input("Долговых расписок: "))

statement = make_bank(friends_count)
get_debts(friends_count, debt_count)
balance_print(statement)
