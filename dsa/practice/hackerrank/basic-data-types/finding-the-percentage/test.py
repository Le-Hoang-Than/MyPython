from solution import average


def test_average():
    data = {
        'Krishna': [67, 68, 69],
        'Arjun': [70, 98, 63],
        'Malika': [52, 56, 60]
    }
    assert round(average(data,'Malika'), 2) == 56.00
