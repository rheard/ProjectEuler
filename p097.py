"""
The first known prime found to exceed one million digits was discovered in 1999,
    and is a Mersenne prime of the form 2**6972593−1; it contains exactly 2,098,960 digits.
    Subsequently other Mersenne primes, of the form 2**p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 * 2**7830457 + 1.

Find the last ten digits of this prime number.
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(k=28433, n=7830457, m=10**10):
    """
    A Proth prime is a prime number of the form k * 2**n + 1.
    A Sierpinski number is a k value that will never produce a prime for all n.

    It is conjectured that 78557 is the smallest Sierpinski number,
        although there were smaller values for which no known prime existed.

    In late 2016, the Proth prime 10223 * 2**31172165 + 1 was found. It was the 7th largest
        prime ever found and currently is the largest known Proth prime.

    This function will return the Proth number k * 2**n + 1 mod m.
    """
    return (k * pow(2, n, m) + 1) % m


solve.answer = 8739992577


if __name__ == '__main__':
    output_answer(solve)
