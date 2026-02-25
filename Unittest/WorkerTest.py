import unittest


class Worker:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        if self.salary < 0:
            raise ValueError('error')

        limit_tax = [(50000, 0.47),
                    (20000, 0.40),
                    (10000, 0.30),
                    (5000, 0.21),
                    (3000, 0.15),
                    (1000, 0.10),
                    (0, 0.00)
                    ]

        tax = 0.0
        remaining_salary = self.salary
        for limit, rate in limit_tax:
            if remaining_salary > limit:
                tax_amount = remaining_salary - limit
                tax += tax_amount * rate
                remaining_salary = limit

        return round(tax, 2)


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("John", 0)

    def tearDown(self):
        del self.worker

    def test_tax_free(self):
        self.worker.salary = 500
        self.assertEqual(self.worker.get_tax_value(), 0)
        self.worker.salary = 1000
        self.assertEqual(self.worker.get_tax_value(), 0)

    def test_high_tax(self):
        self.worker.salary = 100000
        self.assertEqual(self.worker.get_tax_value(), 40050.0)

    def test_boundary(self):
        self.worker.salary = 1500
        self.assertEqual(self.worker.get_tax_value(), 50.0)

    @unittest.expectedFailure
    def test_should_fail(self):
        self.worker.salary = -100
        self.worker.get_tax_value()


if __name__ == '__main__':
    unittest.main()

