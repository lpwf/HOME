"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = 2
    new_el = 0
    length_data = len(data)
    last_data_el = data[length_data - 1]

    true_fib_range = [0, 1]  # our original array

    while new_el < last_data_el:
        new_el = true_fib_range[i - 1] + true_fib_range[
            i - 2]

        true_fib_range.append(
            new_el)

        i += 1  # and add one to the variable i
    index_for_true_list = len(
        true_fib_range) - length_data  # to cover cases in which the Fibonacci sequence does not start with 0 and 1

    if index_for_true_list < 0:
        return False

    final_list = []  # created an empty array
    for i in range(index_for_true_list, len(true_fib_range)):
        final_list.append(true_fib_range[i])

        return final_list == data  # checking our array with this array by condition