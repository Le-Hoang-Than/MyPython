from solution import math


def test_match(capsys):
    math(6, 2)
    captured = capsys.readouterr().out.splitlines()
    assert captured == ["8", "4", "12"]
