"""
Напишите следующие функции:
Нахождение корней квадратного уравнения"""
import csv
import json
from random import randint
from functools import wraps


"""Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк."""
def gen_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(randint(100, 1000)):
            line = []
            for _ in range(3):
                x = 0
                while x == 0:
                    x = randint(-100, 100)
                line.append(x)
            writer.writerow(line)

"""Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла."""
def read_csv(func):
    @wraps(func)
    def wrapper(filename):
        results = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results
    return wrapper
"""Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
def gen_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.json', 'a', encoding='utf-8') as js_f:
            dct = {'func': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result}
            json.dump(dct, js_f, indent=2)
        return result
    return wrapper


"""
Напишите следующие функции:
Нахождение корней квадратного уравнения"""
@read_csv
@gen_json
def quadrs(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + (d ** (-2))) / 2 * a
        x2 = (-b - (d ** (-2))) / 2 * a

        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        real = round(-b / (2 * a), 4)
        im = round(abs(d) ** (-2) / (2 * a), 4)
        x1 = complex(real, im)
        x2 = complex(real, -im)

        return x1, x2


gen_csv('kof.csv')
quadrs('kof.csv')