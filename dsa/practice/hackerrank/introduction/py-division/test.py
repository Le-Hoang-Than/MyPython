from solution import div_a_b

def test_div_a_b(capsys):
    div_a_b(4,3)
    captured = capsys.readouterr().out.splitlines()
    assert captured == [str(4//3),str(4/3)]


def test_div_a_b_zero(capsys):
    div_a_b(4, 0)
    captured = capsys.readouterr().out.splitlines()
    assert captured == []
