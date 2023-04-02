import farm

my_garden = farm.PotatoGarden(5)
my_farmer = farm.Farmer('Grigorii', my_garden)

available_potato = 0
days = 20
for _ in range(days + 1):
    if my_garden.are_all_ripe():
        available_potato += my_farmer.harvest()
    my_farmer.take_care()
print(f'\nЗа {days} дней собрано картошки: {available_potato} кг.')