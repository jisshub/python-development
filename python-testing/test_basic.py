# Simple Testing Program
import unittest


# inherit from TestCase class
class TestMyCases(unittest.TestCase):
    # define a test method
    result = 10
    license = True

    def test_case_1(self):
        # assertEqual(a,b) where a == b
        self.assertEqual(10, self.result, "should be 10")

    def test_case_2(self):
        # assertNotEqual(a,b) where a!=b
        self.assertNotEqual(33, self.result, "should be 10")

    def test_case_3(self):
        # assertTrue(x) # x is True
        self.assertTrue(self.license, "should be true")

    def test_case_4(self):
        married = False
        # asertFalse(x)  #x should be False
        self.assertFalse(married)

    def test_case_5(self):
        a = 10
        b = 10
        # assertIs(a,b) where a is b
        self.assertIs(a, b)

    def test_case_6(self):
        names = ["thor", "speiderman", "hulk", "wolverine"]
        # assertIn(a, iterable) #a in iterable
        self.assertIn("hulk", names)

    def test_case_7(self):
        names = ["thor", "speiderman", "hulk", "wolverine"]
        # assertNotIn(a, iterable) where a not in the iterable
        self.assertNotIn("superman", names)


# to run the test,
if __name__ == "__main__":
    # invoke main() of unittest
    unittest.main()
