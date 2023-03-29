"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    subarray = []
    for i in range(len(nums)):
        subarray = nums[i:i + k]  # Array containing elements from i to i+k
        if sum(subarray) > max_sum:  # Checking the sum of the current subarray with the maximum amount found
            max_sum = sum(subarray)
    return max_sum




