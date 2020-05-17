"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

from __future__ import print_function

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=1000):
    """No strategy here. Bruteforce."""
    return sum(int(x) for x in str(2**n))


solve.answer = 1366


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
