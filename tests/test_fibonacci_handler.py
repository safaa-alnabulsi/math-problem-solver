import unittest
from lambdas.fibonacci_handler import fibonacci


class TestFibonacci(unittest.TestCase):
    test_samples = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55)
    ]

    def test_n_fibonacci(self):
        for number, value in self.test_samples:
            self.assertEqual(fibonacci(number), value)


if __name__ == '__main__':
    unittest.main()
