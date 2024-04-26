import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, -1), -2)
        # This test is designed to fail
        self.assertEqual(add(2, 2), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        # This test is designed to fail
        self.assertEqual(subtract(2, -4), -1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)

    def test_divide_fractional_result(self):
        self.assertAlmostEqual(divide(1, 4), 0.25)
        self.assertAlmostEqual(divide(1, 2), 0.5)


if __name__ == '__main__':
    unittest.main()
