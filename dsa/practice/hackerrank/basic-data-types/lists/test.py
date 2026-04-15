from solution import exe_cmd


def test_basic(capsys):
    commands = [
        "insert 0 5",
        "insert 1 10",
        "insert 0 6",
        "print",
        "remove 6",
        "append 9",
        "append 1",
        "sort",
        "print",
        "pop",
        "reverse",
        "print"
    ]
    exe_cmd(commands)
    captured = capsys.readouterr().out.splitlines()
    assert captured == ["[6, 5, 10]",\
                        "[1, 5, 9, 10]",\
                        "[9, 5, 1]"]
