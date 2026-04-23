from solution import exc_cmd


def test_exc_cmd_intersection_update():
    A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}
    cmd_lst = ['intersection_update', '10']
    N = {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}
    exc_cmd(A, N, cmd_lst)
    assert A == {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}


def test_exc_cmd_update():
    A = {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}
    cmd_lst = ['update', '2']
    N = {55, 66}
    exc_cmd(A, N, cmd_lst)
    assert A == {2, 3, 5, 6, 8, 9, 1, 4, 7, 11, 55, 66}

def test_exc_cmd_symmetric_difference_update():
    A = {2, 3, 5, 6, 8, 9, 1, 4, 7, 11, 55, 66}
    cmd_lst = ['symmetric_difference_update', '5']
    N = {22, 7, 35, 62, 58}
    exc_cmd(A, N, cmd_lst)
    assert A == {2, 3, 5, 6, 8, 9, 1, 4, 11, 55, 66, 22, 35, 62, 58}

def test_exc_cmd_difference_update():
    A = {2, 3, 5, 6, 8, 9, 1, 4, 11, 55, 66, 22, 35, 62, 58}
    cmd_lst = ['difference_update', '7']
    N = {11, 22, 35, 55, 58, 62, 66}
    exc_cmd(A, N, cmd_lst)
    assert A == {2, 3, 5, 6, 8, 9, 1, 4}

def test_exc_cmd_sum():
    assert sum({2, 3, 5, 6, 8, 9, 1, 4}) == 38
