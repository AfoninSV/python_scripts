from random import randint

def throw(raw_list, counter):
    '''imitates throw, delete numbers from list'''
    start_num = raw_list[randint(0, len(raw_list) - 1)]
    fallen = []
    for i_stick in range(randint(1, 4)):
        if start_num + i_stick in raw_list:
            raw_list.pop(raw_list.index(start_num + i_stick))
            fallen.append(start_num + i_stick)
    print(f"Бросок {counter}. Сбиты палки с номера {fallen[0]} по номер {fallen[-1]}.")


def view_make(sticks_list):
    '''takes list of numbers and change it to string list'''
    sticks = ['I' if i_elem in sticks_list else '.' for i_elem in range(1, stick_count + 1)]
    for stick in sticks:
        print(stick, end="")


stick_count = int(input("Количество палок: "))    # sticks total
thr_count = int(input("Количество бросков: "))    # throws total
raw_list = list(range(1, stick_count + 1))        # list of stick indexes

for i_throw in range(1, thr_count + 1):
    throw(raw_list, i_throw)
view_make(raw_list)