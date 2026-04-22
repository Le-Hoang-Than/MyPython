from solution import symmetric_difference


def test_symmetric_difference():
    a = {2, 4, 9, 5}
    b = {2, 4, 11, 12}
    assert symmetric_difference(a, b) == [5, 9, 11, 12]
