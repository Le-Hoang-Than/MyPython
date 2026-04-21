from solution import merge_the_tools


def test_merge_the_tools(capsys):
    merge_the_tools('AABCAAADA', 3)
    captured = capsys.readouterr().out.splitlines()
    assert captured == ['AB', 'CA', 'AD']
