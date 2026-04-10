from solution import check_weird


def test_odd():
    assert check_weird(3) == "Weird"


def test_even_2_5_lower():
    assert check_weird(2) == "Not Weird"


def test_even_2_5_upper():
    assert check_weird(5) == "Weird"


def test_even_6_20_lower():
    assert check_weird(6) == "Weird"


def test_even_6_20_upper():
    assert check_weird(20) == "Weird"


def test_even_gt_20():
    assert check_weird(22) == "Not Weird"


def test_min():
    assert check_weird(1) == "Weird"


def test_max():
    assert check_weird(100) == "Not Weird"
