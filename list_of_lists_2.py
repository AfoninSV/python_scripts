nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

extended_list = [
    number for nested_1 in nice_list
    for nested_2 in nested_1
    for number in nested_2]
print(f"Ответ: {extended_list}")
