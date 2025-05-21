"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from sympy import sieve

import os

try:
    from utils import output_answer
except ImportError:
    from .utils import output_answer


def solve(n=2 * 10**6):
    """No strategy here. Bruteforce."""
    return sum(sieve.primerange(2, n))


solve.answer = 142913828922


if __name__ == '__main__':
    output_answer(solve)
