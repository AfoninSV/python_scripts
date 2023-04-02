"""## Задача 1. Ревью кода
### Что нужно сделать
Ваня работает middle-разработчиком на Python в IT-компании. Один кандидат на позицию junior-разработчика прислал ему код тестового задания. 

В задании был словарь из трёх студентов. Необходимо:

1. Вывести на экран список пар «ID студента — возраст».
1. Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: полный список интересов всех студентов и общую длину всех фамилий студентов.

Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся на экран.

Ваня — очень придирчивый программист, и после просмотра кода он понял, что этого кандидата на работу не возьмёт, хотя он выдаёт верный результат. Вот код кандидата:

```python
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


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)
```

Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться (только если очень захочется). Убедитесь, что программа верно работает Проверки на существование записей в словаре не обязательны, но приветствуются.

Результат работы программы:

```
Список пар "ID студента — возраст": [(1, 23), (2, 24), (3, 22)]
Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
Общая длина всех фамилий студентов: 20
```

### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом — в видео 2.3).
- Новый код более оптимизирован и чист по стилю программирования (pythonic), чем старый.
"""
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
