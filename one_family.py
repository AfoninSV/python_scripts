"""## Задача 5. Одна семья
### Что нужно сделать
В одной базе данных хранится информация о членах нескольких разных семей. Хранение реализовано с помощью словаря с парами «ФИ — возраст».

Инициализируйте словарь членов семей (ФИ и возраст используйте любые) и напишите программу, которая запрашивает у пользователя фамилию и выводит на экран возраст всех членов одной семьи. Учтите, что, например, у двух людей разного пола фамилии отличаются окончанием. Поиск не должен быть регистрозависимым.

Пример:

```
Введите фамилию: Сидоров

Сидоров Никита 35
Сидорова Алина 34
Сидоров Павел 10
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом — в видео 2.3).
"""
fam_dict = {
    ('Сидоров', 'Никита') : 22,
    ('Коваленко', 'Алина') : 34,
    ('Анисимов', 'Владислав') : 28,
    ('Сидорова', 'Наталья') : 41,
    ('Коваленко', 'Наталья') : 26
}

def family_get(fam_dict):
    to_find = input('Введите фамилию: ').capitalize()
    for name, age in fam_dict.items():
        if (to_find in name) or (f'{to_find}а' in name):
            print(name, age)

family_get(fam_dict)