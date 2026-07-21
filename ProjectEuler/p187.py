"""
A composite is a number containing at least two prime factors. For example, 15 = 3 * 5; 9 = 3 * 3; 12 = 2 * 2 * 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors:
    4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10**8, have precisely two, not necessarily distinct, prime factors?
"""

from math import ceil, sqrt

from sympy import sieve


def solve(n=10**8):
    """No strategy here. Bruteforce."""
    # I originally wrote this using a prime2 var and +=, but I just collapsed it all here for simplicity
    return sum(
        1
        for prime1 in sieve.primerange(2, ceil(sqrt(n)))
        for _ in sieve.primerange(prime1, n // prime1 + 1)
    )


solve.answer = 17427258
