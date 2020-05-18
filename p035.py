"""
The number, 197, is called a circular prime because all rotations of the digits:
    197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import os

from math import ceil, log10

from sympy import sieve

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


# For all functionss, primes should contain all primes up to 10**(ceil(log(n) / log(10)))
def circular(n, primes):
    def rotate(n, shift):
        return n[shift:] + n[:shift]

    is_circular = True
    for i in range(len(n)):
        if rotate(n, i) not in primes:
            is_circular = False
            break

    return is_circular


def circular_numbers(n=10**6, primes=None):
    if primes is None:
        target_numbers = set(str(x) for x in range(2, 10, 2))
        primes = set(x for x in
                     map(str, sieve.primerange(2, 10 ** ceil(log10(n))))
                     if len(set(x).union(target_numbers)) != 0)

    for prime in primes:
        if circular(prime, primes):
            yield prime


def solve(n=10**6, primes=None):
    """No strategy here. Bruteforce."""
    return len(set(circular_numbers(n, primes)))


solve.answer = 55


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)
