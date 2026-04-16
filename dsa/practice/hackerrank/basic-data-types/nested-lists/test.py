from solution import find_score_second


def test_find_score_second():
    assert find_score_second([
        ["Harry", 37.21],
        ["Berry", 37.21],
        ["Tina", 37.2],
        ["Akriti", 41],
        ["Harsh", 39]
    ]) == ["Berry", "Harry"]

