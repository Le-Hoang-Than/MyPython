from solution import average


def test_average():
    assert average([154, 161, 167, 170, 171, 174, 176, 182]) == '169.375'


def test_average_float():
    assert average([3, 7]) == '5.000'
