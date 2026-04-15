from solution import permutation

def test_permutations(capsys):
    result = permutation(1,2,2,3)
    assert [0,2,1] not in result