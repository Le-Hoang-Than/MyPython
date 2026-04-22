from solution import union_set


def test_union_set():
    s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    s2 = {10, 1, 2, 3, 11, 21, 55, 6, 8}
    assert union_set(s1, s2) == 13
