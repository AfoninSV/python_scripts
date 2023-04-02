import os

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
        with open(os.path.join(root, 'main.py'), 'r') as f:
            data = f.read()
            t_wr = (t_path, data)
            my_files.append(t_wr)

#os.chdir(os.path.abspath(__file__))
os.chdir('/home/serhii/envs/git_portfolio/scripts/')
with open('tmp.txt', 'w') as f:
    for element in my_files:
        # f.write(f'{element[0][3:]}\n\n{element[1]}\n\n\n'
        #         f'------------------------------------\n')
        with open(f'{element[0][3:]}.py', 'w') as file:
            file.write(element[1])
