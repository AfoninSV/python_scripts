def min_length(list_1, list_2):
    return min(len(list_1), len(list_2))


def my_zip(list_1, list_2):
    return (
            (list_1[i_sym], list_2[i_sym])
            for i_sym in range(min_length(list_1, list_2))
            )


list_1 = 'HelloWorld!'
list_2 = list(range(20))
zip_obj = my_zip(list_1, list_2)

print(zip_obj)
print(list(zip_obj))