"""
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from __future__ import print_function

import os

from math import factorial

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=100):
    """No strategy here. Bruteforce."""
    return sum(int(x) for x in str(factorial(n)))


solve.answer = 648


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
