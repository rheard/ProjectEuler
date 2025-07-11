"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
    If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
    The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import string

from itertools import permutations


def solve():
    """No strategy here. Bruteforce."""
    for i, number in enumerate(permutations(string.digits)):
        if i == 10**6 - 1:
            return int("".join(number))


solve.answer = 2783915460
