import unittest


def divide(num_1, num_2):
    return float(num_1)/num_2


class DivideTest(unittest.TestCase):
    def test_positive_divide(self):
        self.assertEqual(divide(6,3), 2.0)
        self.assertEqual(divide(-6, 3), -2.0)
        self.assertEqual(divide(-6, -3), 2.0)

    def test_float(self):
        self.assertIsInstance(divide(10,2), float)
        self.assertEqual(divide(5,2), 2.5)

    def test_zero(self):
        self.assertEqual(divide(0,3 ), 0.0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)



if __name__ == '__main__':
    unittest.main()