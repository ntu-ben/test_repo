import unittest
from mymath import add, subtract, multiply, divide

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 4)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)

    def test_divide(self):
        self.assertEqual(divide(1, 2), 0.5)

    #hello

if __name__ == '__main__':
    unittest.main()

