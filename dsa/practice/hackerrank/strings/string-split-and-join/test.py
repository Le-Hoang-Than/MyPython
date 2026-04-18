from solution import split_and_join

def test_split_and_join_normal():
    assert split_and_join('this is a string') == 'this-is-a-string'

def test_split_and_join_only_space():
    assert split_and_join('     ') == ''

def test_split_and_join_multiple_spaces():
    assert split_and_join('  this  is  a  string  ') == 'this-is-a-string'
