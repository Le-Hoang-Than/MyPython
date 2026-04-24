from solution import happy_score


def test_happy_score():
    array = [1, 5, 3]
    A = {1, 3}
    B = {5, 7}
    assert happy_score(A,B,array) == 1