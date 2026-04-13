from solution import is_leap


def test_is_leap_divisible_by_4():
    assert is_leap(2023) == False



def test_is_leap_divisible_by_4_but_not_divisible_by_100():
    assert is_leap(2024) == True


def test_is_leap_divisible_by_100_but_not_divisible_by_400():
    assert is_leap(1900) == False


def test_is_leap_divisible_by_400():
    assert is_leap(2000) == True

