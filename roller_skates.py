def get_rollers():
    roller_count = int(input("Кол-во коньков: "))
    rollers = []

    for i_rol in range(1, roller_count + 1):
        rollers.append(int(input(f"Размер {i_rol}-й пары: ")))

    return rollers


def get_foots():
    people_count = int(input("\nКол-во людей: "))
    foots = []

    for i_foot in range(1, people_count + 1):
        foots.append(int(input(f"Размер ноги {i_foot}-го человека: ")))

    return foots


def sort_list(sort_list):
    for index in range(1, len(sort_list)):
        for num in range(index, 0, -1):
            if sort_list[num] < sort_list[num -1]:
                sort_list[num], sort_list[num - 1] = sort_list[num - 1], sort_list[num]
    return sort_list


def matching(shoes_size, foot_size):
    match_count = 0
    for i_ft in foot_size:
        for i_sh in shoes_size:
            if i_sh >= i_ft:
                match_count += 1
                shoes_size.remove(i_sh)
                foot_size.remove(i_ft)
                break
    return match_count


roller_list = sort_list(get_rollers())
foot_list = sort_list(get_foots())
accessible = matching(roller_list, foot_list)

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {accessible}")