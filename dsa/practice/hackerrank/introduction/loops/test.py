import pytest
from solution import loop


def test_loop_invalid():
    with pytest.raises(TypeError):
        loop("abc")


def test_loop(capsys):
    loop(4)
    captured = capsys.readouterr().out.splitlines()
    assert captured == ['0', '1', '4', '9']


def test_loop_zero(capsys):
    loop(0)
    captured = capsys.readouterr().out.splitlines()
    assert captured == []


def test_loop_one(capsys):
    loop(1)
    captured = capsys.readouterr().out.splitlines()
    assert captured == ['0']
