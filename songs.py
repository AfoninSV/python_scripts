violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

def find_song(list, name):
    for i_song in range(len(list)):
        if list[i_song][0] == name:
            return list[i_song][1]
    else:
        print("Такой песни в списке нету.")
        return 0


find_count = int(input("Сколько песен выбрать? "))
total_time = 0

for i_song in range(1, find_count + 1):
    name = input(f"Название {i_song}-й песни: ")
    total_time += find_song(violator_songs, name)

print(f"Общее время звучания песен: {round(total_time, 2)}")