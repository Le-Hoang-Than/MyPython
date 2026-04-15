from solution import func


def test_func_lower_boundary(capsys):
    func(1)
    captured = capsys.readouterr().out
    assert captured == "1"


def test_func_upper_boundary(capsys):
    func(150)
    captured = capsys.readouterr().out
    assert captured.startswith("123")
    assert captured.endswith("150")


def test_func_invalid_low(capsys):
    func(0)
    captured = capsys.readouterr().out
    assert captured == ""


def test_func_invalid_high(capsys):
    func(151)
    captured = capsys.readouterr().out
    assert captured == ""


def test_func_standard_case(capsys):
    func(5)
    captured = capsys.readouterr().out
    assert captured == "12345"
