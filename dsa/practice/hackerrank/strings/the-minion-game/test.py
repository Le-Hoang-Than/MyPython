from solution import minion_game

def test_minion_game(capsys):
    minion_game('BANANA')
    captured = capsys.readouterr().out.splitlines()
    assert captured == ['Stuart 12']