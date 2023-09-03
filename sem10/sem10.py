"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
from math import pi


class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_len(self):
        return 2 * pi * self._radius

    def get_area(self):
        return pi * self._radius ** 2


circle = Circle(5)
print(f'Длина окружности = {circle.get_len():.3f}, \nПлощадь окружности = {circle.get_area():.3f}')
"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""

class Rectangle:

    def __init__(self, side_a, side_b=0):
        self._side_a = side_a
        if side_b == 0:
            side_b = side_a
        self._side_b = side_b

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        return self._side_a * self._side_b


rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)

print(f'Периметр прямоугольника = {rectangle1.get_perimeter():.2f}, \n'
      f'Площадь прямоугольника = {rectangle1.get_area():.2f}')
print(f'Периметр прямоугольника = {rectangle2.get_perimeter():.2f}, \n'
      f'Площадь прямоугольника = {rectangle2.get_area():.2f}')
"""
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""
class Human:

    def __init__(self, last_name, first_name, age):
        self._last_name = last_name
        self._first_name = first_name
        self.__age = age

    def get_age(self):
        return self.__age

    def up_birthday(self):
        self.__age += 1

    def get_fullname(self):
        return f'{self._last_name}, {self._first_name}'


if __name__ == "__main__":
    person = Human('Smith', 'Johan', 40)

    print(person._first_name)
    # print(person.__age())
    print(person.get_age())
    person.up_birthday()
    print(person.get_age())
    print(person.get_fullname())

"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
from script10_3 import Human
from random import randint


class Employee(Human):

    # def __init__(self, *args):
    #     # super().__init__(*args)
    #     self._id = randint(100000, 999999)
    #     self._level = sum(int(i) for i in str(self._id)) % 7

    def get_id(self):
        self._id = randint(100000, 999999)
        return self._id

    def get_level(self):
        self._level = sum(int(i) for i in str(self._id)) % 7
        return self._level


employee = Employee('Петров', 'Саня', 45)

print(employee._last_name)
print(employee.get_age())

print(employee.get_fullname())
print(employee.get_id())
print(employee.get_level())

"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""
lass
Fishes:


def __init__(self, kind, name, age, size):
    self._kind = kind
    self._name = name
    self._age = age
    self._size = size


def get_kind(self):
    return self._kind


def get_name(self):
    return self._name


def get_age(self):
    return self._age


def up_age(self):
    self._age += 1


def get_specific(self):
    return self._size


class Birds:

    def __init__(self, kind, name, age, color):
        self._kind = kind
        self._name = name
        self._age = age
        self._color = color

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_specific(self):
        return self._color


class Mammals:

    def __init__(self, kind, name, age, spec):
        self._kind = kind
        self._name = name
        self._age = age
        self._spec = spec

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_specific(self):
        return self._spec


if __name__ == '__main__':
    f1 = Fishes('Карась', 'Федя', 1, 15)

    print(f'Вид: {f1.get_kind()}')
    print(f'кличка: {f1.get_name()}')
    print(f'возраст: {f1.get_age()} лет')
    print(f'размер: {f1.get_specific()} см.')
