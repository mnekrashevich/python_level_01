# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import sys
import shutil

def current_dir():
    return os.getcwd()

def make_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print(f'Ошибка: Невозможно создать {dir_name}')



def remove_dir(dir_name):
    try:
        os.rmdir(dir_name)
    except OSError:
        print(f'Ошибка: Невозможно удалить {dir_name}')


def dir_list():
    dir_lst = os.listdir()
    dir_lst.insert(0,'..')
    length = len(max(dir_lst,key = len))
    print('ИМЯ'.ljust(length+3),'ТИП'.ljust(6))
    for item in dir_lst:
        item_type = '<DIR>' if os.path.isdir(item) else '<File>'
        print(item.ljust(length+3),item_type.ljust(6))

def backup():
    full_name = os.path.join(os.getcwd(),script_args[0])
    shutil.copyfile(full_name,full_name + '.backup')

def cd(dir_name):
    try:
        os.chdir(dir_name)
    except OSError:
        print(f'Ошибка: Невозможно перейти в {dir_name}')


script_args = sys.argv

if 'task_1_1' in script_args:
    for i in range(1,10):
        make_dir('dir_' + str(i))

if 'task_1_2' in script_args:
    for i in range(1,10):
        remove_dir('dir_' + str(i))

if 'task_2' in script_args:
    dir_list()

if 'task_3' in script_args:
    backup()