# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


lst_1 = ['василий', 'елена', 'екатерина', 'петр', 'александр']
lst_2 = [10000, 20000, 1000, 1400, 600000]

salary = dict(zip(lst_1, lst_2))
text = list(map(lambda name,value: f'{name} - {value}' if value <= 500000 else '', salary.keys(),salary.values()))
text = list(filter(None, text))
text = '\n'.join(text)
with open('salary.txt', 'w',encoding='utf8') as salary_file:
    salary_file.write(text)

with  open('salary.txt', 'r',encoding='utf8') as salary_file:
    string_list = salary_file.readlines()
string_list = list(map(lambda x: x.strip(), string_list))
salary = dict(map(lambda x: x.split(' - '), string_list))
for name,value in salary.items():
    name = name.title()
    value = float(value) * 0.87
    print(f'{name} - {value}')
