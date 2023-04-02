"""## Задача 5. Ускоряем работу функции
### Что нужно сделать
У нас есть функция, которая делает определённые действия с входными данными:

1) берёт факториал от числа;
1) результат делит на куб входного числа;
1) получившееся число возводит в 10-ю степень.

```python
def calculating_math_func(data):
	result = 1
	for index in range(1, data + 1):
		result *= index
	result /= data ** 3
	result = result ** 10
	return result
```
Однако каждый раз нам приходится делать сложные вычисления, хотя входные и выходные данные одни и те же. И тут наши знания тонкостей Python должны нам помочь.

Оптимизируйте функцию так, чтобы высчитывать факториал для одного и того же числа только один раз.

Подсказка: вспомните, что происходит с изменяемыми данными, если их выставить по умолчанию в параметрах функции.

### Что оценивается
- Результат вычислений корректен.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

"""
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

