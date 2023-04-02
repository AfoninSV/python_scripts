names = input('Доступное меню: ')
available_menu = names.split(';')
formatted_view = ', '.join(available_menu)
print(f'\nНа данный момент в меню есть: {formatted_view}')