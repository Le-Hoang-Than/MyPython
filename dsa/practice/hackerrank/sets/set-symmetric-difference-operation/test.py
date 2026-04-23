from solution import symmetric_difference


def test_symmetric_difference():
    s1, s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}, {10, 1, 2, 3, 11, 21, 55, 6, 8}
    assert symmetric_difference(s1,s2) == 8
