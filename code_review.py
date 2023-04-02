students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def get_data(st_dict):
    in_list = []
    len_count = 0

    for id in st_dict:
        in_list.append(st_dict[id]['interests'])
        len_count += len(st_dict[id]['surname'])

    return in_list, len_count


print('ID студента и возраст:')
for student in students:
    print(f"{student}: {students[student]['age']}")

'''interests, name length'''
interests_list, name_total = get_data(students)
print(f'\nСписок всех интересов: \n{interests_list}')
print(f'\nОбщая длина всех фамилий студентов: {name_total}')
