import os


"""Collects tasks from homework with info"""

my_files = list()
path = 'home/serhii/python_basic/'
os.chdir('/')
for root, dirs, files in os.walk(path):
    print('---------')
    print(root)
    print(dirs)
    print(files)

    t_path = root.split('/')[-1]
    if 'main.py' in files:
        cell = list()
        with open(os.path.join(root, 'main.py'), 'r') as f:
            data = f.read()
            cell.append(t_path)
            cell.append(data)
        with open(os.path.join(root, 'README.md'), 'r') as f:
            data = f.read()
            cell.append(data)

        my_files.append(tuple(cell))

os.chdir('/home/serhii/envs/git_portfolio/scripts/')
with open('tmp.txt', 'w') as f:
    for element in my_files:
        # f.write(f'{element[0][3:]}\n """{element[2]}"""'
        #         f'\n\n{element[1]}\n\n\n'
        #         f'------------------------------------\n')
        with open(f'{element[0][3:]}.py', 'w') as file:
            file.write(f'"""{element[2]}"""\n'
                       f'{element[1]}')
