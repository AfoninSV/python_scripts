def my_zip(*args):
    zip_gen = (
        tuple(list(lst)[i_elem]
        for lst in args)
        for i_elem in range(len(min(args, key=len)))
    )

    return zip_gen


# list_1 = 'HelloWorld!'
# list_2 = list(range(5))
# diction = {1:2,3:4}
# zip_l = my_zip(list_1, list_2,diction)
# print(zip_l)
# print(list(zip_l))
