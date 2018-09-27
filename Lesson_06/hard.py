# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Factory:
    class Toy:
        def __init__(self, type_of_toy, color='Неокрашенный'):
            self.color = color
            self.type = type_of_toy
            self.name = f'{self.color} {self.type}'

        def info(self):
            for key, value in self.__dict__.items():
                print(f'{key} : {value}')

        def __eq__(self, other):
            for key, value in self.__dict__.items():
                if other.__dict__[key] != value:
                    return False
            return True

        def __hash__(self):
            return hash(self.name)

        def __repr__(self):
            return f'Toy.{self.name}'

    class Material:
        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            for key, value in self.__dict__.items():
                if other.__dict__[key] != value:
                    return False
            return True

        def __hash__(self):
            return hash(self.name)

        def __repr__(self):
            return f'Material.{self.name}'

    def __init__(self, money):
        self.money = money
        self.materials = {}
        self.toys = {}

    def info(self):
        print(f'Денег - {self.money}')
        print(f'Материала - {self.materials}')
        print(f'Игрушек - {self.toys}')

    def _get_class_by_name(self, parеnt_class, class_name):
        cl_dict = {c.__name__: c for c in parеnt_class.__subclasses__()}
        if class_name in cl_dict:
            return cl_dict[class_name]
        else:
            return type(class_name, (parеnt_class,), {})

    def get_toy(self, type_of_toy, color='Неокрашенный'):
        current_class = self._get_class_by_name(Factory.Toy, 'Factory.Toy.' + type_of_toy.title())
        new_toy = current_class(type_of_toy, color)
        return new_toy

        pass

    def get_material(self, material):
        current_class = self._get_class_by_name(Factory.Material, 'Factory.Material.' + material.title())
        new_material = current_class(material)
        return new_material

    def purchase_of_raw_materials(self, material, quantity, cost):
        new_material = self.get_material(material)
        if self.money >= cost:
            print(f'Закупка материала - {new_material.name} количесвто {quantity} стоимость {cost}')
            self.money -= cost
            if self.materials.get(new_material):
                self.materials[new_material] += quantity
            else:
                self.materials[new_material] = quantity
        else:
            print(f'Не достаточно денег для покупки {new_material.name}')

    def sewing(self, type_of_toy, quantity, material, consumption):
        new_toy = self.get_toy(type_of_toy)
        if self.materials.get(material) and self.materials[material] >= consumption:
            self.materials[material] -= consumption
            print(
                f'Пошив игрушки - {new_toy.type} - количество {quantity}. Расход материала {material.name} : {consumption}')
            if self.toys.get(new_toy):
                self.toys[new_toy] += quantity
            else:
                self.toys[new_toy] = quantity
        else:
            print(f'Не достаточно материала - {material.name}')

    def coloring(self, toy, color, quantity):
        if self.toys.get(toy) and self.toys[toy] >= quantity:
            colored_toy = self.get_toy(toy.type, color)
            self.toys[toy] -= quantity
            if self.toys.get(colored_toy):
                self.toys[colored_toy] += quantity
            else:
                self.toys[colored_toy] = quantity
        else:
            print(f'Не достаточно - {toy.name}')

    def sale_toy(self, toy, quantity, cost):
        if self.toys.get(toy) and self.toys[toy] >= quantity:
            self.toys[toy] -= quantity
            self.money += cost
        else:
            print(f'Не достаточно - {toy.name}')


f = Factory(1000)
f.info()
f.purchase_of_raw_materials('Хлопок', 1000, 1000)
f.info()
f.sewing('чебурашка', 5, f.get_material('Хлопок'), 500)
f.info()
f.coloring(f.get_toy('чебурашка'), 'Синий', 3)
f.info()
f.sale_toy(f.get_toy('чебурашка', 'Синий'), 2, 2000)
f.info()
