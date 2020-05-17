"""
Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from __future__ import print_function

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=1001):
    """We don't need to compute a grid, all the diagonals have a predictable formula."""
    top_right = lambda x: (2 * x + 1)**2
    top_left = lambda x: 4 * x**2 + 2 * x + 1
    bottom_left = lambda x: 4 * x**2 + 1
    bottom_right = lambda x: top_left(-x)

    running_sum = 1
    n = (n - 1) // 2  # We're computing numbers to the left and right, so we only need to go up to half the width.

    for i in range(1, n + 1):
        running_sum += top_left(i) + top_right(i) + bottom_right(i) + bottom_left(i)

    return running_sum


solve.answer = 669171001


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
