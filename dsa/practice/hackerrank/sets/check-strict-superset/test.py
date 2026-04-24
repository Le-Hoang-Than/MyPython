from solution import check_strict_superset


def test_check_strict_superset_true():
    A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78}
    B = {1, 2, 3, 4, 5}
    assert check_strict_superset(A, B) == True

def test_check_strict_superset_false():
    A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78}
    B = {100, 11, 12}
    assert check_strict_superset(A, B) == False


