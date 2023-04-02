import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(team_1[i_win], team_2[i_win]) for i_win in range(20)]

print(f"Первая команда: {team_1}")
print(f"Вторая команда: {team_2}")
print(f"Победители тура: {winners}")