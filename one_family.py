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