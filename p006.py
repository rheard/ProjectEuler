"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.
"""

from __future__ import print_function

import os

try:
    from .utils import output_answer, triangle
except ImportError:
    from utils import output_answer, triangle


def sum_of_squares(n):
    """The sum of all squares less and equal to n**2."""
    # return sum(x**2 for x in range(1, n + 1))
    # OEIS A000330 lists several formulas for this, after testing, this is the fastest:
    return n * (n + 1) * (2 * n + 1) // 6


def square_of_sum(n):
    """
    The square of the sum of all integers less than n.

    Fun facts:
        This is equal to the sum of all cubes <= n**3.
    """
    # return sum(range(1, n + 1))**2
    # Small shortcut: The sum of the numbers from 1 to n is the nth triangle number.
    return triangle(n)**2


def solve(n=100):
    """No strategy is required, but we have optimized the operations."""
    return int(square_of_sum(n) - sum_of_squares(n))


solve.answer = 25164150


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
