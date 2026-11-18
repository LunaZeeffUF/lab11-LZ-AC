# https://github.com/LunaZeeffUF/lab11-LZ-AC
# Partner 1: Luna Zeeff
# Partner 2: Adolfo Camacho

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(5, add(2,3))
        self.assertEqual(5, add(0, 5))
        self.assertEqual(5, add(-1, 6))

    def test_subtract(self): # 3 assertions
        self.assertEqual(5, subtract(10, 5))
        self.assertEqual(5, subtract(5, 0))
        self.assertEqual(5, subtract(0, -5))

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(12, mul(3, 4))
        self.assertEqual(-10, mul(-2, 5))
        self.assertEqual(0, mul(0, 7))

    def test_divide(self): # 3 assertions
        self.assertEqual(5, div(2, 10))
        self.assertAlmostEqual(0.5, div(4, 2))
        self.assertEqual(-2, div(-5, 10))

    ######### Partner 2

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(3, logarithm(2, 8))
        self.assertEqual(2, logarithm(2, 4))
        self.assertEqual(0, logarithm(2, 1))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,1)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(5.0, hypotenuse(3,4))
        self.assertAlmostEqual(5.0, hypotenuse(-3, -4))
        self.assertAlmostEqual(13.0, hypotenuse(5, 12))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(4.0, square_root(16))
        self.assertAlmostEqual(1.41421356, square_root(2), places=6)

# Do not touch this
if __name__ == "__main__":
    unittest.main()