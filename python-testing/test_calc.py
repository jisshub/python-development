import unittest

# import module calc.py
import calc


class TestCalc(unittest.TestCase):
    # define a test method
    def test_additon(self):
        self.assertEqual(calc.addition(10, 5), 15)
        self.assertNotEqual(calc.addition(13, 6), 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(30, 10), 20)
        self.assertNotEqual(calc.subtract(30, 15), 20)

    def test_multiply(self):
        self.assertEqual(calc.multiply(20, 2), 40)

    def test_division(self):
        self.assertEqual(calc.division(50, 5), 10)


# Run the test
if __name__ == '__main__':
    unittest.main()
