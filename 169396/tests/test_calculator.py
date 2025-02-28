import unittest
from src.Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_check_sum_int(self):
        self.assertEqual(self.calculator.add(4,5),9)

    def test_check_sum_float(self):
        self.assertAlmostEqual(self.calculator.add(0.1,1e23),1e23)

    def test_check_sum_string(self):
        self.assertEqual(self.calculator.add("aa","bb"),"aabb")

    def test_check_substract_int(self):
        self.assertEqual(self.calculator.substract(9,4),5)

    def test_check_multiply_int(self):
        self.assertEqual(self.calculator.multiply(3,4),12)

    def test_check_divide_int(self):
        self.assertEqual(self.calculator.divide(12,4),3)

    def test_check_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5,0)

    def tearDown(self):
        pass

if __name__ == "__main__": (
    unittest.main())