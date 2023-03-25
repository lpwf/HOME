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
    result = 0
    while k > 0:  # The loop will be executed if the value of k is greater than 0
        Max = max(nums)  # Maximum value from the list
        result = result + Max
        nums.remove(Max)
        k -= 1
    return result



