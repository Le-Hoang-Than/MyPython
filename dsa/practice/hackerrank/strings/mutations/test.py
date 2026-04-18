from solution import mutate_string

def test_mutate_string():
    assert mutate_string('abracadabra', 5, 'k') == 'abrackdabra'