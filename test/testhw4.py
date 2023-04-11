from typing import List

import pytest
from homewk4 import check_sum_of_four


@pytest.mark.parametrize(
    "a,b,c,d,num",
    [
        ([-1, 3, 4, 2], [3, -6, 7, 4, 1], [1, 5], [6, -4, 5], 3)
    ],
)
def test_check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int], num):
    result = check_sum_of_four(a, b, c, d)
    assert result == num
