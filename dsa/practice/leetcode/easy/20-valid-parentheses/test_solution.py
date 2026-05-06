import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("()", True),
    ("((", False),
    ("()[]{}", True),
    ("(){}}{", False),
    ("(]", False),
    ("]{", False),
    ("([])", True),
    ("([)]", False),
    ("[", False),
    ("]", False)
])
def test_is_valid(s, expected):
    f = Solution()

    assert f.is_valid(s) == expected
