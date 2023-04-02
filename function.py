def slicer(origin_tuple, i_number):
    r_list = []
    ss_flag = False
    for sym in origin_tuple:
        if sym == i_number and ss_flag:
            ss_flag = False
            r_list.append(sym)
            break

        elif sym == i_number and not ss_flag:
            ss_flag = True
            r_list.append(sym)

        elif ss_flag == 1:
            r_list.append(sym)

    return tuple(r_list)

some_nums = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
some_nums_2 = (1, 3, 4, 5, 6, 7, 8, 9, 10)
print(slicer(some_nums, 2))
print(slicer(some_nums_2, 2))