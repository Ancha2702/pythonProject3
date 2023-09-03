import doctest

def quadrs(a, b, c):
    """Решает квадратные уравнения при положительном дискриминанте.
    >>> quadrs(2, 100, 1001)
    (-99.99999974798794, -100.00000025201206)
    >>> quadrs(-5, 12, 5)
    (29.99995800859984, 30.00004199140016)
    >>> quadrs(3, 100, 20)
    (-149.9999999842532, -150.0000000157468)
    """
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

if __name__ == '__main__':
  #  print(quadrs(3,100,20))
    doctest.testmod(verbose=True)
