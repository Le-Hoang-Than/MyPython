from solution import Solution


def test_roman_to_int_hang_don_vi():
    s = Solution()
    assert s.roman_to_int('IV') == 4


def test_roman_to_int_hang_chuc():
    s = Solution()
    assert s.roman_to_int('XIV') == 14


def test_roman_to_int_hang_tram():
    s = Solution()
    assert s.roman_to_int('CD') == 400


def test_roman_to_int_hang_nghin():
    s = Solution()
    assert s.roman_to_int('MCMXCIV') == 1994
