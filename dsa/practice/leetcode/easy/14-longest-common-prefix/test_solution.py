import pytest
from solution import Solution


@pytest.mark.parametrize("strs, expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["a"], "a"),
    (["ab", "a"],"a")
])
def test_longest_common_prefix(strs, expected):
    s = Solution()

    assert s.longest_common_prefix(strs) == expected