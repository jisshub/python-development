# testing using python
def test_sum():
    assert sum([3, 4, 5]) == 12, "should be 12"


def test_sum_tuple():
    assert sum((3, 4, 5)) == 18


if __name__ == "__main__":
    test_sum()
    print('Everything Passed')
    test_sum_tuple()
    print('Everything Passed')


