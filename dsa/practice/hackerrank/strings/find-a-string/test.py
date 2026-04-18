from solution import count_substring

def test_count_substring_with_3_words():
    assert count_substring('ABCDCDC', 'CDC') == 2


def test_count_substring_with_2_words():
    assert count_substring('ThIsisCoNfUsInG', 'is') == 1


def test_count_substring_case_words():
    assert count_substring('ThIsisCoNfUsInG', 'thisis') == 0
