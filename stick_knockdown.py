"""
Given the number of sticks N and the number of throws K and a list of pairs representing the range of sticks to be knocked down by each throw, determine which sticks are still standing.

:param N: an integer representing the number of sticks
:param K: an integer representing the number of throws
:param throws: a list of K pairs of integers representing the range of sticks knocked down by each throw
:return: a string of length N where each character is "I" if the corresponding stick is still standing, or "." if it has been knocked down.
"""

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