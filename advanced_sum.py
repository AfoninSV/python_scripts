def my_sum(*args):
    total = 0
    for item in args:
        if isinstance(item, list):
            total += my_sum(*item)
        else:
            total += item
    return total


# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(1, 2, 3, 4, 5))