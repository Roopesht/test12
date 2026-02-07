from businesslogic import calculate_discount
import unittest


class TestDiscountCalculator(unittest.TestCase):
    
    def test_normal_discount(self):
        result = calculate_discount(100, 20)
        self.assertEqual(result, 80.0)
    
    def test_no_discount(self):
        result = calculate_discount(100, 0)
        self.assertEqual(result, 100.0)
    
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

if __name__ == '__main__':
    unittest.main()