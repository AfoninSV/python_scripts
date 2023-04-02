def counter(file_name) -> str:
    file = open(file_name, 'r')
    file_data = file.read()
    print(f'Содержимое файла {file_name}\n{file_data}')
    total = sum([int(elem)
                 for elem in file_data.split()
                 if elem.isdigit()]
                )
    file.close()
    return str(total)


def to_write(data, file_name):
    file = open(file_name, 'w')
    file.write(data)
    file.close()
    print(f'Содержимое файла {file_name}\n{data}')


result = counter('numbers.txt')
to_write(result, 'answer.txt')
