import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10, 0), 10)
        self.assertEqual(add(2.5, 2.5), 5.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10, 0), 10)
        self.assertEqual(subtract(0, 10), -10)
        self.assertEqual(subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(3.5, 2), 7.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 10), 0)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(-5, 0)

if __name__ == '__main__':
    unittest.main()
