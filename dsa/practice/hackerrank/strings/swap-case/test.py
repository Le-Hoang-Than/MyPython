from solution import swap_case

def test_swap_case_normal():
    result = swap_case('HackerRank.com presents "Pythonist 2".')
    assert result == 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'

def test_swap_case_only_spaces():
    result = swap_case('   ')
    assert result == '   '

def test_swap_case_empty():
    result = swap_case('')
    assert result == ''

def test_swap_case_numbers():
    result = swap_case('1234567890')
    assert result == '1234567890'
