"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
    but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import os
import string


def same_digits(i, j):
    # The length of the two strings doesn't match, so they can't have the exact same digits.
    if len(i) != len(j):
        return False

    for digit in string.digits:
        # The counts of one of the digits doesn't match, so they can't have the exact same digits.
        if i.count(digit) != j.count(digit):
            return False

    return True


def solve():
    """No strategy here. Bruteforce."""
    n = 2
    while True:
        has_same_digits_as_multiples = True
        for i in range(2, 7):
            has_same_digits_as_multiples = same_digits(str(n), str(i * n))

            if not has_same_digits_as_multiples:
                break

        if has_same_digits_as_multiples:
            break

        n += 1

    return n


solve.answer = 142857
