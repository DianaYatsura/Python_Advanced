import unittest
from math import sqrt

class TriangleNotValidArgumentException(Exception):
    pass

class TriangleNotExistException(Exception):
    pass


class Triangle:
    def __init__(self, sides_size):
        if not isinstance(sides_size, (list, tuple)) or len(sides_size) != 3:
            raise TriangleNotValidArgumentException('Not valid arguments')

        for s in sides_size:
            if not isinstance(s, (int, float)):
                raise TriangleNotValidArgumentException('Not valid arguments')

        a, b, c = sides_size
        if a <= 0 or b <= 0 or c <= 0 or not (a + b > c and a + c > b and b + c > a):
            raise TriangleNotExistException ('Can`t create triangle with this arguments')

        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return f'{area:.1f}'


class TriangleTest(unittest.TestCase):
    def test_valid_data(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]

        for sides, expected in valid_test_data:
            with self.subTest(sides=sides):
                triangle = Triangle(list(sides))
                self.assertEqual(float(triangle.get_area()), expected)

    def test_not_valid_triangle(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for sides in not_valid_triangle:
            with self.subTest(sides=sides):
                with self.assertRaises(TriangleNotExistException):
                    Triangle(list(sides))

    def test_not_valid_arguments(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]

        for arg in not_valid_arguments:
            with self.subTest(arg=arg):
                with self.assertRaises(TriangleNotValidArgumentException):
                    if isinstance(arg, (list, tuple)):
                        input_data = list(arg)
                    else:
                        input_data = arg
                    Triangle(input_data)


if __name__ == '__main__':
    unittest.main()