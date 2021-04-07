import unittest
from lambdas.ackermann_handler import ackermann


class TestAckermann(unittest.TestCase):
    test_samples = [
        (0, 0, 1),
        (1, 2, 4),
        (2, 1, 5),
        (2, 2, 7),
        (3, 4, 125)
    ]

    def test_n_ackermann(self):
        for m, n, value in self.test_samples:
            self.assertEqual(ackermann(m, n), value)


if __name__ == '__main__':
    unittest.main()
