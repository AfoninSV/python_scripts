length = int(input("Введите длину списка: "))
seq = [1 if i_num % 2 == 0 else i_num % 5 for i_num in range(length)]

print(f"Результат: {seq}")