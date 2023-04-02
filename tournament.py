"""## Задача 7. Турнир 
### Что нужно сделать
В файле `first_tour.txt` записано число K и данные об участниках турнира по настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в первом туре. Во второй тур проходят участники, которые набрали более K баллов в первом туре. 

Напишите программу, которая выводит в файл `second_tour.txt` данные всех участников, прошедших во второй тур, с нумерацией. 

В первой строке нужно вывести в файл `second_tour.txt` количество участников второго тура. Затем программа должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.

Пример:
```
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Sergeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78

Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
- Входные и выходные файлы названы так, как указано в задании.
"""
def multi_close(*args):
    for file in args:
        file.close()

def write_scores(filename, data):
    filename.write(data)


def next_tour(filename):
    pass_level = int(filename.readline())
    players_data = filename.readlines()
    return_string = str()

    temp_split = [[f'{word[0]}.'
                   if i_word == 1 else word
                   for i_word, word in enumerate(line.split())]
                  for line in players_data
                  if int(line[-3:]) > pass_level]
    temp_split.sort(reverse=True, key=lambda x: x[2])

    return_string += f'{len(temp_split)}\n'
    for item in temp_split:
        item[0], item[1] = item[1], item[0]
        return_string += ' '.join(item) + '\n'

    return return_string


players_file = open('first_tour.txt', 'r')
next_stage_file = open('second_tour.txt', 'w')
new_scores = next_tour(players_file)
write_scores(next_stage_file, new_scores)
multi_close(players_file, next_stage_file)
