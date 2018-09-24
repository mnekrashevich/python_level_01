# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class TownCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = False

    def go(self):
        print(f'машина {self.name} поехала')
    def stop(self):
        print(f'машина {self.name} остановилась')
    def turn(self, direction):
        dict_direction = {'left':'повернула налево','right':'повернула направо','back':'развернулась'}
        if dict_direction.get(direction):
            print(f'машина {self.name} {dict_direction[direction]}')
        else:
            print(f'машина {self.name} выполнила неизвестный маневр')

class SportCar(TownCar):
    pass

class WorkCar(TownCar):
    pass

class PoliceCar(TownCar):
    def __init__(self,speed, color, name):
        super().__init__(speed, color, name)
        self.is_polis = True


t_car = TownCar(100, 'black', 'Honda Legend')
s_car = SportCar(350,'red', 'Ferrary')
w_car = WorkCar(50, 'yellow','CAT')
p_car = PoliceCar(180, 'с синей полоской', 'УАЗ Буханка')
cars = [t_car, s_car, w_car, p_car]
for car in cars:
    car.turn('back')
    print(car.is_polis)