"""
Counts the number of letters (in Latin alphabet), words, and lines in the file 'zen.txt', and outputs the three numbers.
Additionally, outputs the letter that appears the least frequently in the text.
"""

import os

def counter(file_path):
    """
    Returns a tuple of counter stats:
    (letters, words, lines, min_used_letter)
    """
    zen_file = open(file_path, 'r')
    l_dict = dict()
    lines = 0
    words = 0
    letters = 0

    for line in zen_file.readlines():
        lines += 1
        clear_line = str()

        for sym in line.lower():
            if sym.isalpha():
                clear_line += sym
                letters += 1
                if sym in l_dict:
                    l_dict[sym] += 1
                else:
                    l_dict[sym] = 1
            elif sym == ' ':
                clear_line += sym
        words += len(clear_line.split())

    zen_file.close()
    min_letter = min(l_dict.items(), key=lambda x: x[1])[0]
    return (letters, words, lines, min_letter)


def stats_print(stats: tuple):
    print(f'Количество букв в файле:  {stats[0]}')
    print(f'Количество слов в файле:  {stats[1]}')
    print(f'Количество строк в файле:  {stats[2]}')
    print(f'Наиболее редкая буква: {stats[3]}')

# path to read file
zen_path = os.path.join('..', '02_zen_of_python', 'zen.txt')

zen_stat = counter(zen_path)
stats_print(zen_stat)
