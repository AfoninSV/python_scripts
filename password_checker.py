"""
Module for checking the reliability of a user-entered password.

The program requests a password from the user until a reliable password is entered.
A reliable password must contain at least eight characters, including at least one uppercase letter and at least three digits.
"""

def pass_check(password):
    counter = [sym for sym in password if sym.isdigit()]

    if len(password) < 8:
        return False
    elif password.islower():
        return False
    elif len(counter) < 3:
        return False
    else:
        return True


while True:
    password = input('Придумайте пароль: ')
    if pass_check(password):
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')