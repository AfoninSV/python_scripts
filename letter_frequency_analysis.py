"""
This program performs a frequency analysis of letters in a text file, determines the share of each English alphabet letter
in the total number of English letters in the text and writes the result to a file called "analysis.txt".
"""

def read_data(filename):
    data = dict()
    len_syms = 0
    file = open(filename, 'r')

    for line in file.readlines():
        for sym in line.lower():
            if sym.isalpha():
                len_syms += 1
                if sym in data:
                    data[sym] += 1
                else:
                    data[sym] = 1

    file.close()
    return data, len_syms


def letter_analysis(data: dict, total: int):
    for point in data:
        data[point] = round((data[point] / total), 3)


def sort_condition(element: tuple):
    alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    return element[1], alphabet.index(element[0])


def sort_data(data_dict) -> list:
    data_sorted = sorted(data_dict.items(),
                         reverse=True,
                         key=lambda x: sort_condition(x))
    return data_sorted


def write_result(filename, data: list):
    file = open(filename, 'a')
    for item in data:
        string = f'{item[0]} {item[1]}\n'
        file.write(string)
    file.close()


to_analyze = 'text.txt'
write_to = 'analysis.txt'
# get letters dict, total letters count
lets_data, lets_count = read_data(to_analyze)
# make frequency analysis, rewrite current dict
letter_analysis(lets_data, lets_count)
# make list with sorted data
listed_data = sort_data(lets_data)
# write got data to new file
write_result(write_to, listed_data)
