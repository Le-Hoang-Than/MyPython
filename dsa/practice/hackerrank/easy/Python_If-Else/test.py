from solution import check_weird

def test_odd_number():
    assert check_weird(3) == "Weird"

def test_even_2_to_5():
    assert check_weird(2) == "Not Weird"
    assert check_weird(4) == "Not Weird"

def test_even_6_to_20():
    assert check_weird(6) == "Weird"
    assert check_weird(20) == "Weird"

def test_even_greater_20():
    assert check_weird(22) == "Not Weird"