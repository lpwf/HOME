"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""

from typing import List
import collections


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    summ = collections.Counter(first + second for first in a for second in b) # The number and possible values of two numbers from the first and second lists.
    return sum(summ[-third - forth] for third in c for forth in d) # All possible combinations when the sum of the four elements is zero
