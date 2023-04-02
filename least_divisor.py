def lowest_divider(num):
    for symbol in range(num + 1, 1, -1):
        if num % symbol == 0:
            divider = symbol
    return divider


number = int(input("Введите число: "))
lcd = lowest_divider(number)
print(f"Наименьший делитель, отличный от единицы: {lcd}")