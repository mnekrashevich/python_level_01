# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import os

class Person:

    def __init__(self, name, health = 100, damage = 50, armor = 1, load_from_file_if_exist = False):
        if load_from_file_if_exist and os.path.exists(name) and os.path.isfile(name):
            self.get_person_by_filename(name)
        else:
            self.name = name
            self.health = health
            self.damage = damage
            self.armor = armor

    def write_person_to_file(self):
        with open(self.name, 'w', encoding='UTF-8') as f:
            for key, value in self.__dict__.items():
                f.write(f'{key} {value}\n')

    def get_person_by_filename(self,filename):
        with open(filename, encoding='UTF-8') as f:
            for line in f:
                key, value = line.split()
                if key == 'armor':
                    value = float(value)
                elif key != 'name':
                    value = int(value)
                # Сохраняем значение по ключу.
                self.__dict__[key] = value

    def info(self):
        for key, value in self.__dict__.items():
            print(f'{key} - {value}')

    def _calculate_damage(self, armor):
        return self.damage // armor

    def attack(self, who_defend):
        damage = min(self._calculate_damage(who_defend.armor),who_defend.health)
        who_defend.health -= damage
        print(f'{self.name} нанес {who_defend.name} урона {damage}, у того осталось {who_defend.health} жизней.')
        return who_defend.health

class Player(Person):
    pass

class Enemy(Person):
    pass

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        while self.player.attack(self.enemy) and self.enemy.attack(self.player):
            pass
        winner = max(self.player,self.enemy,key = lambda pers: pers.health )
        print(f'Победил {winner.name}')

lena = Player('lena')
vasja = Enemy('vasja')
game = Game(vasja,lena)
game.fight()

