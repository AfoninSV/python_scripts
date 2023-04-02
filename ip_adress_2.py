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