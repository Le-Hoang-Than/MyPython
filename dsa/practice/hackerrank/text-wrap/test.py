from solution import wrap


def test_warp_logic():
    w = wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4).splitlines()
    assert w == ['ABCD', 'EFGH', 'IJKL', 'IMNO', 'QRST', 'UVWX', 'YZ']

def test_warp_formating():
    w = wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)
    assert w == 'ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ'
