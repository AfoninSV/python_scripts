def get_input_data():
    c_count = int(input('Количество стран: '))
    country_dict = {}
    for i_country in range(1, c_count + 1):
        print(f'{i_country} страна: ', end='')
        names_str = input().split()
        country_dict[names_str[0]] = names_str[1:]

    return country_dict


def city_get(country_dict, city):
    for i_country in country_dict.keys():
        if city in country_dict[i_country]:
            country = i_country
            break
    else:
        country = None

    if country:
        message = f'Город {city} расположен в стране {country}.'
    else:
        message = f'По городу {city} данных нет.'

    return message


country_dict = get_input_data()
for i_city in range(1, 4):
    city_name = input(f'\n{i_city} город: ')
    print(city_get(country_dict, city_name))
