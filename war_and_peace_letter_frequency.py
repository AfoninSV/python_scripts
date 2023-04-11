"""
Counts the frequency of letters in the novel "War and Peace" by L.N. Tolstoy
stored in the "voina-i-mir.zip" archive and displays the result sorted by frequency.

The program reads the zip file, extracts the novel, and removes all non-letter characters before counting the frequency.

Returns a dictionary where keys are letters and values are the frequency of their occurrence.
"""

from zipfile import ZipFile
import io


def get_zip_data(name, db):
    with ZipFile(f'{name}.zip') as arch:
        with arch.open(f'{name}.txt') as to_read:
            decoded = io.TextIOWrapper(to_read, encoding='utf-8')
            data = decoded.read()
            for sym in data:
                if sym.isalpha():
                    if sym in db:
                        db[sym] += 1
                    else:
                        db[sym] = 1


def sort_dict(dict_to_sort):
    return sorted(dict_to_sort.items(), key=lambda x: x[1])


def print_stat(data):
    for item in data:
        print(item[0], item[1])


my_file = 'voyna-i-mir'
syms_db = dict()

get_zip_data(my_file, syms_db)
sorted_data = sort_dict(syms_db)
print_stat(sorted_data)
