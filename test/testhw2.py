import pytest
from homewk2 import check_fibonacci
from collections.abc import Sequence


@pytest.mark.parametrize(
    "list_nums,is_fibonachi",
    [
        ([0, 1, 1, 2, 3, 5, 8], True),
        ([0, 1, 3, 2, 3, 5, 8], False),
        ([0, 1, 1, 2], True),
    ],
)
def test_check_fibonacci(list_nums: Sequence[int], is_fibonachi: bool):
    result = check_fibonacci(list_nums)
    assert result == is_fibonachi
