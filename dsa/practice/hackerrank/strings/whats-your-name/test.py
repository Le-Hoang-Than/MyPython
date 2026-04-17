from solution import print_full_name

def test_print_full_name(capsys):
    print_full_name('Ross', 'Taylor')
    captured = capsys.readouterr().out
    assert  captured == 'Hello Ross Taylor! You just delved into python.\n'
