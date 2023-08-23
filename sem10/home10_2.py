"""
Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2. (завернуть в класс)
"""

class Quadr:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.с = c
        self.d = b ** b - (4 * a * c)

    def solve(self):
        if self.d > 0:
            x1 = (-self.b + (self.d ** (-2))) / (2 * self.a)
            x2 = (-self.b - (self.d ** (-2))) / (2 * self.a)
            return (print(f'Корни квадратного уравнения {x1} и {x2}'))
        else:
            return (f'Уравнение не имеет решения')


a = float(input('Введите коэффициент уравнения a: '))
b = float(input('Введите коэффициент уравнения b: '))
c = float(input('Введите коэффициент уравнения c: '))

quadr = Quadr(a, b, c)
print(quadr.solve())
