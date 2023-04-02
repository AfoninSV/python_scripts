a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
list_count_b = a.count(5) #кол-во цифр "5" в списке
a.extend(c)
list_count_c = a.count(3) #кол-во цифр "3" в списке

for _ in range(list_count_b):
    a.remove(5)

print(f"Кол-во цифр 5 при первом объединении: {list_count_b}")
print(f"ККол-во цифр 3 при втором объединении: {list_count_c}")
print(f"Итоговый список: {a}")