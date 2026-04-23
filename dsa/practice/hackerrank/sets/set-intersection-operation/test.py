from solution import intersection


def test_intersection():
    s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    s2 = {10, 1, 2, 3, 11, 21, 55, 6, 8}
    assert intersection(s1, s2) == 5
