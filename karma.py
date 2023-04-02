import random
import exceptions


def write_log(exception, day):
    """Записывает исключение в файл"""
    with open('karma.log', 'a') as file:
        file.write(f'Day {day}: {exception};\n')


def one_day():
    """Возвращает очки кармы или исключение"""
    chance = 1 / 10
    if random.random() < chance:
        raise random.choice(exceptions.exceptions_list)
    return random.randint(1, 7)


def main_loop():
    """Основной цикл получения кармы"""
    karma = 0
    days = 1
    while karma < 500:
        try:
            get_points = one_day()
            karma += get_points
            print(f'День {days}, получено очков кармы: {get_points}, всего {karma};')
        except (exceptions.KillError,
                exceptions.DrunkError,
                exceptions.CarCrashError,
                exceptions.DepressionError,
                exceptions.GluttonyError
                ) as exc:
            write_log(exc.__class__.__name__, days)
            raise exc
        days += 1


main_loop()
