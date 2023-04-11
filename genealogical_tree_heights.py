"""
Program that determines the height of each element in a given genealogical tree.

The program receives N as input, which represents the number of people in the genealogical tree.
Next, N-1 lines are given, each of which specifies a parent for each tree element, except for the ancestor.
Each line has the form "child_name parent_name".

The program should output a list of all tree elements in lexicographic order (alphabetical order).
After outputting the name of each element, its height must be printed.
"""

def insert_name(relative_list):
    parent = relative_list[1]
    descendant = relative_list[0]

    if parent not in pedigree_tree.keys():
        pedigree_tree[parent] = 0

    i_depth = pedigree_tree.get(parent) + 1    # depth index of inserted name
    pedigree_tree[descendant] = i_depth


def dict_view(dict):
    print('\n«Высота» каждого члена семьи:')
    for key in sorted(dict.keys()):
        print(key, dict[key])


pairs_count = int(input('Введите количество человек: '))
pedigree_tree = dict()
for i_pair in range(1, pairs_count):
    pair = input(f'{i_pair} пара: ').split()
    insert_name(pair)

dict_view(pedigree_tree)