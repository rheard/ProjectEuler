"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from __future__ import print_function

import os

from sympy import primefactors

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=600851475143):
    """No strategy here. Bruteforce."""
    return max(primefactors(n))


solve.answer = 6857


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
