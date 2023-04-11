"""
This program allows the user to add contacts to a phone book and search for contacts by last name.
The user can choose to add a contact by providing their first name, last name, and phone number,
or search for a contact by last name and display all contacts with the matching last name and their phone numbers.
The program runs infinitely until terminated by the user.
"""

def get_name():
    names = tuple(input("Введите имя и фамилию нового контакта (через пробел): "
                        ).title().split())
    if names in members_dict.keys():
        return names, True
    else:
        return names, False


def add_member(name):
    ph_number = input("Введите номер телефона: ")
    members_dict[name] = ph_number


def find_member():
    to_find = input("Введите фамилию для поиска: ").capitalize()
    for i_name in members_dict.keys():
        if to_find in i_name:
            print(f"{' '.join([str(i) for i in i_name])} : {members_dict[i_name]}")
            break
    else:
        print("Такого человека нету в книге контактов.")


members_dict = dict()    # phone book initialization

while True:    # main loop
    print("1 - Добавить контакт, 2 - Найти человека")
    action = input("Введите номер действия: ")

    if action == "1":
        names_tpl, id_exist = get_name()
        if id_exist:
            print("Такой человек уже есть в контактах.")
        else:
            add_member(names_tpl)

    elif action == "2":
        find_member()

    else:
        print("Ошибка ввода.")

    print(f"Текущий словарь контактов: {members_dict}\n")