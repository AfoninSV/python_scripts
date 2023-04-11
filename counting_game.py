"""
Implement a program that plays a counting-out game with N players and counting-out interval K.
The program should output the number of the last remaining player.

"""

def delete_cycle(players, start, cycle):
    counter = 0

    while counter <= cycle:
        for member in players[start : len(players)]:
            counter += 1
            if counter == cycle:
                i_deleted = players.index(member)
            elif counter == cycle + 1:
                return i_deleted, member
        else:
            start = 0


players_count = int(input("Кол-во человек: "))
cycle = int(input("Какое число в считалке?: "))
print(f"Значит, выбывает каждый {cycle}-й человек")

members = list(range(1, players_count + 1))    #members init
start_point = [0, 1]    #index of deleted member, next member

while len(members) > 1:
    print(f"\nТекущий круг людей: {members}")
    print(f"Начало счёта с номера {start_point[1]}")
    start_point[0], start_point[1] = delete_cycle(members, start_point[0], cycle)
    print(f"Выбывает человек под номером {members[start_point[0]]}")

    del members[start_point[0]]
else:
    print(f"\nОстался человек под номером {members[0]}")
