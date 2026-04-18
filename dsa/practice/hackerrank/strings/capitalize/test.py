from solution import solve


def test_basic_words():
    assert solve("hello world") == "Hello World"


def test_mixed_word_number():
    assert solve("1 w 2 r 3g") == "1 W 2 R 3g"


def test_multiple_spaces():
    assert solve("hello   world  lol") == "Hello   World  Lol"


def test_leading_spaces():
    assert solve("  hello world") == "  Hello World"


def test_only_spaces():
    assert solve("   ") == "   "


def test_empty():
    assert solve("") == ""


def test_number_prefix():
    assert solve("123abc test") == "123abc Test"
