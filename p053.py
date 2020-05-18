"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ^5C_3 = 10.

In general,

^nC_r =
n!
/
r! * (n-r)!
where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: ^23C_10 = 1144066.

How many, not necessarily distinct, values of  ^nC_r, for 1 <= n <= 100, are greater than one-million?
"""

import os

from math import factorial

try:
    from .utils import output_answer, binomial
except ImportError:
    from utils import output_answer, binomial


def solve():
    """The only "strategy" here is to use an efficient binomial function."""
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if binomial(n, r) > 1000000:
                count += 1

    return count


solve.answer = 4075


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
