"""
The number 3797 has an interesting property. Being prime itself,
    it is possible to continuously remove digits from left to right,
    and remain prime at each stage: 3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math import log10, floor
from itertools import count

from sympy import Sieve, isprime


def two_sided_primes():
    def right_truncatable(n):
        for possible_prime in (n // 10**i for i in range(int(floor(log10(n))) + 1)):
            if not isprime(possible_prime):
                return False

        return True

    def left_truncatable(n):
        for possible_prime in (n % 10**i for i in range(int(floor(log10(n))) + 1, 0, -1)):
            if not isprime(possible_prime):
                return False

        return True

    s = Sieve()
    for i in count(5):
        prime_i = s[i]

        if left_truncatable(prime_i) and right_truncatable(prime_i):
            yield prime_i


def solve():
    """We're given the upper limit of 11. So just go until we find 11."""
    generator = two_sided_primes()
    return sum(next(generator) for _ in range(11))


solve.answer = 748317
