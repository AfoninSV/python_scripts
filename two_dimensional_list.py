"""## Задача 7. Двумерный список
### Что нужно сделать
Как мы говорили ранее, в программировании часто приходится писать код исходя из результата, который требует заказчик. В этот раз заказчику нужно получить вот такой двумерный список:

`[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]`

Напишите программу, которая генерирует такой список и выводит его на экран. Используйте только list comprehensions.
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру: без текста, просто двумерный список с числами.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
"""
dimensional_list = [[num, num + 4, num + 8] for num in range(1, 5)]
print(dimensional_list)