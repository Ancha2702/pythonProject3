class ErrorConvert(Exception):
    def __str__(self):
        return f'Ошибка преобразования данных в тип INT'

class Limit(Exception):
    DOWN = 1
    UP = 1000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Функция может принимать значения от {self.DOWN} до {self.UP}\n Вы ввели {self.a, self.b, self.c}'
def quadrs(a, b, c):
    try:
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            raise ErrorConvert
        if Limit.DOWN <= a <= Limit.UP and Limit.DOWN <= b <= Limit.UP and Limit.DOWN <= c <= Limit.UP:
            pass
        else:
            raise Limit(a, b, c)
    except ErrorConvert as er:
        print(er)
        exit()
    except Limit as l:
        print(l)
        exit()
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


quadrs(2,10,1001)
