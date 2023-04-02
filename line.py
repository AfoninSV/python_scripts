group_1 = list(range(160, 177, 2))
group_2 = list(range(162, 181, 3))

group_1.extend(group_2)
group_1.sort()

print(f"Отсортированный список учеников: {group_1}")
