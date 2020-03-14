import unittest

import calc


#

# inherit from TestCase class
class TestMyCalculations(unittest.TestCase):
    # define a test method
    result = 10
    license = True

    def test_add(self):
        self.assertEqual(10, self.result, "should be 10")
        self.assertNotEqual(33, self.result, "should be 10")


# to run the test,
if __name__ == "__main__":
    unittest.main()
