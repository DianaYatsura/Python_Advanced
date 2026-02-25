import unittest
import math


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError('error')
    discriminant  = b**2 - 4*a*c
    if discriminant  < 0:
        return None
    elif discriminant  == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b - math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
        if x1 > x2:
            return x1, x2
        else:
            return x2, x1


class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_less_zero(self):
        self.assertEqual(quadratic_equation(1, 1, 1), None)

    def test_discriminant_equal_zero(self):
        self.assertEqual(quadratic_equation(1, 2, 1), -1.0)

    def test_discriminant_greater_zero(self):
        self.assertEqual(quadratic_equation(1, 4, -21),(3.0, -7.0))
        self.assertEqual(quadratic_equation(3, -12, 9), (3.0, 1.0))

    def test_zero(self):
        self.assertRaises(ValueError, quadratic_equation, 0, 0, 0)



