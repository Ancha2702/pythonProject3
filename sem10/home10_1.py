"""
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики
"""

from task10_1 import Mammals, Birds, Fishes


class Fabric:

    def __init__(self, animal_class, **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'kind':
                self.kind = value
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'spec':
                self.spec = value
            if key == 'size':
                self.size = value

    def get_info(self):
        if self.animal_class == 'bird':
            return Birds(self.kind, self.name, self.age, self.color)
        elif self.animal_class == 'mammal':
            return Mammals(self.kind, self.name, self.age, self.spec)
        elif self.animal_class == 'fish':
            return Fishes(self.kind, self.name, self.age, self.size)


if __name__ == '__main__':
    ani1 = Fabric(animal_class='bird', kind='Курица', name='Лариса', age=10, color='Фиолетовый')
    print(ani1.get_info().get_info())

    ani2 = Fabric(animal_class='mammal', kind='Ленивец', name='Вася', age=12, spec='бразильский')
    print(ani2.get_info().get_info())

    ani4 = Fabric(animal_class='fish', kind='Сом', name='Саныч', age=15, size=200)
    print(ani4.get_info().get_info())
