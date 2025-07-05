"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors each.
    What is the first of these numbers?
"""

from itertools import count

from sympy import factorint


def solve(n=4):
    """No strategy here. Bruteforce."""
    found_len = 0
    first_i = 0
    for i in count(2):
        if len(factorint(i)) == n:
            found_len += 1

            if found_len == 1:
                first_i = i
            elif found_len == n:
                break
        else:
            found_len = 0

    return first_i


solve.answer = 134043
