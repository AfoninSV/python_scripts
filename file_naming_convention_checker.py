"""
A program that checks if the given file name satisfies the naming convention of IT-company for text documents:

- File name should not start with any of these special characters: @№$%^&\*().
- File extension should be .txt or .docx.
"""

def name_check(ban_start, rqr_end, filename):

    for i_start in ban_start:
        if filename.startswith(i_start):
            message = 'Ошибка: название начинается на один из специальных символов.'
            return message
    else:
        if not filename.endswith(rqr_end[0]) \
                and not filename.endswith(rqr_end[1]):
            message = 'Ошибка: неверное расширение файла. Ожидалось .txt или .docx.'
            return message
        else:
            message = 'Файл назван верно.'
            return message


'''requirements to naming'''
ban_start = [sym for sym in '@№$%^&\*()']    # banned syms to start name with
rqr_end = ['.txt', '.docx']    # required file extension

file_name = input('Название файла: ').lower()
print(name_check(ban_start, rqr_end, file_name))

