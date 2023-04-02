violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


def get_input_parameters():
    '''returns list of requested songs'''
    song_count = input('Сколько песен выбрать? ')
    while not song_count.isdigit():
        print('Ошибка ввода, ожидается целое число.')
        song_count = input('Сколько песен выбрать? ')
    song_count = int(song_count)

    song_names = []
    for i_song in range(1, song_count + 1):
        song_name = input(f'Название {i_song} песни: ')
        song_names.append(song_name)

    return song_names


def time_get(get_list, avl_list):
    '''returns total time'''
    total_duration = 0

    for name in get_list:
        if name in avl_list.keys():
            total_duration += avl_list[name]
        else:
            print(f'Песни {name} нету в списке доступных.')

    return round(total_duration, 2)


req_songs = get_input_parameters()    # list of requested songs
total_rq_time = time_get(req_songs, violator_songs)    # total duration time of requested songs
print(f'\nОбщее время звучания песен: {total_rq_time} минуты')