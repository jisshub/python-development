# from unitest module import testcase class
from unittest import TestCase


# inherit from TestCase class
class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(sum([4, 5, 6], 15), "should be 15")

    def test_sum_tuple(self):
        self.assertEqual(sum((4, 5, 6), 15), "should be 15")


if __name__ == '__main__':
    test = TestSum()
    test.test_sum()
    test.test_sum_tuple()
