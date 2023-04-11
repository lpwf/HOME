"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""

from typing import List, Tuple
from collections import Counter


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    counter = Counter(inp)  #
    least_common_element = min(counter, key=counter.get)  # Searches for the least common element
    most_common_element = max(counter, key=counter.get)  # Searches for the most common element
    return most_common_element, least_common_element
