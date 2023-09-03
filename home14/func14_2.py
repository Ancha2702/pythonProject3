import pytest
from doctest14_1 import quadrs

def test_1():
    assert quadrs(2, 100, 1001) == (-99.99999974798794, -100.00000025201206),'ошибка вычисления D > 0'

def test_2():
    assert quadrs(-5, 12, 5) == (29.99995800859984, 30.00004199140016), 'ошибка вычисления D = 0'


def test_3():
    assert quadrs(3, 100, 20) == (-149.9999999842532, -150.0000000157468), "ошибка вычисления D < 0"


if __name__ == '__main__':
    pytest.main(['-v'])
