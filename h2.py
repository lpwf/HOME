"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = 0
    if len(data) < 3:  # Check the length of the array, which cannot be less than the value 2
        return False

    if data[-3] + data[-2] != data[-1]:  # Check that the outermost 3 elements belong to the Fibonacci sequence
        return False

    while data[i] + data[i + 1] != data[-1]:  # The cycle goes on until all elements are checked
        if data[i] + data[i + 1] == data[i + 2]:  # Checking each element for membership in a Fibonacci sequence
            i += 1
        else:
            return False

    return True
