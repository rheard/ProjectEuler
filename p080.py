"""
It is well known that if the square root of a natural number is not an integer, then it is irrational.
    The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first
    one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first
    one hundred decimal digits for all the irrational square roots.
"""

import os

from decimal import Decimal, getcontext
from math import sqrt

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=100, d=100):
    """No strategy here. Bruteforce with an arbitrarily long precision."""
    if getcontext().prec < 128:
        getcontext().prec = 128

    return sum(
        sum(int(x) for x in str(Decimal(i).sqrt()).replace('.', '')[:d])
        for i in range(2, n) if not sqrt(i).is_integer()
    )


solve.answer = 40886


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
