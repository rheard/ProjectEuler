"""
In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n
It can be verified that when n = 1260 there are 113 distinct solutions
    and this is the least value of n for which the total number of distinct
    solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions
    exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it
    is well beyond the limitations of a brute force approach it requires a
    clever implementation.
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

try:
    from .p108 import solve as _solve
except ImportError:
    from p108 import solve as _solve


def solve():
    return _solve(4 * 10**6)


solve.__doc__ = _solve.__doc__
solve.answer = 9350130049860600


if __name__ == '__main__':
    output_answer(solve)
