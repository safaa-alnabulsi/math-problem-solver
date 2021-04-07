import unittest
from lambdas.factorial_handler import factorial


class TestFactorial(unittest.TestCase):
    test_samples = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (24, 620448401733239439360000),
        (34, 295232799039604140847618609643520000000)
    ]

    def test_n_factorial(self):
        for number, value in self.test_samples:
            self.assertEqual(factorial(number), value)


if __name__ == '__main__':
    unittest.main()
