# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

# print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("ping - тестовый ключ")
    print("ls - отображение полного пути текущей директории")
    print("mkdir <dir_name> - создание директории")
    print("cd <dir_name> - изменить текущую директорию")
    print("rm <file_name> - удалить файл")
    print("cp <file_name> - скопировать файл")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
    except FileNotFoundError:
        print('Неверно задан путь до директории {}'.format((dir_name)))

def ping():
    print("pong")

def chk_file():

    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return None

    file_path = os.path.join(os.getcwd(), file_name)

    if not os.path.exists(file_path):
        print(f'{file_name} не существует')
        return None
    if not os.path.isfile(file_path):
        print(f'{file_name} не является файлом')
        return None
    return file_path

def copy_file():
    full_file_name = chk_file()
    if not full_file_name:
        return
    shutil.copyfile(full_file_name,full_file_name + '.copy')
    print(f'файл {file_name} скопирован')

def remove_file():
    full_file_name = chk_file()
    if not full_file_name:
        return
    os.remove(full_file_name)
    print(f'файл {file_name} удален')

def ch_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.chdir(dir_path)
    except FileNotFoundError:
        print(f'Директория {dir_name} не найдена')
    except NotADirectoryError:
        print(f'{dir_name} не является директорией')
    print(os.getcwd())

def current_dir():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": ch_dir,
    "ls": current_dir
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key in ['mkdir','cd']:
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

elif key in ['rm','cp']:
    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")