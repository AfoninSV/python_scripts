import random


def answ_a(nums_list, desired_num):
    if not nums_list:
        desired_num = int(desired_num)

        if desired_num > 2:
            help_list = list(range(desired_num - 2, desired_num + 3, 2))
        else:
            help_list = list(range(1, 4))
        random.shuffle(help_list)
        message = f'Артём мог загадать следующие числа: {help_list}'

    elif len(nums_list) == 1 and nums_list[0] == desired_num:
        message = 'Победа!'
        return message, False

    elif desired_num in nums_list:
        message = 'Ответ Артёма: Да'

    else:
        message = 'Ответ Артёма: Нет'

    return message, True


def get_nums():
    """get numbers"""
    help_words = {'помогите', 'помогите!', 'памагити'}
    string = input('\nНужное число есть среди вот этих чисел: ').lower()

    if string.lower() not in help_words:
        appr_nums = string.split()
    else:
        appr_nums = False

    return appr_nums


max_num = int(input('Введите максимальное число: '))
desired_num = str(random.randint(1, max_num))
game_flag = True

while game_flag:
    attempt_num = get_nums()
    answer, game_flag = answ_a(attempt_num, desired_num)
    print(f'{answer}')
