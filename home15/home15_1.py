import argparse
import logging


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

if __name__ == '__main__':
    logging.basicConfig(filename='log_home.log',
                        filemode='a',
                        encoding='utf-8',
                        format='{levelname:<6} - {asctime} в модуле {module} функция "{funcName}()" : {msg}',
                        style='{',
                        level=logging.INFO)

    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser(description="Данные:")
    parser.add_argument('-a', type=str, default='-5')
    parser.add_argument('-b', type=str, default='12')
    parser.add_argument('-c', type=str, default='100')

    args = parser.parse_args()

    try:
        a = int(args.a)
    except ValueError as e:
        logger.error(f'Коэффициент a:"{args.a}", {e}')

    try:
        b = int(args.b)
    except ValueError as e:
        logger.error(f'Коэффициент b:"{args.b}", {e}')

    try:
        c = int(args.c)
    except ValueError as e:
        logger.error(f'Коэффициент с:"{args.c}", {e}')

    try:
        res = quadrs(a, b, c)
        logger.info(f'Решение уравнения: {a}x^2 + ({b})x + ({c}) = 0 , {res}')
        print(res)
    except NameError as e:
        logger.error(f'Коэффициенты a:={args.a}, b={args.b}, c={args.c}", ошибка: {e}')
        print('Переданы некорректные данные, см: Log/quadr.log')

    #>> (решение2)
    #>> (-a=2 -b=100 -c=1001)
    # (-99.99999974798794, -100.00000025201206)
    #>> (-a=-5 -b=12 -c=5)
    # (29.99995800859984, 30.00004199140016)
    #>> (-a=3 -b=100 -c=20)
    # (-149.9999999842532, -150.0000000157468)