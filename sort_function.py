def tpl_sort(nums_tpl):
    '''using sorted func '''
    for num in nums_tpl:    # check for float numbers
        if int(num) != num:
            return nums_tpl
    else: # returning sorted list
        return tuple(sorted(nums_tpl))


def tpl_sort_2(nums_tpl):
    '''hand-written sort function'''
    nums_list = list(nums_tpl)

    for num in nums_list:   # check for float numbers
        if int(num) != num:
            return nums_tpl
    else:   # sorting
        for i_num in range(1, len(nums_list)):
            for num in range(i_num, 0, -1):
                if nums_list[num] < nums_list[num - 1]:
                    nums_list[num], nums_list[num - 1] = \
                        nums_list[num - 1], nums_list[num]

    return tuple(nums_list)


some_nums_1 = (6, 3, -1, 8, 4, 10.5, -5)
some_nums_2 = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(some_nums_1))
print(tpl_sort(some_nums_2))

print(tpl_sort_2(some_nums_1))
print(tpl_sort_2(some_nums_2))