"""## Задача 6. Чат
### Что нужно сделать
Реализуйте программу — чат, в котором могут участвовать сразу несколько человек, то есть программа может работать одновременно для нескольких пользователей. При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:

1. Посмотреть текущий текст чата.
1. Отправить сообщение (затем вводит сообщение).

Действия запрашиваются бесконечно. 

Примечание: для решения задачи вам будет достаточно текущих знаний, нужно лишь проявить немного фантазии и хитрости. Не нужно лезть в дебри работы с сетями, создания GUI-приложений и прочих штук. (Но если очень хочется, то останавливать вас никто не будет!)
### Что оценивается
- Результат вычислений корректен.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
- Сообщения об ошибках осмысленные и понятные для пользователя.
"""
def file_check(filename):
    file = open(filename, 'a')
    file.close()


def get_name():
    user = input('Введите имя(никнейм): ')
    try:
        if (len(user) > 20) or (len(user.split()) > 1):
            raise IndexError
        return user
    except IndexError:
        print('Имя должно состоять из одной части (не более 20 символов)')

def choose_act():
    print('(1 - Почитать | 2 - Написать | 3 - выйти):', end=' ')
    answer = input()
    positive_answer = {1, 2, 3}
    try:
        answer = int(answer)
        if answer not in positive_answer:
            raise ValueError
        return answer
    except ValueError:
        print('Ошибка ввода, ответ должен быть "1", "2" или "3"')


def db_read(to_read, user):
    with open(to_read, 'r') as db_readfile:
        data = db_readfile.readlines()
    if len(data) ==0:
        print('История пустая')
        return None
    for line in data:
        lst_data = line.strip().split(' : ')
        name = lst_data[0]
        message = lst_data[1]

        if name == user:
            print(f'*{name}: {message}')
        else:
            print(f'{name}: {message}')


def db_write(write_to, user):
    message = input('Введите сообщение: ').rstrip()
    with open(write_to, 'a') as db:
        db.write(f'{user} : {message}\n')


def chat(database):
    while True:
        if act_user := get_name():
            break
    while True:
        make_action = choose_act()
        if not make_action:
            continue
        elif make_action == 1:
            db_read(database, act_user)
        elif make_action == 2:
            db_write(database, act_user)
        elif make_action == 3:
            break


db_file = 'db.log'
file_check(db_file)
chat(db_file)