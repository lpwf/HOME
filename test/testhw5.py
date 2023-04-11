import pytest
from homewk5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "nums,k,sum",
    [
        ([2, 5, 6, 5], 2, 11)
    ],
)
def test_find_maximal_subarray_sum(nums, k, sum):
    result = find_maximal_subarray_sum(nums, k)
    assert result == sum
