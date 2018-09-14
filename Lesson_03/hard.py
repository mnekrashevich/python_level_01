# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def player_to_file(player):
    with open(player['name'] + '.txt', 'w', encoding='utf8') as file:
        for key, value in player.items():
            file.write(f'{key}:{value}\n')


def file_to_player(name):
    with open(name + '.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        lines = list(map(lambda x: x.split(':'), lines))
        player = dict(lines)
        player['health'] = float(player['health'])
        player['damage'] = float(player['damage'])
        player['armor'] = float(player['armor'])

        return player

def attack(assaulter, attacked):
    damage = assaulter['damage']
    damage = damage / attacked['armor']
    attacked['health'] -= damage
    return damage


def auto_fight(assaulter, attacked):
    while True:
        damage = attack(assaulter, attacked)
        if attacked['health'] <= 0:
            return assaulter
        else:
            assaulter, attacked = attacked, assaulter


player = {'name': 'Человек-диван', 'health': 1000, 'damage': 50, 'armor': 1.2}
enemy = {'name': 'Человек-шкаф', 'health': 950, 'damage': 140, 'armor': 1.5}

player_to_file(player)
player_to_file(enemy)

attack(player, enemy)

print(player)
print(enemy)

player = file_to_player('Человек-диван')
enemy = file_to_player('Человек-шкаф')

winner = auto_fight(player, enemy)

print('Победил {}, единиц здоровья {:0.2f}'.format(winner['name'],winner['health']))
