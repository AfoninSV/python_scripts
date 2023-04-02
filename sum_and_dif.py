def num_count(num):
    counter = 0
    while num != 0:
        num //= 10
        counter += 1
    return counter


def summ(num):
    result = 0
    while num != 0:
        result += num % 10
        num //= 10
    return result


number = int(input("Введите число: "))
difference = summ(number) - num_count(number)

print(f"\nСумма чисел:  {summ(number)}")
print(f"Количество цифр в числе: {num_count(number)}")
print(f"Разность суммы и количества цифр: {difference}")