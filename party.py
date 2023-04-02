guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def guest_move(list):
    print(f"\nСейчас на вечеринке {len(list)} человек: {list}")
    direction = input("Гость пришёл или ушёл? ").lower()

    if direction == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        return False

    guest_name = input("Имя гостя: ").capitalize()

    if direction == "пришёл":
        if len(list) < 6:
            list.append(guest_name)
            print(f"Привет, {guest_name}!")
        else:
            print(f"Прости, {guest_name}, но мест нет.")

    elif direction == "ушёл":
        if guest_name in list:
            list.remove(guest_name)
            print(f"Пока, {guest_name}!")
        else:
            print("Такого гостя не было!")

    else:
        print("Ошибка ввода")

    return True


party = True
while party:
    party = guest_move(guests)