from solution import print_formatted
def test_print_formatted_spacing(capsys):
    print_formatted(2)
    captured = capsys.readouterr().out.splitlines()
    assert captured  == [
        " 1  1  1  1",
        " 2  2  2 10"
    ]
def test_print_formatted_logic(capsys):
    print_formatted(2)
    captured = capsys.readouterr().out.strip().splitlines()
    assert [line.split() for line in captured] == [
        ["1", "1", "1", "1"],
        ["2", "2", "2", "10"]
    ]


