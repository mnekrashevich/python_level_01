# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
def info(name, age, city):
    return f'{name.title()}, {age} год(а), проживает в городе {city.title()}'

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
def max_of_3(num_1, num_2, num_3):
    return max(num_1, num_2, num_3)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_of_string(*args):
    return max(args, key=len)

