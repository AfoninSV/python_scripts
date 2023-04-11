"""
A program that determines whether a given string is a valid IP address.
The input string should consist of four integers in the range from 0 to 255, separated by dots.
"""

def ip_check(ip):
    ip_parts = ip.split('.')

    if ip.count('.') != 3:
        message = 'Адрес — это четыре числа, разделённые точками.'
        return message

    for i_elem in ip_parts:
        if not i_elem.isdigit():
            message = f'{i_elem} - это не целое число.'
            break
        elif not -1 < int(i_elem) < 256:
            message = f'{i_elem} не в диапазоне от 0 до 255.'
            break
    else:
        message = 'IP-адрес корректен.'

    return message


ip_string = input('Введите IP: ')
print(ip_check(ip_string))