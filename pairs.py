'''Method 1'''
nums_list_1 = [
    (num_tpl, num_tpl + 1)
    for num_tpl in range(0, 10, 2)
]
print(nums_list_1)

'''Method 2'''
nums_1 = list(range(0, 10, 2))
nums_2 = list(range(1, 10, 2))

nums_list_2 = zip(nums_1, nums_2)
print(list(nums_list_2))