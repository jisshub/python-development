import unittest
import arraymin


class TestTheArray(unittest.TestCase):
    def test_my_array(self):
        getVals = [5, 1, 6, 8, ]
        arraymin.get_items_list(getVals)
        self.assertNotEqual(0, len(getVals))


if __name__ == '__main__':
    unittest.main()
