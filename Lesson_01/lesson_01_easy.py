# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

int_var = 132
float_var = 3.14
boolean_var = True
str_var = 'Hello,'

print('int_var = ', int_var, ' boolean_var = ', boolean_var)

name = input('Ваше имя: ')
print(str_var, ' ', name)

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

num = int(input('int'))
num = int(num)
num += 2
print(num)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Ваш возраст:'))
if age < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")



