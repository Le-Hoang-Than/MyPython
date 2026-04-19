from solution import validate_string

def test_validate_string(capsys):
    validate_string('qA2')
    captured = capsys.readouterr().out.splitlines()
    assert captured == ['True','True','True','True','True']