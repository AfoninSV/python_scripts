import random


def defeat_check(chance=1/13):
    if random.random() <= chance:
        raise OverflowError('Вас постигла неудача!')


def write_number(number, write_to='out_file.txt'):
    with open(write_to, 'a') as log:
        log.write(f'{number}\n')


def read_log(to_read='out_file.txt'):
    with open(to_read, 'r') as file:
        data = file.read()
    print(f'\nСодержимое файла {to_read}:')
    print(data)


def game():
    total = 0
    while total < 777:
        try:
            number = int(input('Введите число: '))
            total += number
            defeat_check()
            write_number(number)

        except OverflowError as exc:
            print(f'{exc}')
            break
        except ValueError:
            print('Не похоже на число, попробуй ещё.')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')


game()
read_log()
