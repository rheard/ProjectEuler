"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

import os

from sympy import prime

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=10001):
    """No strategy here. Bruteforce."""
    return prime(n)


solve.answer = 104743


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
