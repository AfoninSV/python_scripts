"""
Return a list of elements from an iterable object, whose index is a prime number.
"""

import math

def is_prime(sym_list):
    produced_list = []

    for i_sym, sym in enumerate(sym_list):
        if (i_sym == 0) or (i_sym == 1):
            continue
        elif i_sym == 2:
            produced_list.append(sym)

        else:
            counter = 2
            while counter < math.ceil(math.sqrt(i_sym)) + 1:
                if i_sym % counter == 0:
                    break
                counter += 1
            else:
                produced_list.append(sym)
    return produced_list


print(is_prime(list(range(11))))
print(is_prime('О Дивный Новый мир!'))