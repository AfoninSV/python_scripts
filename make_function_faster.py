def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result


def calculating_math_func_2(data):
    factors_dict = f_collection

    if data > (collection_max := max(factors_dict, default=1)):
        result = factors_dict[collection_max]
        for index in range(collection_max + 1, data + 1):
            result *= index
            factors_dict[index] = result
    else:
        result = factors_dict[data]

    result /= data ** 3
    result = result ** 10
    return result


f_collection = {1:1}   # main dictionary: {num: factorial, ...}

func_result = calculating_math_func_2(5)
func_result_2 = calculating_math_func_2(7)

