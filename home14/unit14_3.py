import unittest
from doctest14_1 import quadrs


class TestCaseName(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(quadrs(2, 100, 1001), (-99.99999974798794, -100.00000025201206))

    def test_method_2(self):
        self.assertEqual(quadrs(-5, 12, 5), (29.99995800859984, 30.00004199140016))

    def test_method_3(self):
        self.assertEqual(quadrs(3, 100, 20), (-149.9999999842532, -150.0000000157468))


if __name__ == '__main__':
    unittest.main(verbosity=2)